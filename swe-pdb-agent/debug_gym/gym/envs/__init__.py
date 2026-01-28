from debug_gym.gym.envs.aider import AiderBenchmarkEnv
from debug_gym.gym.envs.env import RepoEnv, TooledEnv
from debug_gym.gym.envs.kodcode import KodCodeEnv
from debug_gym.gym.envs.mini_nightmare import MiniNightmareEnv
from debug_gym.gym.envs.pdb_better import PdbBetterEnv
from debug_gym.gym.envs.r2egym import R2EGymEnv
from debug_gym.gym.envs.swe_bench import SWEBenchEnv
from debug_gym.gym.envs.swe_bench_debug import SWEBenchDebugEnv
from debug_gym.gym.envs.swe_smith import SWESmithEnv
from debug_gym.gym.envs.synthetic import SyntheticEnv
from debug_gym.gym.envs.r2egym_debug import R2EGymDebugEnv
from debug_gym.gym.envs.editbench import EditBenchEnv
from debug_gym.gym.envs.canitedit import CaniTEditEnv


def select_env(env_type: str = None) -> type[RepoEnv]:
    match env_type:
        case None:
            return RepoEnv
        case "aider":
            return AiderBenchmarkEnv
        case "swebench":
            return SWEBenchEnv
        case "swebench-debug":
            return SWEBenchDebugEnv
        case "swesmith":
            return SWESmithEnv
        case "mini_nightmare":
            return MiniNightmareEnv
        case "pdb-better":
            return PdbBetterEnv
        case "r2egym":
            return R2EGymEnv
        case "kodcode":
            return KodCodeEnv
        case "synthetic":
            return SyntheticEnv
        case "r2egym-debug":
            return R2EGymDebugEnv
        case "editbench":
            return EditBenchEnv
        case "canitedit":
            return CaniTEditEnv
        case _:
            raise ValueError(f"Unknown benchmark {env_type}")
