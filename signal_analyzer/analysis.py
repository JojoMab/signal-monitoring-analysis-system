from statistics import mean, median, pstdev
from signal_analyzer.reader import SignalSample


def calculate_statistics(samples: list[SignalSample]) -> dict:
    values = [sample.signal_strength_dbm for sample in samples]

    return {
        "sample_count": len(samples),
        "average_dbm": round(mean(values), 2),
        "median_dbm": round(median(values), 2),
        "std_dev_dbm": round(pstdev(values), 2),
        "min_dbm": round(min(values), 2),
        "max_dbm": round(max(values), 2),
        "noise_floor_dbm": round(median(values), 2),
    }


def find_strongest_signal(samples: list[SignalSample]) -> SignalSample:
    return max(samples, key=lambda sample: sample.signal_strength_dbm)


def find_weakest_signal(samples: list[SignalSample]) -> SignalSample:
    return min(samples, key=lambda sample: sample.signal_strength_dbm)


def detect_dropouts(samples: list[SignalSample], threshold_dbm: float) -> list[SignalSample]:
    return [sample for sample in samples if sample.signal_strength_dbm <= threshold_dbm]


def detect_signal_peaks(samples: list[SignalSample], threshold_dbm: float) -> list[SignalSample]:
    return [sample for sample in samples if sample.signal_strength_dbm >= threshold_dbm]


def detect_anomalies(samples: list[SignalSample], sensitivity: float = 2.0) -> list[dict]:
    stats = calculate_statistics(samples)
    avg = stats["average_dbm"]
    std = stats["std_dev_dbm"]

    anomalies = []
    for sample in samples:
        if std == 0:
            continue

        z_score = (sample.signal_strength_dbm - avg) / std
        if abs(z_score) >= sensitivity:
            anomalies.append({
                "frequency_mhz": sample.frequency_mhz,
                "signal_strength_dbm": sample.signal_strength_dbm,
                "z_score": round(z_score, 2),
                "anomaly_type": classify_anomaly_type(sample.signal_strength_dbm, avg),
            })

    return anomalies


def classify_anomaly_type(signal_strength_dbm: float, average_dbm: float) -> str:
    if signal_strength_dbm >= average_dbm:
        return "strong_peak"
    return "dropout"


def classify_signal_quality(stats: dict) -> str:
    avg = stats["average_dbm"]

    if avg >= -50:
        return "excellent"
    if avg >= -65:
        return "good"
    if avg >= -80:
        return "weak"
    return "critical"


def calculate_health_score(
    stats: dict,
    dropouts: list[SignalSample],
    peaks: list[SignalSample],
    anomalies: list[dict],
) -> int:
    score = 100
    score -= len(dropouts) * 6
    score -= len(anomalies) * 4
    score -= max(0, stats["std_dev_dbm"] - 8) * 2

    if stats["average_dbm"] < -70:
        score -= 10
    if peaks and len(peaks) > max(1, stats["sample_count"] * 0.2):
        score -= 5

    return max(0, min(100, round(score)))
