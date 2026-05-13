# Advanced Signal Analyzer

Advanced Signal Analyzer is a small Python CLI for analyzing frequency-domain signal measurements from CSV files. It reads signal strength values in dBm, calculates statistics, detects weak dropouts, strong peaks and z-score based anomalies, then writes report files for further inspection.

## Features

- Load signal samples from CSV
- Calculate average, median, standard deviation, minimum and maximum
- Detect dropouts, strong peaks and statistical anomalies
- Classify signal quality as `excellent`, `good`, `weak` or `critical`
- Generate a text report and anomaly CSV
- Optionally generate a PNG signal spectrum plot

## Project Structure

```txt
.
├── main.py
├── requirements.txt
├── data/
│   └── signal_samples.csv
├── signal_analyzer/
│   ├── analysis.py
│   ├── plotter.py
│   ├── reader.py
│   └── report.py
└── output/
    ├── plots/
    └── reports/
```

## Installation

```bash
python3 -m pip install -r requirements.txt
```

`matplotlib` is only needed when plot generation is enabled with `--plot`.

## Usage

Run the default analysis from the repository root:

```bash
python3 main.py
```

Generate the report, anomaly CSV and signal spectrum plot:

```bash
python3 main.py --plot
```

Analyze a custom input file:

```bash
python3 main.py --input path/to/signals.csv
```

## Input Format

The input CSV needs these columns:

```csv
frequency_mhz,signal_strength_dbm
2390,-72
2391,-70
2400,-35
2408,-88
```

## Output

By default, the application writes:

```txt
output/reports/signal_report.txt
output/reports/anomalies.csv
```

When `--plot` is used, it also writes:

```txt
output/plots/signal_spectrum.png
```

## Portfolio Relevance

This project demonstrates practical Python skills for CSV processing, statistical analysis, configurable command-line tooling, report generation and basic visualization of technical measurement data.
