# Signal Monitoring Analysis System

![Python CI](https://github.com/JojoMab/signal-monitoring-analysis-system/actions/workflows/python-ci.yml/badge.svg)

Dieses Bewerberprojekt analysiert synthetische Sensordaten mit Frequenz, Amplitude, Rauschen und Zeitstempel. Es erkennt Anomalien mit Z-Score-Logik, berechnet einen Health Score und erzeugt technische Monitoring-Berichte.

## Bewerbungskontext

Das Projekt passt zu technischer Informatik, Informatik, Data Science und KI-Grundlagen. Es ist relevant für MTU, Rohde & Schwarz, KNDS, Infineon und ASMPT.

## Tech Stack

- Python 3.11
- CSV-Daten
- Statistik mit Z-Score
- Health-Score-Logik
- Unit Tests
- GitHub Actions

## Funktionen

- Sensordaten einlesen
- Anomalien erkennen
- Health Score berechnen
- Monitoring-Bericht erzeugen
- technische Daten verständlich dokumentieren

## Health Score

- 90–100: Normal
- 70–89: Leichte Auffälligkeiten
- 50–69: Erhöhte Anomalierate
- 0–49: Kritisch

## Projektstruktur

```txt
signal-monitoring-analysis-system/
├── main.py
├── signal_analyzer/
│   ├── anomaly_detector.py
│   ├── health_scorer.py
│   └── report_generator.py
├── data/
├── tests/
└── docs/
```

## Schnellstart

```bash
python main.py
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Beispielausgabe

```txt
Signal analysis completed.
Signal quality: good
Health score: 49/100
```

## Hinweis auf synthetische Daten

Alle Messwerte sind synthetisch. Das Projekt simuliert eine technische Datenanalyse und verwendet keine echten Unternehmensdaten.

## English Summary

This project analyzes synthetic sensor signals and demonstrates anomaly detection, health scoring and monitoring reports. It is designed as an applicant portfolio project for technical computer science and data-oriented study programs.
