import psutil

def get_cpu_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    return f"{cpu_usage}%"

def get_cpu_status_raw():
    return psutil.cpu_percent(interval=1)

def get_ram_status():
    ram = psutil.virtual_memory()

    used_gb = ram.used / 1024**3
    total_gb = ram.total / 1024**3
    percent = ram.percent

    return f"{percent}% ({used_gb:.2f} GB / {total_gb:.2f} GB)"

def get_ram_status_raw():
    return psutil.virtual_memory().percent

def get_disk_status():
    disks_data = []
    parts = psutil.disk_partitions(all=False)

    for part in parts:
        letter = part.device

        # skip the disk drives to avoid errors
        try:
            disk = psutil.disk_usage(letter)

            total_gb = round(disk.total / 1024**3, 2)
            free_gb = round(disk.free / 1024**3, 2)
            percent = disk.percent

            disks_data.append({
                "name": letter.strip("\\"),
                "percent": percent,
                "free": free_gb,
                "total": total_gb
            })
        except PermissionError:
            continue
    return disks_data

def get_disk_summary_raw() -> tuple[float, float]:
    total_free = 0.0
    total_size = 0.0
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.device)
            total_free += usage.free
            total_size += usage.total
        except PermissionError:
            continue
    return total_free / (1024 ** 3), total_size / (1024 ** 3)

def get_top_processes(limit):
    process_list = []

    for proc in psutil.process_iter(attrs=["name","memory_info"]):
        try:
            info = proc.info
            name = info["name"]
            memory_info = info["memory_info"]

            if memory_info:
                memory_mb = memory_info.rss / (1024**2)

                process_list.append({
                    "name": name,
                    "memory": memory_mb
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    sorted_list = sorted(process_list, key=lambda k: k["memory"], reverse=True)

    return sorted_list[:limit]