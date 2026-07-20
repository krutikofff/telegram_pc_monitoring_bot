from datetime import datetime

def forecast_disk_full(snapshots: list[tuple[str, float]]) -> float | None:
    if len(snapshots) < 2:
        return None

    first_time = datetime.fromisoformat(snapshots[0][0])

    xs, ys = [], []
    for ts, free_gb in snapshots:
        days_passed = (datetime.fromisoformat(ts) - first_time).total_seconds() / 86400
        xs.append(days_passed)
        ys.append(free_gb)

    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n

    numerator = sum((xs[i] - mean_x) * (ys[i] - mean_y) for i in range(n))
    denominator = sum((xs[i] - mean_x) ** 2 for i in range(n))

    if denominator == 0:
        return None

    slope = numerator / denominator

    if slope >= 0:
        return None

    days_left = ys[-1] / abs(slope)
    return round(days_left, 1)

def format_forecast_text(days_left: float | None) -> str:
    if days_left is None:
        return "📊 Not enough data yet for a forecast."
    return f"📉 Disk forecast: ~{days_left} days left at current rate"