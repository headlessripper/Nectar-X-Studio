import platform
import psutil, shutil, subprocess, os, re

def get_llm_hardware_recommendation():
    info = {}
    info['cpu_name'] = platform.processor()
    info['cpu_cores'] = psutil.cpu_count(logical=False)
    info['cpu_threads'] = psutil.cpu_count(logical=True)
    total_ram_gb = round(psutil.virtual_memory().total / 1073741824, 2)
    info['total_ram_gb'] = total_ram_gb
    info['gpu_name'] = 'Unknown'
    info['gpu_memory_gb'] = 0
    if shutil.which('nvidia-smi'):
        try:
            result = subprocess.run(['nvidia-smi', '--query-gpu=name,memory.total', '--format=csv,noheader,nounits'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, check=True)
            gpu_info = result.stdout.strip().split('\n')[0]
            if gpu_info:
                gpu_name, gpu_mem = map(str.strip, gpu_info.split(','))
                info['gpu_name'] = gpu_name
                info['gpu_memory_gb'] = round(int(gpu_mem) / 1024, 2)
        except subprocess.CalledProcessError:
            info['gpu_name'] = 'nvidia-smi failed'
    else:
        if shutil.which('rocm-smi'):
            try:
                result = subprocess.run(['rocm-smi', '--showproductname', '--showmeminfo', 'vram'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, check=True)
                output = result.stdout
                name_match = re.search('Card\\s*\\d+\\s*:\\s*(.*)', output)
                mem_match = re.search('Total Memory.*?(\\d+)\\s*MiB', output)
                if name_match:
                    info['gpu_name'] = name_match.group(1).strip()
                if mem_match:
                    info['gpu_memory_gb'] = round(int(mem_match.group(1)) / 1024, 2)
            except subprocess.CalledProcessError:
                info['gpu_name'] = 'rocm-smi failed'
        else:
            if os.name == 'nt' and shutil.which('dxdiag'):
                try:
                    dxdiag_file = 'dxinfo.txt'
                    subprocess.run(['dxdiag', '/t', dxdiag_file], check=True)
                    with open(dxdiag_file, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    gpu_lines = re.findall('Card name:\\s*(.+)', content)
                    if gpu_lines:
                        gpu_name = gpu_lines[0].strip()
                        info['gpu_name'] = gpu_name
                        info['gpu_memory_gb'] = 1
                except Exception:
                    info['gpu_name'] = 'Intel GPU detection failed'
    ram = info['total_ram_gb']
    gpu_vram = info['gpu_memory_gb']
    recommendation = []
    if ram < 4:
        recommendation.append('Not recommended to run LLMs locally (too little RAM).')
    else: 
        if 4 <= ram < 8:
            recommendation.append('Run small quantized models like 7B (Q4_0 or Q5_0) using CPU.')
        else: 
            if 8 <= ram < 16:
                recommendation.append('Run 7B models comfortably (Q4_0 to Q6_K).')
            else: 
                if 16 <= ram < 32:
                    recommendation.append('Run 13B (Q4/Q5), 7B full precision possible.')
                else:
                    if ram >= 32:
                        recommendation.append('Run 13B easily, 33B quantized models possible (Q4).')
    if gpu_vram >= 12:
        recommendation.append('Run 13B or even 33B models in GGUF on GPU.')
    else: 
        if 6 <= gpu_vram < 12:
            recommendation.append('Run 7B GGUF models on GPU (Q4 or Q5 quantization).')
        else: 
            if 0 < gpu_vram < 6:
                recommendation.append('Very limited GPU use CPU instead.')
            else: 
                recommendation.append('No GPU acceleration available; CPU-only inference recommended.')
    rec_text = '                '.join(recommendation)
    summary = f"\n    LLM Recommendation: With {ram} GB RAM and GPU: {info['gpu_name']} ({gpu_vram} GB VRAM)\n [ {rec_text} ]\n    "
    return summary
