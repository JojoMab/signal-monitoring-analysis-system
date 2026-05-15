import csv
from dataclasses import dataclass
from typing import Optional


@dataclass
class SignalSample:
    frequency_mhz: float
    signal_strength_dbm: float


REQUIRED_COLUMNS = {"frequency_mhz", "signal_strength_dbm"}


def load_signal_data(filepath: str) -> list[SignalSample]:
    samples = []

    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        validate_columns(reader.fieldnames)

        for line_number, row in enumerate(reader, start=2):
            try:
                samples.append(SignalSample(
                    frequency_mhz=float(row["frequency_mhz"]),
                    signal_strength_dbm=float(row["signal_strength_dbm"])
                ))
            except ValueError as exc:
                raise ValueError(f"Invalid numeric value in line {line_number}.") from exc

    if not samples:
        raise ValueError("No signal data found in input file.")

    return samples


def validate_columns(fieldnames: Optional[list[str]]) -> None:
    if fieldnames is None:
        raise ValueError("Input file must contain a CSV header.")

    missing_columns = REQUIRED_COLUMNS.difference(fieldnames)
    if missing_columns:
        formatted_columns = ", ".join(sorted(missing_columns))
        raise ValueError(f"Missing required CSV column(s): {formatted_columns}.")
