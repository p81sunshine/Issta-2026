# 僵尸进程和系统卡死问题解决方案

## 问题分析

### 症状
- 训练在**第20步**时系统卡死
- 系统负载极高 (load average > 1200)
- **55个僵尸进程**
- **93.7% system CPU** (内核态CPU占用)
- **Ray TaskRunner CPU: 14359%** (相当于143个CPU核心)
- 内存持续增长
- **关键特征：前19步正常，第20步突然崩溃**

### 根本原因（累积性环境泄漏）

#### 1. **第20步触发多个操作**
```bash
trainer.save_freq=10     # 每10步保存checkpoint
trainer.test_freq=5      # 每5步运行验证
```
- 第20步 = 10的倍数 → **保存checkpoint**
- 第20步 = 5的倍数 → **运行验证**
- 两个操作同时触发，创建大量环境实例

#### 2. **进程爆炸**
```bash
n_parallel_agents=32        # 32个并行agent
max_workers=128             # 128个worker线程
filter_prompts_workers=64   # 64个过滤worker
ray_init.num_cpus=64        # 64个Ray CPU
```
**总计可能创建**: 32 × 128 = **数千个subprocess**

每个环境操作（pdb、grep、bash）都会fork子进程，导致：
- 进程数爆炸
- 系统CPU全部用于进程调度
- 子进程结束后变成僵尸进程（父进程没有wait()）

#### 3. **环境实例累积泄漏（最关键的Bug！）**

**核心Bug: `update_envs_and_agents` 不清理旧环境 (第233行)**
```python
def update_envs_and_agents(self, envs, agents):
    # ❌ 直接覆盖，旧环境对象丢失但subprocess仍在运行！
    self.envs = envs
    self.agents = agents
```

**累积过程（这就是为什么是第20步！）：**
```
Step 1: 创建32个环境 → rollout完成 → 环境保留在self.envs
Step 2: init_envs_and_agents() → 创建32个新环境 → 覆盖self.envs
        ❌ 旧的32个环境对象被丢弃，但subprocess未清理 → 32个泄漏
Step 3: 再创建32个新环境 → 又覆盖
        ❌ Step 2的32个环境泄漏 → 累计64个
...
Step 20: 19×32 = 608个环境泄漏！
        每个环境 × 2-3个subprocess = 1216-1824个进程
        + 第20步触发保存+验证 → 系统崩溃！
```

**为什么是第20步？**
- 每步泄漏32个环境实例（约64-96个subprocess）
- 前19步累积：608个环境 = 1200-1800个进程
- 第20步 = 保存checkpoint + 验证同时触发
- 系统承受不住 → 崩溃

#### 4. **其他环境泄漏bug**

**Bug 2: 环境覆盖不清理 (第744行，execute_tasks方法)**
```python
# 直接覆盖旧环境，没有先close()
self.envs[index] = self.env_class.from_dict({**task, **self.env_args})
```
→ 旧环境的subprocess没有被清理，变成僵尸进程

**Bug 3: Executor强制关闭 (第705行)**
```python
self.executor.shutdown(wait=False, cancel_futures=True)
```
→ 取消正在执行的 `env.close()`，导致清理不完整

**Bug 4: 没有主动关闭所有环境**
在shutdown前没有遍历关闭所有环境实例

## 解决方案

### 1. 降低并发参数 ✅ (已修改)
```bash
# 修改前
n_parallel_agents=32
max_workers=128
filter_prompts_workers=64
ray_init.num_cpus=64
N_PARALLEL=8

# 修改后
n_parallel_agents=8      # 32 → 8
max_workers=16           # 128 → 16
filter_prompts_workers=16 # 64 → 16
ray_init.num_cpus=32     # 64 → 32
N_PARALLEL=4             # 8 → 4
```

### 2. 修复环境泄漏 ✅ (已修改)

**修改1: 创建环境前先关闭旧环境**
```python
# 在 execute_tasks 方法中 (第744行)
if self.envs[index] is not None:
    try:
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(self.executor, self.envs[index].close)
    except Exception as e:
        logger.warning(f"Failed to close old env at index {index}: {e}")

self.envs[index] = self.env_class.from_dict({**task, **self.env_args})
```

**修改2: Shutdown前主动关闭所有环境**
```python
# 在两个shutdown位置添加环境清理
loop = asyncio.get_event_loop()
close_tasks = []
for idx, env in enumerate(self.envs):
    if env is not None:
        try:
            close_tasks.append(loop.run_in_executor(self.executor, env.close))
        except Exception as e:
            logger.warning(f"Failed to initiate close for env {idx}: {e}")

if close_tasks:
    try:
        await asyncio.gather(*close_tasks, return_exceptions=True)
    except Exception as e:
        logger.warning(f"Error during environment cleanup: {e}")
```

**修改3: 等待executor完全关闭**
```python
# 从 wait=False 改为 wait=True
self.executor.shutdown(wait=True)  # 等待所有任务完成
```

### 3. 清理当前僵尸进程

使用提供的清理脚本：
```bash
cd /home/jiaxingliu/workspace/swe-pdb/rllm/examples/swe-pdb
./cleanup_zombies.sh
```

选项：
1. **停止Ray** (推荐先尝试)
2. **强制终止所有训练进程** (如果Ray停止无效)
3. **系统重启** (最后手段)

### 4. 监控训练过程

使用监控脚本实时查看资源使用：
```bash
./monitor_training.sh
```

会每5秒显示：
- 系统负载
- 内存使用
- 僵尸进程数
- Ray进程数
- Top CPU/内存进程

## 预防措施

### 1. 调整验证频率
如果问题仍然出现，可以减少验证频率：
```bash
trainer.test_freq=10  # 从5改为10，避免与save_freq冲突
```

### 2. 限制验证batch size
```bash
data.val_batch_size=64  # 从128减少到64
```

### 3. 增加环境超时
```bash
rllm.agent.trajectory_timeout=3600  # 从5400减少到3600，更快超时
```

### 4. 启用环境清理日志
在环境类中添加日志确认清理：
```python
def close(self):
    logger.info(f"Closing environment instance {id(self)}")
    # ... 清理代码
```

## 验证修复

重新运行训练后，检查：

1. **第20步是否正常通过**
```bash
# 查看wandb或日志确认step 20-25正常
```

2. **僵尸进程数量**
```bash
ps aux | grep 'Z' | wc -l
# 应该保持在0或个位数
```

3. **系统负载**
```bash
uptime
# load average应该 < 100
```

4. **CPU使用**
```bash
top
# system CPU应该 < 10%
```

## 技术细节

### 为什么是第20步？
- 第20步 = lcm(save_freq=10, test_freq=5) 的倍数
- 同时触发：
  - Checkpoint保存 (IO密集)
  - 验证运行 (创建大量新环境)
  - 旧环境未清理
- 资源需求叠加导致系统崩溃

### 僵尸进程形成原理
1. 环境调用 `subprocess.Popen()` 创建子进程 (pdb/grep/bash)
2. 子进程执行完毕，变成"defunct"状态
3. 父进程应该调用 `wait()` 读取退出状态
4. 如果父进程没有wait()，子进程变成僵尸
5. 僵尸进程占用进程表项，导致系统无法创建新进程

### 93.7% system CPU的原因
- 大量进程创建/销毁 (fork/exit系统调用)
- 进程调度和上下文切换
- 内核处理僵尸进程清理
- 几乎没有实际用户态工作

## 修改的文件

1. ✅ `train_swepdb_8b.sh` - 降低并发参数
2. ✅ `agent_execution_engine.py` - 修复环境泄漏
3. ✅ `cleanup_zombies.sh` - 清理脚本（新建）
4. ✅ `monitor_training.sh` - 监控脚本（新建）

## 联系与反馈

如果修复后问题仍然存在，请检查：
1. debug-gym的LocalTerminal是否正确实现close()
2. 是否有其他地方创建subprocess没有清理
3. Ray配置是否合理




































