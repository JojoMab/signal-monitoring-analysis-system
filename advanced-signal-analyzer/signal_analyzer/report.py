import csv
import os
from datetime import datetime
from signal_analyzer.reader import SignalSample


def create_text_report(
    samples: list[SignalSample],
    stats: dict,
    strongest: SignalSample,
    weakest: SignalSample,
    dropouts: list[SignalSample],
    peaks: list[SignalSample],
    anomalies: list[dict],
    quality: str,
    output_path: str
) -> str:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("Advanced Signal Analysis Report\n")
        file.write("===============================\n\n")
        file.write(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Signal quality: {quality}\n\n")

        file.write("Statistics\n")
        file.write("----------\n")
        for key, value in stats.items():
            file.write(f"{key}: {value}\n")

        file.write("\nStrongest Signal\n")
        file.write("----------------\n")
        file.write(f"{strongest.frequency_mhz} MHz -> {strongest.signal_strength_dbm} dBm\n")

        file.write("\nWeakest Signal\n")
        file.write("--------------\n")
        file.write(f"{weakest.frequency_mhz} MHz -> {weakest.signal_strength_dbm} dBm\n")

        file.write("\nDetected Dropouts\n")
        file.write("-----------------\n")
        if dropouts:
            for sample in dropouts:
                file.write(f"{sample.frequency_mhz} MHz -> {sample.signal_strength_dbm} dBm\n")
        else:
            file.write("No dropouts detected.\n")

        file.write("\nDetected Strong Peaks\n")
        file.write("---------------------\n")
        if peaks:
            for sample in peaks:
                file.write(f"{sample.frequency_mhz} MHz -> {sample.signal_strength_dbm} dBm\n")
        else:
            file.write("No strong peaks detected.\n")

        file.write("\nStatistical Anomalies\n")
        file.write("---------------------\n")
        if anomalies:
            for anomaly in anomalies:
                file.write(
                    f"{anomaly['frequency_mhz']} MHz -> "
                    f"{anomaly['signal_strength_dbm']} dBm "
                    f"(z-score: {anomaly['z_score']})\n"
                )
        else:
            file.write("No statistical anomalies detected.\n")

    return output_path


def export_anomalies_csv(anomalies: list[dict], output_path: str) -> str:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["frequency_mhz", "signal_strength_dbm", "z_score"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(anomalies)

    return output_path
