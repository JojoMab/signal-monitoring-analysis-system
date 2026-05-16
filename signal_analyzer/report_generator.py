def create_monitoring_report(score, anomalies):
    lines = [
        "Signal Monitoring Bericht",
        "=========================",
        "",
        f"Health Score: {score}",
        f"Anomalien: {len(anomalies)}",
    ]
    for anomaly in anomalies:
        lines.append(f"Index {anomaly['index']}: Wert {anomaly['value']} Z-Score {anomaly['z_score']}")
    return "
".join(lines)
