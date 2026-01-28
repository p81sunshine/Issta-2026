import os
import re
import subprocess

def set_environment_variables():
    os.environ['TORCHINDUCTOR_UNIQUE_KERNEL_NAMES'] = '1'
    os.environ['TORCHINDUCTOR_BENCHMARK_KERNEL'] = '1'


def run_benchmark_script():
    command = "python -u benchmarks/dynamo/timm_models.py --backend inductor --amp --performance --dashboard --only mixnet_l --disable-cudagraphs --training"
    subprocess.run(command, shell=True)


def extract_compiled_module_path(log_data):
    match = re.search(r"SAVED: (.+)\n", log_data)
    if match:
        return match.group(1)
    else:
        raise ValueError("Compiled module path not found in performance logs")


def analyze_performance_logs(log_path):
    with open(log_path, 'r') as log_file:
        log_data = log_file.read()
    compiled_module_path = extract_compiled_module_path(log_data)
    subprocess.run(f"python {compiled_module_path} -p", shell=True)
    return compiled_module_path


def extract_kernel_path(compiled_module_path):
    kernel_path_pattern = re.compile(r"KERNEL_PATH: (.+)")
    with open(compiled_module_path, 'r') as compiled_module_file:
        compiled_data = compiled_module_file.read()
    match = kernel_path_pattern.search(compiled_data)
    if match:
        return match.group(0)
    else:
        raise ValueError("Kernel path not found in compiled module")


def profile_individual_kernel(kernel_path):
    os.environ['TORCHINDUCTOR_MAX_AUTOTUNE'] = '1'
    subprocess.run(f"python {kernel_path} -p", shell=True)


def main():
    set_environment_variables()
    run_benchmark_script()
    log_path = "/path/to/performance/log"
    compiled_module_path = analyze_performance_logs(log_path)
    kernel_path = extract_kernel_path(compiled_module_path)
    profile_individual_kernel(kernel_path)
    print("Detailed performance metrics for the identified kernel have been generated.")

if __name__ == "__main__":
    main()