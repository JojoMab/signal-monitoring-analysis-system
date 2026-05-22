import argparse
from signal_analyzer.reader import load_signal_data
from signal_analyzer.analysis import (
    calculate_statistics,
    find_strongest_signal,
    find_weakest_signal,
    detect_dropouts,
    detect_signal_peaks,
    detect_anomalies,
    classify_signal_quality,
    calculate_health_score,
)
from signal_analyzer.report import create_text_report, export_anomalies_csv


def parse_args():
    parser = argparse.ArgumentParser(description="Advanced Signal Analyzer")
    parser.add_argument("--input", default="data/signal_samples.csv", help="Path to signal CSV file")
    parser.add_argument("--dropout-threshold", type=float, default=-80, help="Threshold for weak signal/dropouts in dBm")
    parser.add_argument("--peak-threshold", type=float, default=-40, help="Threshold for strong signal peaks in dBm")
    parser.add_argument("--sensitivity", type=float, default=2.0, help="Z-score sensitivity for anomaly detection")
    parser.add_argument("--report", default="output/reports/signal_report.txt", help="Output text report path")
    parser.add_argument("--anomalies", default="output/reports/anomalies.csv", help="Output anomalies CSV path")
    parser.add_argument("--plot", action="store_true", help="Generate signal plot")
    parser.add_argument("--plot-output", default="output/plots/signal_strength_by_frequency.png", help="Output plot path")
    return parser.parse_args()


def main():
    args = parse_args()

    if args.plot:
        from signal_analyzer.plotter import require_matplotlib

        try:
            require_matplotlib()
        except RuntimeError as error:
            raise SystemExit(str(error)) from error

    samples = load_signal_data(args.input)
    stats = calculate_statistics(samples)
    strongest = find_strongest_signal(samples)
    weakest = find_weakest_signal(samples)
    dropouts = detect_dropouts(samples, args.dropout_threshold)
    peaks = detect_signal_peaks(samples, args.peak_threshold)
    anomalies = detect_anomalies(samples, args.sensitivity)
    quality = classify_signal_quality(stats)
    health_score = calculate_health_score(stats, dropouts, peaks, anomalies)

    report_path = create_text_report(
        samples=samples,
        stats=stats,
        strongest=strongest,
        weakest=weakest,
        dropouts=dropouts,
        peaks=peaks,
        anomalies=anomalies,
        quality=quality,
        health_score=health_score,
        output_path=args.report,
    )

    anomalies_path = export_anomalies_csv(anomalies, args.anomalies)

    print("Signal analysis completed.")
    print(f"Report: {report_path}")
    print(f"Anomalies CSV: {anomalies_path}")
    print(f"Signal quality: {quality}")
    print(f"Health score: {health_score}/100")
    print(f"Dropouts detected: {len(dropouts)}")
    print(f"Strong peaks detected: {len(peaks)}")
    print(f"Statistical anomalies detected: {len(anomalies)}")

    if args.plot:
        from signal_analyzer.plotter import create_signal_plot

        plot_path = create_signal_plot(samples, args.plot_output)
        print(f"Plot: {plot_path}")


if __name__ == "__main__":
    main()
