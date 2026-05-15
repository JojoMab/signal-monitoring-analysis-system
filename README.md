# Advanced Signal Analyzer

Advanced Signal Analyzer is a compact Python CLI for evaluating signal measurement data from CSV files. The tool reads signal strengths in dBm, calculates statistics, detects dropouts, strong peaks and statistical anomalies, and writes report files for further inspection.

## GitHub Description

Python CLI for technical signal measurement analysis with anomaly detection, report output and optional spectrum plotting.

## Recruiter Snapshot

- Topic: technical measurement data, monitoring and data analysis
- Technology: Python, CSV processing, statistics, CLI, optional visualization with Matplotlib
- Input: frequency and signal strength values from `data/signal_samples.csv`
- Output: text report, anomaly CSV and optional PNG spectrum
- Focus: traceable technical data analysis without complex setup

## Features

- load signal values from CSV files
- calculate average, median, standard deviation, minimum and maximum
- detect dropouts, strong peaks and statistical anomalies
- classify signal quality as `excellent`, `good`, `weak` or `critical`
- generate a text report and anomaly CSV
- optionally generate a PNG spectrum plot

## Quick Start

Run the analysis from the repository root:

```bash
python3 main.py
```

Expected terminal output:

```txt
Signal analysis completed.
Report: output/reports/signal_report.txt
Anomalies CSV: output/reports/anomalies.csv
Signal quality: good
Dropouts detected: 5
Strong peaks detected: 5
Statistical anomalies detected: 2
```

Run the analysis including the plot:

```bash
python3 main.py --plot
```

## Examples

The example outputs are versioned intentionally so recruiters can inspect the result directly on GitHub without running the project locally:

- [Terminal output](examples/terminal_output.txt)

The terminal output shows the standard analysis and the run with `--plot`.

## Installation

The base analysis only uses Python standard libraries. The optional plot requires `matplotlib`:

```bash
python3 -m pip install -r requirements.txt
```

## Analyze Custom Data

```bash
python3 main.py --input path/to/signals.csv
```

The input CSV needs these columns:

```csv
frequency_mhz,signal_strength_dbm
2390,-72
2391,-70
2400,-35
2408,-88
```

## Outputs

Default output:

```txt
output/reports/signal_report.txt
output/reports/anomalies.csv
```

When `--plot` is used, the program also creates:

```txt
output/plots/signal_spectrum.png
```

## Project Structure

```txt
.
├── main.py
├── requirements.txt
├── data/
│   └── signal_samples.csv
├── examples/
│   ├── README.md
│   └── terminal_output.txt
├── signal_analyzer/
│   ├── analysis.py
│   ├── plotter.py
│   ├── reader.py
│   └── report.py
└── output/
    ├── plots/
    └── reports/
```

## Portfolio Relevance

This project demonstrates practical Python skills in CSV processing, statistical analysis, command-line tooling, report generation and simple visualization of technical measurement data. It is a clear portfolio example for IT, monitoring, data analysis and system-oriented roles.
