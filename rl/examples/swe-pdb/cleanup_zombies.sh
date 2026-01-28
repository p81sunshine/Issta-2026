#!/bin/bash
# 清理僵尸进程和相关训练进程的脚本

echo "========================================="
echo "清理SWE-PDB训练相关进程"
echo "========================================="

# 1. 查找并显示僵尸进程
echo -e "\n[1] 检查僵尸进程..."
zombie_count=$(ps aux | grep 'Z' | grep -v grep | wc -l)
if [ $zombie_count -gt 0 ]; then
    echo "发现 $zombie_count 个僵尸进程:"
    ps aux | grep 'Z' | grep -v grep
    
    # 找到僵尸进程的父进程
    echo -e "\n尝试找到僵尸进程的父进程..."
    ps -el | awk '$2 == "Z" {print $4}' | sort -u | while read ppid; do
        if [ ! -z "$ppid" ]; then
            echo "父进程 PID: $ppid"
            ps -p $ppid -o pid,cmd
        fi
    done
else
    echo "没有发现僵尸进程"
fi

# 2. 查找ray相关进程
echo -e "\n[2] 检查Ray进程..."
ray_procs=$(ps aux | grep 'ray::' | grep -v grep | wc -l)
if [ $ray_procs -gt 0 ]; then
    echo "发现 $ray_procs 个Ray进程"
    ps aux | grep 'ray::' | grep -v grep | head -5
fi

# 3. 查找训练脚本进程
echo -e "\n[3] 检查训练进程..."
train_procs=$(pgrep -f "train_agent_ppo" | wc -l)
if [ $train_procs -gt 0 ]; then
    echo "发现 $train_procs 个训练进程"
    pgrep -af "train_agent_ppo"
fi

# 4. 提供清理选项
echo -e "\n========================================="
echo "清理选项:"
echo "========================================="
echo "1. 停止Ray (推荐先尝试)"
echo "2. 强制终止所有训练相关进程"
echo "3. 重启（最彻底但会影响其他任务）"
echo "4. 仅显示状态，不执行清理"
echo ""
read -p "请选择操作 [1-4]: " choice

case $choice in
    1)
        echo -e "\n停止Ray..."
        ray stop --force
        sleep 2
        echo "Ray已停止，请重新检查进程状态"
        ;;
    2)
        echo -e "\n强制终止训练进程..."
        # 终止训练主进程
        pkill -9 -f "train_agent_ppo"
        sleep 1
        # 终止ray进程
        pkill -9 -f "ray::"
        sleep 1
        # 清理ray
        ray stop --force
        echo "进程已终止"
        ;;
    3)
        echo "请使用 'sudo reboot' 手动重启系统"
        ;;
    4)
        echo "仅显示状态，无操作"
        ;;
    *)
        echo "无效选择"
        ;;
esac

# 5. 显示最终状态
echo -e "\n========================================="
echo "当前系统状态:"
echo "========================================="
echo "负载: $(uptime | awk -F'load average:' '{print $2}')"
echo "僵尸进程数: $(ps aux | grep 'Z' | grep -v grep | wc -l)"
echo "Ray进程数: $(ps aux | grep 'ray::' | grep -v grep | wc -l)"
echo "训练进程数: $(pgrep -f "train_agent_ppo" | wc -l)"











