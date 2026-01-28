# 如何在 KodCodeDebugGymEnv 中使用 Tools

## 概述

`KodCodeDebugGymEnv` 现在支持将环境中的 tools 自动转换为 OpenAI function calling 格式，并传递给模型进行生成。

## 功能特性

1. **自动工具转换**：环境中的 tools（ViewTool, ListdirTool, EvalTool, RewriteTool, PDBTool, GrepTool, BashTool）会自动转换为 OpenAI 格式
2. **无缝集成**：tools 会自动包含在环境的 `info` 中，供 agent 和引擎使用
3. **支持两种模式**：
   - 有 tokenizer：tools 会被格式化到 prompt 字符串中
   - 无 tokenizer（使用 chat completions API）：tools 会作为 `tools` 参数传递给 OpenAI API

## 使用方法

### 基本使用

当你使用 `KodCodeDebugGymEnv` 时，tools 会自动包含在环境的 `info` 中：

```python
from rllm.environments.debug_gym.kodcode_env import KodCodeDebugGymEnv

# 创建环境
env = KodCodeDebugGymEnv(
    enable_pdb=True,
    enable_grep=True,
    enable_bash=False,
)

# 重置环境
observation, info = env.reset()

# info 中现在包含 tools_openai_format 字段
tools = info.get("tools_openai_format")
print(f"可用工具数量: {len(tools)}")
for tool in tools:
    print(f"- {tool['function']['name']}: {tool['function']['description']}")
```

### 在 AgentExecutionEngine 中使用

`AgentExecutionEngine` 会自动从环境的 `info` 中提取 tools 并传递给模型：

```python
from rllm.engine.agent_execution_engine import AgentExecutionEngine
from rllm.agents.debug_gym_agent import DebugGymAgent
from rllm.environments.debug_gym.kodcode_env import KodCodeDebugGymEnv

# 创建引擎（不提供 tokenizer 以使用 chat completions API）
engine = AgentExecutionEngine(
    engine_name="openai",
    tokenizer=None,  # 不提供 tokenizer 会使用 chat completions API，支持 tools 参数
    rollout_engine_args={
        "model": "gpt-4o",
        "base_url": "https://api.openai.com/v1",
        "api_key": os.getenv("OPENAI_API_KEY"),
    },
    agent_class=DebugGymAgent,
    env_class=KodCodeDebugGymEnv,
    env_args={
        "enable_pdb": True,
        "enable_grep": True,
    },
)

# 运行任务时，tools 会自动传递
trajectories = await engine.execute_tasks([task1, task2, ...])
```

### 手动获取工具定义

如果需要手动获取工具的 OpenAI 格式定义：

```python
env = KodCodeDebugGymEnv()

# 获取工具的 OpenAI 格式
tools_openai = env.get_tools_for_openai()

# 现在可以传递给 OpenAI API 或用于其他目的
for tool in tools_openai:
    print(json.dumps(tool, indent=2))
```

## 工具格式

每个工具都会被转换为以下格式：

```json
{
  "type": "function",
  "function": {
    "name": "view",
    "description": "View the contents of a file",
    "parameters": {
      "type": "object",
      "properties": {
        "file_path": {
          "type": "string",
          "description": "Path to the file to view"
        }
      },
      "required": ["file_path"],
      "additionalProperties": false
    }
  }
}
```

## 注意事项

1. **使用 chat completions API**：要使用 OpenAI function calling 功能，需要确保 `OpenAIEngine` 不使用 tokenizer（即 `tokenizer=None`），这样会使用 chat completions API 而不是 completions API。

2. **工具一致性**：环境中的 tools 和传递给模型的 tools 会保持一致，确保模型调用的工具名称与环境中注册的工具名称匹配。

3. **动态工具**：如果环境在运行时动态添加或移除工具，`tools_openai_format` 会在每次 `reset()` 和 `step()` 时更新。

## 示例：完整的调试流程

```python
import asyncio
from rllm.engine.agent_execution_engine import AgentExecutionEngine
from rllm.agents.debug_gym_agent import DebugGymAgent
from rllm.environments.debug_gym.kodcode_env import KodCodeDebugGymEnv

async def main():
    # 创建引擎
    engine = AgentExecutionEngine(
        engine_name="openai",
        tokenizer=None,  # 使用 chat completions API 以支持 tools
        rollout_engine_args={
            "model": "gpt-4o",
            "api_key": os.getenv("OPENAI_API_KEY"),
        },
        agent_class=DebugGymAgent,
        env_class=KodCodeDebugGymEnv,
        env_args={
            "enable_pdb": True,
            "enable_grep": True,
            "enable_bash": False,
        },
        max_steps=10,
    )
    
    # 创建任务
    task = {
        "files": [...],
        "entrypoint": "python -m pytest test.py",
    }
    
    # 执行任务
    trajectories = await engine.execute_tasks([task])
    
    # 模型现在可以使用所有环境中的工具进行调试

if __name__ == "__main__":
    asyncio.run(main())
```

## 总结

通过这个实现，你可以：
- ✅ 自动将 debug-gym 环境中的 tools 转换为 OpenAI 格式
- ✅ 无缝集成到现有的 agent 和引擎架构中
- ✅ 支持 OpenAI function calling API
- ✅ 保持工具定义的一致性

所有工具（ViewTool, ListdirTool, EvalTool, RewriteTool, PDBTool, GrepTool, BashTool）都会自动可用。

