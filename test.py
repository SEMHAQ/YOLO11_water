import os
import subprocess

# 检查conda环境中的CUDA
print("=== Conda环境检查 ===")
result = subprocess.run(['conda', 'list', 'cudatoolkit'], capture_output=True, text=True)
print("Conda中的CUDA工具包:")
print(result.stdout)

# 检查conda的Library目录
conda_env = os.environ.get('CONDA_PREFIX')
if conda_env:
    print(f"\nConda环境路径: {conda_env}")
    cuda_paths = [
        os.path.join(conda_env, 'Library', 'bin'),
        os.path.join(conda_env, 'bin')
    ]
    for path in cuda_paths:
        if os.path.exists(path):
            print(f"检查路径: {path}")
            nvcc_path = os.path.join(path, 'nvcc.exe')
            if os.path.exists(nvcc_path):
                print(f"找到nvcc: {nvcc_path}")