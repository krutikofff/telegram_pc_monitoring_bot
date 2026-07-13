import psutil

def get_cpu_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    return f"📊 CPU usage: {cpu_usage}%"

def get_ram_status():
    ram = psutil.virtual_memory()

    used_gb = round(ram.used / 1024**3, 2)
    total_gb = round(ram.total / 1024**3, 2)
    percent = ram.percent

    return f"💾 RAM usage: {percent}% ({used_gb} GB / {total_gb} GB)"