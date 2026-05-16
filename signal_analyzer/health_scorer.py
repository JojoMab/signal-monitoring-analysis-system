def calculate_health_score(sample_count, anomaly_count, stability):
    if sample_count == 0:
        return 0
    anomaly_rate = anomaly_count / sample_count
    score = 100 - anomaly_rate * 100 - max(0, 1 - stability) * 30
    return max(0, min(100, round(score)))


def explain_health_score(score):
    if score >= 90:
        return "Normal"
    if score >= 70:
        return "Leichte Auffälligkeiten"
    if score >= 50:
        return "Erhöhte Anomalierate"
    return "Kritisch"
