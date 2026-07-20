import asyncio
import config
from services.system_info import (
    get_cpu_status_raw,
    get_ram_status_raw,
    get_disk_summary_raw
)
from services.database import save_snapshot


def build_alert_message(cpu: float, ram: float):
    messages = []

    if cpu >= config.CPU_THRESHOLD:
        messages.append(f"⚠️ High CPU load: {cpu}% (threshold: {config.CPU_THRESHOLD}%)")

    if ram >= config.RAM_THRESHOLD:
        messages.append(f"⚠️ High RAM load: {ram}% (threshold: {config.RAM_THRESHOLD}%)")

    return messages

async def alert_monitor_loop(bot, admin_id: int):
    while True:
        await asyncio.sleep(config.ALERT_INTERVAL)

        if not config.ALERT_ENABLED:
            continue

        try:
            cpu = get_cpu_status_raw()
            ram = get_ram_status_raw()
            disk_free, disk_total = get_disk_summary_raw()

            save_snapshot(cpu, ram, disk_free, disk_total)

            if config.ALERT_ENABLED:
                for msg in build_alert_message(cpu, ram):
                    await bot.send_message(admin_id, msg)
        except Exception as e:
            print(f"Log: Alert monitor error: {e}")
