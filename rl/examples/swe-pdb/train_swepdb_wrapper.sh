#!/bin/bash
set -euo pipefail

# 包装脚本：监控训练脚本输出，如果10分钟内没有新输出则kill并重启
# 使用方法: ./train_swepdb_14b_wrapper.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TRAIN_SCRIPT="${SCRIPT_DIR}/train_swepdb_4b.sh"
TIMEOUT_SECONDS=1200  # 10分钟 = 600秒
LOG_DIR="${SCRIPT_DIR}/wrapper_logs"
RESTART_COUNT=0
MAX_RESTARTS=100  # 最大重启次数，防止无限循环

# 创建日志目录
mkdir -p "$LOG_DIR"

# 查找训练相关的所有进程
find_training_processes() {
    # 查找Python训练进程
    pgrep -f "rllm.trainer.verl.train_agent_ppo" 2>/dev/null || true
    # 查找可能的Ray进程
    pgrep -f "train_agent_ppo" 2>/dev/null || true
}

# 清理函数：kill所有相关进程
cleanup() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 清理进程..."
    
    # 方法1: 如果知道主进程组ID，kill整个进程组
    if [ ! -z "${MAIN_PGID:-}" ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] 终止进程组 ${MAIN_PGID}..." | tee -a "${LOG_DIR}/wrapper.log"
        kill -TERM -"${MAIN_PGID}" 2>/dev/null || true
        sleep 2
        kill -KILL -"${MAIN_PGID}" 2>/dev/null || true
    fi
    
    # 方法2: 如果知道主进程PID，kill进程及其子进程
    if [ ! -z "${MAIN_PID:-}" ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] 终止主进程 ${MAIN_PID} 及其子进程..." | tee -a "${LOG_DIR}/wrapper.log"
        # 获取进程组ID并kill
        local pgid=$(ps -o pgid= -p "${MAIN_PID}" 2>/dev/null | tr -d ' ' || echo "")
        if [ ! -z "$pgid" ]; then
            kill -TERM -"$pgid" 2>/dev/null || true
            sleep 2
            kill -KILL -"$pgid" 2>/dev/null || true
        fi
        # 也直接kill主进程
        kill -TERM "${MAIN_PID}" 2>/dev/null || true
        sleep 2
        kill -KILL "${MAIN_PID}" 2>/dev/null || true
    fi
    
    # 方法3: 通过进程名查找并kill训练相关进程
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 查找并终止训练相关进程..." | tee -a "${LOG_DIR}/wrapper.log"
    local pids=$(find_training_processes)
    if [ ! -z "$pids" ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] 找到训练进程: $pids" | tee -a "${LOG_DIR}/wrapper.log"
        for pid in $pids; do
            # 获取进程组并kill
            local pgid=$(ps -o pgid= -p "$pid" 2>/dev/null | tr -d ' ' || echo "")
            if [ ! -z "$pgid" ]; then
                kill -TERM -"$pgid" 2>/dev/null || true
            fi
            kill -TERM "$pid" 2>/dev/null || true
        done
        sleep 2
        for pid in $pids; do
            kill -KILL "$pid" 2>/dev/null || true
        done
    fi
    
    # 方法4: 使用pkill作为最后手段
    pkill -f "train_agent_ppo" 2>/dev/null || true
    pkill -f "rllm.trainer.verl.train_agent_ppo" 2>/dev/null || true
    
    # 等待一下确保进程被清理
    sleep 2
    
    # 验证是否还有残留进程
    local remaining=$(find_training_processes)
    if [ ! -z "$remaining" ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] 警告: 仍有残留进程: $remaining" | tee -a "${LOG_DIR}/wrapper.log"
    else
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] 所有训练进程已清理" | tee -a "${LOG_DIR}/wrapper.log"
    fi
}

# 监控函数：检测输出超时
monitor_output() {
    local output_file="$1"
    local last_size=0
    local current_size=0
    local last_change_time=$(date +%s)
    local check_interval=30  # 每30秒检查一次
    local timeout=$TIMEOUT_SECONDS
    
    while true; do
        sleep $check_interval
        
        # 检查主进程是否还在运行
        if [ ! -z "${MAIN_PID:-}" ]; then
            if ! kill -0 "${MAIN_PID}" 2>/dev/null; then
                echo "[$(date '+%Y-%m-%d %H:%M:%S')] 主进程 ${MAIN_PID} 已退出" | tee -a "${LOG_DIR}/monitor.log"
                return 2  # 返回2表示进程已退出
            fi
        fi
        
        # 也检查是否还有Python训练进程在运行
        local python_pids=$(find_training_processes)
        if [ -z "$python_pids" ] && [ ! -z "${MAIN_PID:-}" ]; then
            # 如果找不到Python进程，但主进程还在，可能是进程已经退出但PID还在
            if ! kill -0 "${MAIN_PID}" 2>/dev/null; then
                echo "[$(date '+%Y-%m-%d %H:%M:%S')] 训练进程已全部退出" | tee -a "${LOG_DIR}/monitor.log"
                return 2
            fi
        fi
        
        if [ ! -f "$output_file" ]; then
            # 文件不存在，重置计时
            last_change_time=$(date +%s)
            continue
        fi
        
        # 检查文件大小是否变化
        current_size=$(stat -c %s "$output_file" 2>/dev/null || echo 0)
        
        if [ $current_size -ne $last_size ]; then
            # 文件大小有变化，说明有新输出
            last_size=$current_size
            last_change_time=$(date +%s)
        else
            # 文件大小没变化，检查是否超时
            local current_time=$(date +%s)
            local elapsed=$((current_time - last_change_time))
            
            if [ $elapsed -ge $timeout ]; then
                echo "[$(date '+%Y-%m-%d %H:%M:%S')] 检测到超时：${elapsed}秒内没有新输出 (文件大小: ${current_size} bytes)" | tee -a "${LOG_DIR}/monitor.log"
                return 1  # 返回1表示超时
            fi
        fi
    done
}

# 运行训练脚本
run_training() {
    local run_id=$(date +%Y%m%d_%H%M%S)
    local output_file="${LOG_DIR}/train_output_${run_id}.log"
    local timeout_occurred=0
    
    echo "==========================================" | tee -a "${LOG_DIR}/wrapper.log"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 开始第 $((RESTART_COUNT + 1)) 次训练运行" | tee -a "${LOG_DIR}/wrapper.log"
    echo "输出文件: $output_file" | tee -a "${LOG_DIR}/wrapper.log"
    echo "==========================================" | tee -a "${LOG_DIR}/wrapper.log"
    
    # 启动训练脚本，将输出同时写入文件和终端
    # 使用 setsid 创建新的进程组，便于后续管理
    # 使用 stdbuf 确保输出是行缓冲的，这样能更快检测到新输出
    setsid stdbuf -oL -eL bash "$TRAIN_SCRIPT" 2>&1 | tee "$output_file" &
    local bash_pid=$!
    
    # 获取进程组ID
    MAIN_PGID=$(ps -o pgid= -p "$bash_pid" 2>/dev/null | tr -d ' ' || echo "")
    MAIN_PID=$bash_pid
    
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 启动训练脚本，Bash PID: ${MAIN_PID}, 进程组ID: ${MAIN_PGID}" | tee -a "${LOG_DIR}/wrapper.log"
    
    # 等待一下确保文件被创建，并找到真正的Python训练进程
    sleep 10
    
    # 尝试找到真正的Python训练进程
    local python_pids=$(pgrep -f "rllm.trainer.verl.train_agent_ppo" 2>/dev/null || true)
    if [ ! -z "$python_pids" ]; then
        # 取第一个找到的Python进程作为主进程
        local first_python_pid=$(echo "$python_pids" | head -n1)
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] 找到Python训练进程: $python_pids，使用 PID: $first_python_pid 作为主进程" | tee -a "${LOG_DIR}/wrapper.log"
        MAIN_PID=$first_python_pid
        MAIN_PGID=$(ps -o pgid= -p "$first_python_pid" 2>/dev/null | tr -d ' ' || echo "")
    else
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] 警告: 未找到Python训练进程，使用Bash PID: ${MAIN_PID}" | tee -a "${LOG_DIR}/wrapper.log"
    fi
    
    # 启动监控进程
    monitor_output "$output_file" &
    MONITOR_PID=$!
    
    # 等待主进程或监控进程结束
    wait $MAIN_PID 2>/dev/null
    MAIN_EXIT_CODE=$?
    
    # 检查监控进程的退出状态
    wait $MONITOR_PID 2>/dev/null
    MONITOR_EXIT_CODE=$?
    
    # 如果监控进程因为超时退出（退出码1），需要kill主进程
    if [ $MONITOR_EXIT_CODE -eq 1 ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] 监控检测到超时，正在终止训练进程..." | tee -a "${LOG_DIR}/wrapper.log"
        timeout_occurred=1
        
        # 尝试优雅终止
        kill -TERM $MAIN_PID 2>/dev/null || true
        sleep 5
        
        # 如果还在运行，强制kill
        if kill -0 $MAIN_PID 2>/dev/null; then
            echo "[$(date '+%Y-%m-%d %H:%M:%S')] 强制终止训练进程..." | tee -a "${LOG_DIR}/wrapper.log"
            kill -KILL $MAIN_PID 2>/dev/null || true
        fi
        
        # 清理可能的子进程
        cleanup
        
        wait $MAIN_PID 2>/dev/null || true
        MAIN_EXIT_CODE=124  # 使用124表示超时（与timeout命令一致）
    fi
    
    # 检查退出原因
    if [ $timeout_occurred -eq 1 ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] 训练因超时被终止" | tee -a "${LOG_DIR}/wrapper.log"
        return 1
    elif [ $MAIN_EXIT_CODE -eq 0 ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] 训练正常完成，退出码: $MAIN_EXIT_CODE" | tee -a "${LOG_DIR}/wrapper.log"
        return 0
    else
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] 训练异常退出，退出码: $MAIN_EXIT_CODE" | tee -a "${LOG_DIR}/wrapper.log"
        return 1
    fi
}

# 主循环
main() {
    # 设置信号处理
    trap cleanup EXIT INT TERM
    
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 启动训练包装脚本" | tee -a "${LOG_DIR}/wrapper.log"
    echo "训练脚本: $TRAIN_SCRIPT" | tee -a "${LOG_DIR}/wrapper.log"
    echo "超时时间: ${TIMEOUT_SECONDS}秒 (10分钟)" | tee -a "${LOG_DIR}/wrapper.log"
    echo "日志目录: $LOG_DIR" | tee -a "${LOG_DIR}/wrapper.log"
    
    while [ $RESTART_COUNT -lt $MAX_RESTARTS ]; do
        # 清理之前的进程（如果有）
        cleanup
        
        # 运行训练
        if run_training; then
            echo "[$(date '+%Y-%m-%d %H:%M:%S')] 训练成功完成，退出" | tee -a "${LOG_DIR}/wrapper.log"
            exit 0
        fi
        
        RESTART_COUNT=$((RESTART_COUNT + 1))
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] 准备重启训练 (第 ${RESTART_COUNT} 次重启)" | tee -a "${LOG_DIR}/wrapper.log"
        
        # 等待一下再重启
        sleep 10
    done
    
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 达到最大重启次数 (${MAX_RESTARTS})，退出" | tee -a "${LOG_DIR}/wrapper.log"
    exit 1
}

# 运行主函数
main
