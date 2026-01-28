import json
import sys
from pathlib import Path

import pytest


def _ensure_debug_gym_importable():
    """Add the local debug_gym package (swe-pdb/debug_gym) to sys.path."""
    project_root = Path(__file__).resolve().parents[3]
    debug_gym_root = project_root / "swe-pdb"
    if str(debug_gym_root) not in sys.path:
        sys.path.insert(0, str(debug_gym_root))


_ensure_debug_gym_importable()

# Skip the whole module if debug_gym is not available.
pytest.importorskip("debug_gym")

from rllm.environments.debug_gym.kodcode_env import KodCodeDebugGymEnv  # noqa: E402
from rllm.trainer import env_agent_mappings  # noqa: E402


@pytest.fixture()
def tmp_kodcode_dataset(tmp_path):
    """Create a minimal KodCode dataset with one passing test."""
    task_dir = tmp_path / "task1"
    task_dir.mkdir()
    (task_dir / "test.py").write_text(
        "from task1_code import add\n\n"
        "def test_add():\n"
        "    assert add(1, 2) == 3\n",
        encoding="utf-8",
    )
    (task_dir / "task1_code.py").write_text(
        "def add(a, b):\n"
        "    return a + b\n",
        encoding="utf-8",
    )
    return tmp_path


def test_reset_and_eval_step_local(tmp_kodcode_dataset):
    env = KodCodeDebugGymEnv(
        instance_id="task1",
        problems=["task1"],
        data_path=str(tmp_kodcode_dataset),
        backend="local",
        max_steps=2,
        enable_pdb=False,
        enable_grep=False,
        enable_bash=False,
        show_directory_tree=False,
        show_current_breakpoints=False,
    )

    observation, info = env.reset()

    assert "Investigate the repository" in observation  # instructions from KodCodeEnv
    assert info["instance_id"] == "task1"
    assert isinstance(info["done"], bool)
    assert info["score"] in (0, 1)
    assert info["max_score"] is None or info["max_score"] >= 0

    # Run eval to execute pytest and update score/resolution
    action_json = json.dumps({"name": "eval", "arguments": {}})
    observation, reward, done, info = env.step(action_json)

    assert isinstance(observation, str) and observation
    assert reward == 0.0  # wrapper sets immediate reward to 0
    assert done is True  # max_score == score => resolved
    assert info["terminated"] is True
    assert info["score"] >= 1
    assert info["max_score"] >= info["score"]
    assert env.compute_final_reward() > 0.0


def test_env_agent_mapping_has_kodcode():
    assert "kodcode_debug_gym" in env_agent_mappings.ENV_CLASS_MAPPING
    assert env_agent_mappings.ENV_CLASS_MAPPING["kodcode_debug_gym"] is not None

env_config = {
    "backend": "local",
    "show_directory_tree": False,
    "show_current_breakpoints": False,
    "enable_pdb": True,
    "enable_grep": True,
    "enable_bash": False,
    "max_steps": 2,
    "data_path": "/home/jiaxingliu/workspace/swe-pdb/temp",
}

def test_from_dict_recreates_files():
    extra_info_payload = {
        "task_name": "taskX",
        "entrypoint": "python -m pytest --tb=no -s test.py",
        "files": [
            {"path": "test.py", "content": "from code import add\n\ndef test_add():\n    assert add(2,3)==5\n"},
            {"path": "code.py", "content": "def add(a,b):\n    return a+b\n"},
        ],
    }

    env = KodCodeDebugGymEnv.from_dict({**extra_info_payload, **env_config})
    observation, info = env.reset()
    assert info["instance_id"] == "taskX"
    assert "Investigate the repository" in observation

    obs, reward, done, info = env.step(json.dumps({"name": "eval", "arguments": {}}))
    assert isinstance(obs, str) and obs
    assert reward == 0.0
    assert done is True
    assert info["terminated"] is True
    assert env.compute_final_reward() > 0.0


# def test_from_parquet_creates_envs(tmp_path):
#     pd = pytest.importorskip("pandas")
#     try:
#         import pyarrow  # noqa: F401
#     except ImportError:
#         pytest.skip("pyarrow not available for parquet test")

#     payloads = []
#     for i in range(2):
#         task_name = f"task{i}"
#         payloads.append(
#             {
#                 "extra_info": json.dumps(
#                     {
#                         "task_name": task_name,
#                         "files": [
#                             {
#                                 "path": "test.py",
#                                 "content": f"from code import add\n\ndef test_add():\n    assert add({i}, {i+1}) == {2*i+1}\n",
#                             },
#                             {"path": "code.py", "content": "def add(a,b):\n    return a+b\n"},
#                         ],
#                     }
#                 ),
#                 "backend": "local",
#                 "show_directory_tree": False,
#                 "show_current_breakpoints": False,
#                 "enable_pdb": False,
#                 "enable_grep": False,
#                 "enable_bash": False,
#                 "max_steps": 1,
#             }
#         )

#     parquet_path = tmp_path / "tasks.parquet"
#     pd.DataFrame(payloads).to_parquet(parquet_path)

#     records = pd.read_parquet(parquet_path).to_dict(orient="records")

#     created_dirs = []
#     for rec in records:
#         env = KodCodeDebugGymEnv.from_dict(rec)
#         assert env._tmp_dataset_dir and env._tmp_dataset_dir.exists()
#         created_dirs.append(env._tmp_dataset_dir)
#         observation, info = env.reset()
#         assert isinstance(observation, str)
#         assert info["instance_id"] in ("task0", "task1")
#         env.close()
#         assert not env._tmp_dataset_dir.exists()

#     assert created_dirs[0] != created_dirs[1]


def test_real_parquet_row_if_available():
    """If the real parquet exists and deps are present, ensure we can build an env from one row."""
    pd = pytest.importorskip("pandas")
    try:
        import pyarrow  # noqa: F401
    except ImportError:
        pytest.skip("pyarrow not available for parquet test")

    parquet_path = Path(__file__).resolve().parents[2] / "rl_1125.parquets"
    if not parquet_path.exists():
        pytest.skip(f"Parquet not found at {parquet_path}")

    df = pd.read_parquet(parquet_path)
    if df.empty:
        pytest.skip("Parquet is empty")

    rec = df.iloc[0].to_dict()
    env = KodCodeDebugGymEnv.from_dict({**rec, **env_config})
    observation, info = env.reset()
    assert isinstance(observation, str)
    assert isinstance(info.get("instance_id"), str)
    env.close()
