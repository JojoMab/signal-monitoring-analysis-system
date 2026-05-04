# Advanced Signal Analyzer

Advanced Signal Analyzer is a small Python CLI for analyzing frequency-domain signal measurements from CSV files. It reads signal strength values in dBm, calculates descriptive statistics, detects weak dropouts, strong peaks and z-score based anomalies, then writes report files for further inspection.

The project is structured as a portfolio-style example for measurement technology, diagnostics, monitoring and technical data analysis workflows.

## Features

- Load signal samples from CSV
- Calculate sample count, average, median, population standard deviation, minimum and maximum
- Estimate the noise floor from the median signal strength
- Find the strongest and weakest measured signal
- Detect dropouts with a configurable dBm threshold
- Detect strong signal peaks with a configurable dBm threshold
- Detect statistical anomalies with configurable z-score sensitivity
- Classify signal quality as `excellent`, `good`, `weak` or `critical`
- Generate a plain-text analysis report
- Export detected anomalies as CSV
- Optionally generate a PNG signal spectrum plot

## Project Structure

```txt
advanced-signal-analyzer/
├── .gitignore
├── main.py
├── requirements.txt
├── data/
│   └── signal_samples.csv
├── signal_analyzer/
│   ├── __init__.py
│   ├── analysis.py
│   ├── plotter.py
│   ├── reader.py
│   └── report.py
├── output/
│   ├── plots/
│   │   └── .gitkeep
│   └── reports/
│       └── .gitkeep
└── docs/
    └── screenshots/
        └── README.md
```

## Input Format

The input file must be a CSV with these columns:

- `frequency_mhz`
- `signal_strength_dbm`

Example:

```csv
frequency_mhz,signal_strength_dbm
2390,-72
2391,-70
2400,-35
2408,-88
```

The default input file is `data/signal_samples.csv`.

## Installation

Create and activate a virtual environment if desired, then install the required dependency:

```bash
python3 -m pip install -r requirements.txt
```

`matplotlib` is required only when plot generation is enabled with `--plot`.

## Usage

Run the default analysis:

```bash
python3 main.py
```

Generate the analysis report, anomaly CSV and signal spectrum plot:

```bash
python3 main.py --plot
```

Analyze a custom input file:

```bash
python3 main.py --input path/to/signals.csv
```

Use custom detection thresholds:

```bash
python3 main.py --dropout-threshold -82 --peak-threshold -38 --sensitivity 1.8
```

Write outputs to custom paths:

```bash
python3 main.py \
  --report output/reports/custom_report.txt \
  --anomalies output/reports/custom_anomalies.csv \
  --plot \
  --plot-output output/plots/custom_spectrum.png
```

## CLI Options

| Option | Default | Description |
| --- | --- | --- |
| `--input` | `data/signal_samples.csv` | Path to the input CSV file |
| `--dropout-threshold` | `-80` | Signals at or below this dBm value are treated as dropouts |
| `--peak-threshold` | `-40` | Signals at or above this dBm value are treated as strong peaks |
| `--sensitivity` | `2.0` | Absolute z-score threshold for anomaly detection |
| `--report` | `output/reports/signal_report.txt` | Path for the generated text report |
| `--anomalies` | `output/reports/anomalies.csv` | Path for the anomaly CSV export |
| `--plot` | disabled | Enables PNG plot generation |
| `--plot-output` | `output/plots/signal_spectrum.png` | Path for the generated plot |

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

The terminal output summarizes the generated file paths, signal quality and the number of detected dropouts, strong peaks and statistical anomalies.

Generated files in `output/reports/` and `output/plots/` are ignored by Git. The directories are kept in the repository with `.gitkeep` files.

## Module Overview

- `main.py` parses CLI arguments and coordinates the analysis workflow.
- `signal_analyzer/reader.py` loads CSV rows into `SignalSample` objects.
- `signal_analyzer/analysis.py` contains statistics, threshold detection, anomaly detection and quality classification.
- `signal_analyzer/report.py` writes the text report and anomaly CSV.
- `signal_analyzer/plotter.py` creates the optional PNG plot using matplotlib with a non-interactive backend.

## Portfolio Relevance

This project demonstrates practical Python skills for:

- CSV-based measurement data processing
- statistical signal evaluation
- configurable command-line tooling
- modular application structure
- report and artifact generation
- basic visualization of technical data

## Author

Johannes Maboudou
