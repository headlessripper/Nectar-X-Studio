# hooks/llama_cpp.py
from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files, get_package_paths
import os
import glob

# Collect DLLs and binaries
binaries = collect_dynamic_libs('llama_cpp')

# Windows-specific: bundle llama.dll
if os.name == 'nt':
    if package_path := get_package_paths('llama_cpp'):
        lib_dir = os.path.join(package_path[0], 'llama_cpp', 'lib')
        if os.path.exists(lib_dir):
            dll_pattern = os.path.join(lib_dir, '*.dll')
            for dll in glob.glob(dll_pattern):
                binaries.append((dll, 'llama_cpp/lib'))

# Collect data files (models, configs)
datas = collect_data_files('llama_cpp')
