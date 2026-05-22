![Python CI](https://github.com/JojoMab/signal-monitoring-analysis-system/actions/workflows/python-ci.yml/badge.svg)

# Signal Monitoring Analysis System

Dieses Bewerberprojekt analysiert synthetische Sensordaten mit Frequenz, Amplitude, Rauschen und Zeitstempel. Es erkennt Anomalien mit Z-Score-Logik, berechnet einen Health Score und erzeugt technische Monitoring-Berichte.

## Bewerbungskontext

Das Projekt passt zu technischer Informatik, Informatik, Data Science und KI-Grundlagen. Es ist relevant für MTU, Rohde & Schwarz, KNDS, Infineon und ASMPT.

## Technologie-Stack

- Python 3.11
- CSV-Daten
- Statistik mit Z-Score
- Health-Score-Logik
- optionale Matplotlib-Plots
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
│   ├── analysis.py
│   ├── reader.py
│   ├── report.py
│   └── plotter.py
├── data/
├── tests/
└── docs/
```

## Schnellstart

```bash
python -m pip install -r requirements.txt
python main.py
```

## Tests ausführen

```bash
python -m pytest tests/ -v
```

## Beispielausgabe

```txt
Signal analysis completed.
Signal quality: good
Health score: 49/100
```

## Hinweis auf synthetische Daten

Alle Daten sind synthetisch und dienen ausschließlich der Demonstration.

Dieses Projekt ist ein Bewerberprojekt und nicht für den produktiven Einsatz vorgesehen.

## Kurzfassung

Dieses Projekt analysiert synthetische Sensorsignale und zeigt Anomalieerkennung, Health-Score-Berechnung und technische Monitoring-Berichte. Es ist als Bewerberprojekt für technische Informatik und datenorientierte Studiengänge aufgebaut.
