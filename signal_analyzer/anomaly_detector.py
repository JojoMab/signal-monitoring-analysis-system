from statistics import mean, pstdev


def detect_anomalies(values, threshold=2.5):
    average = mean(values)
    std_dev = pstdev(values)
    if std_dev == 0:
        return []
    anomalies = []
    for index, value in enumerate(values):
        z_score = (value - average) / std_dev
        if abs(z_score) > threshold:
            anomalies.append({"index": index, "value": value, "z_score": round(z_score, 2)})
    return anomalies
