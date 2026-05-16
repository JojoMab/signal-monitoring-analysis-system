from signal_analyzer.anomaly_detector import detect_anomalies
from signal_analyzer.health_scorer import calculate_health_score, explain_health_score


def test_detect_anomalies_with_z_score():
    values = [1, 1, 1, 1, 10, 1, 1]
    assert len(detect_anomalies(values, threshold=2.0)) == 1


def test_health_score_range():
    score = calculate_health_score(10, 2, 0.8)
    assert 0 <= score <= 100


def test_health_score_explanation():
    assert explain_health_score(95) == "Normal"
    assert explain_health_score(45) == "Kritisch"
