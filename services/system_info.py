import psutil

def get_cpu_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    return f"{cpu_usage}%"

def get_ram_status():
    ram = psutil.virtual_memory()

    used_gb = round(ram.used / 1024**3, 2)
    total_gb = round(ram.total / 1024**3, 2)
    percent = ram.percent

    return f"{percent}% ({used_gb} GB / {total_gb} GB)"

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