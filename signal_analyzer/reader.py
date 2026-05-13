import csv
from dataclasses import dataclass


@dataclass
class SignalSample:
    frequency_mhz: float
    signal_strength_dbm: float


def load_signal_data(filepath: str) -> list[SignalSample]:
    samples = []

    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            samples.append(SignalSample(
                frequency_mhz=float(row["frequency_mhz"]),
                signal_strength_dbm=float(row["signal_strength_dbm"])
            ))

    if not samples:
        raise ValueError("No signal data found in input file.")

    return samples
