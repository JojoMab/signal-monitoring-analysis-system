import unittest

from signal_analyzer.analysis import (
    calculate_health_score,
    calculate_statistics,
    classify_signal_quality,
    detect_anomalies,
    detect_dropouts,
    detect_signal_peaks,
)
from signal_analyzer.reader import SignalSample


class AnalysisTest(unittest.TestCase):
    def sample_signals(self):
        return [
            SignalSample(2398, -63),
            SignalSample(2399, -62),
            SignalSample(2400, -35),
            SignalSample(2401, -32),
            SignalSample(2402, -30),
            SignalSample(2407, -85),
            SignalSample(2408, -88),
            SignalSample(2410, -63),
            SignalSample(2411, -60),
            SignalSample(2421, -82),
        ]

    def test_calculate_statistics_contains_monitoring_values(self):
        stats = calculate_statistics(self.sample_signals())

        self.assertEqual(stats["sample_count"], 10)
        self.assertEqual(stats["min_dbm"], -88)
        self.assertEqual(stats["max_dbm"], -30)
        self.assertEqual(stats["noise_floor_dbm"], stats["median_dbm"])

    def test_threshold_detection_finds_dropouts_and_peaks(self):
        samples = self.sample_signals()

        dropouts = detect_dropouts(samples, -80)
        peaks = detect_signal_peaks(samples, -40)

        self.assertEqual([sample.frequency_mhz for sample in dropouts], [2407, 2408, 2421])
        self.assertEqual([sample.frequency_mhz for sample in peaks], [2400, 2401, 2402])

    def test_detect_anomalies_adds_anomaly_type(self):
        anomalies = detect_anomalies(self.sample_signals(), sensitivity=1.0)

        self.assertTrue(anomalies)
        self.assertLessEqual(
            {anomaly["anomaly_type"] for anomaly in anomalies},
            {"dropout", "strong_peak"},
        )

    def test_quality_and_health_score_are_recruiter_readable(self):
        samples = self.sample_signals()
        stats = calculate_statistics(samples)
        dropouts = detect_dropouts(samples, -80)
        peaks = detect_signal_peaks(samples, -40)
        anomalies = detect_anomalies(samples, sensitivity=1.0)

        self.assertEqual(classify_signal_quality(stats), "good")
        self.assertGreaterEqual(calculate_health_score(stats, dropouts, peaks, anomalies), 0)
        self.assertLessEqual(calculate_health_score(stats, dropouts, peaks, anomalies), 100)


if __name__ == "__main__":
    unittest.main()
