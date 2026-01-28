from solution import *

import math

from solution import *

import math

from solution import *

import math

import os
import subprocess
from unittest.mock import patch, mock_open

def test_set_environment_variables():
    set_environment_variables()
    assert os.environ['TORCHINDUCTOR_UNIQUE_KERNEL_NAMES'] == '1'
    assert os.environ['TORCHINDUCTOR_BENCHMARK_KERNEL'] == '1'

@patch('subprocess.run')
def test_run_benchmark_script(mock_run):
    run_benchmark_script()
    mock_run.assert_called_with("python -u benchmarks/dynamo/timm_models.py --backend inductor --amp --performance --dashboard --only mixnet_l --disable-cudagraphs --training", shell=True)

def test_extract_compiled_module_path():
    log_data = "Some log lines\nSAVED: /path/to/compiled/module.py\nOther log lines"
    assert extract_compiled_module_path(log_data) == "/path/to/compiled/module.py"

@patch("builtins.open", new_callable=mock_open, read_data="Some log lines\nSAVED: /path/to/compiled/module.py\nOther log lines")
@patch("subprocess.run")
def test_analyze_performance_logs(mock_run, mock_file):
    log_path = "/path/to/performance/log"
    compiled_module_path = analyze_performance_logs(log_path)
    assert compiled_module_path == "/path/to/compiled/module.py"
    mock_run.assert_called_with("python /path/to/compiled/module.py -p", shell=True)

def test_extract_kernel_path():
    compiled_data = "Some compiled data\nKERNEL_PATH: /path/to/kernel.py\nMore compiled data"
    with patch("builtins.open", mock_open(read_data=compiled_data)):
        compiled_module_path = "/path/to/compiled/module.py"
        assert extract_kernel_path(compiled_module_path) == "/path/to/kernel.py"

@patch("subprocess.run")
def test_profile_individual_kernel(mock_run):
    kernel_path = "/path/to/kernel.py"
    profile_individual_kernel(kernel_path)
    assert os.environ['TORCHINDUCTOR_MAX_AUTOTUNE'] == '1'
    mock_run.assert_called_with("python /path/to/kernel.py", shell=True)