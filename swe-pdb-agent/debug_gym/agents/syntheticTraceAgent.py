from pathlib import Path

from debug_gym.agents.base_agent import BaseAgent, register_agent


@register_agent
class SyntheticTraceDebugAgent(BaseAgent):
    name: str = "synthetic_trace_debug_agent"
    system_prompt = (
    "You are an AI debugging assistant specialized in generating synthetic debugging traces "
    "using the provided tools (`view`, `eval`, `pdb`, and `rewrite`).\n\n"

    "You must:\n"
    "- Use these tools exactly as defined.\n"
    "- Strictly follow the workflow order specified in the user instructions: "
    "- Follow the user’s instructions as the debugging scenario description.\n"
    "- Never set breakpoints on the function definition line.\n"
    "- Compare with the correct code to learn how to fix the bug.\n"
    "- Never attemp to create a new file to reproduce the issue."
    "- You do not have ability to create a new file, so do not start pdb or rewrite on a file that is not exist."
)

    
    def __init__(self, config: dict, env, llm=None, logger=None):
        super().__init__(config, env, llm, logger)
    
    def _default_system_prompt(self, info) -> str:
        """返回默认的系统提示。"""
        # system_prompt_dict = {
        #     "Overall task": self.system_prompt,
        #     "Instructions": info.instructions,
        # }
        
        # if self._show_directory_tree():
        #     system_prompt_dict["Repo directory tree"] = self.trim_message(
        #         info.dir_tree, max_length_percentage=0.1, where="end"
        #     )
        
        # if self._show_current_breakpoints():
        #     system_prompt_dict["Current breakpoints"] = info.current_breakpoints
        
        # if self._auto_eval_on_rewrite():
        #     system_prompt_dict["Evaluation output of current code"] = self.trim_message(
        #         info.eval_observation.observation,
        #         max_length_percentage=0.8,
        #         where="middle",
        #     )
        
        shortcut_features = self.shortcut_features()
        # if shortcut_features:
        #     system_prompt_dict["Shortcut features"] = shortcut_features
        
        # return self.to_pretty_json(system_prompt_dict)
        return self.system_prompt + "\n\n" + "Additional tool details: " + "\n".join(shortcut_features)
