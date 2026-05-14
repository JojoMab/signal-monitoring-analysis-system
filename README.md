# Advanced Signal Analyzer

Advanced Signal Analyzer ist ein kompaktes Python-CLI zur Auswertung von Signal-Messdaten aus CSV-Dateien. Das Tool liest Signalstärken in dBm, berechnet Kennzahlen, erkennt Aussetzer, starke Peaks und statistische Auffälligkeiten und erstellt daraus Report-Dateien für die weitere Prüfung.

## GitHub-Beschreibung

Python-CLI zur Analyse technischer Signal-Messdaten mit Anomalieerkennung, Report-Ausgabe und optionalem Spektrum-Plot.

## Kurzprofil für Recruiter

- Thema: technische Messdaten, Monitoring und Datenanalyse
- Technologie: Python, CSV-Verarbeitung, Statistik, CLI, optionale Visualisierung mit Matplotlib
- Eingabe: Frequenz- und Signalstärke-Werte aus `data/signal_samples.csv`
- Ausgabe: Textreport, Anomalie-CSV und optionales PNG-Spektrum
- Fokus: nachvollziehbare Analyse technischer Daten ohne komplexe Einrichtung

## Funktionen

- Signalwerte aus CSV-Dateien laden
- Durchschnitt, Median, Standardabweichung, Minimum und Maximum berechnen
- Dropouts, starke Peaks und statistische Anomalien erkennen
- Signalqualität als `excellent`, `good`, `weak` oder `critical` klassifizieren
- Textreport und Anomalie-CSV erzeugen
- optional ein PNG-Diagramm des Signalspektrums erzeugen

## Schnellstart

Analyse aus dem Repository-Root starten:

```bash
python3 main.py
```

Erwartete Terminalausgabe:

```txt
Signal analysis completed.
Report: output/reports/signal_report.txt
Anomalies CSV: output/reports/anomalies.csv
Signal quality: good
Dropouts detected: 5
Strong peaks detected: 5
Statistical anomalies detected: 2
```

Analyse inklusive Diagramm starten:

```bash
python3 main.py --plot
```

## Beispiele im Repository

Die Beispielausgaben sind bewusst versioniert, damit Recruiter das Ergebnis direkt auf GitHub prüfen können, ohne das Projekt lokal auszuführen:

- [Terminal-Mitschnitt](examples/terminal_output.txt)

Der Mitschnitt zeigt die Standardanalyse und die Ausführung mit `--plot`.

## Installation

Die Basisanalyse nutzt nur Python-Standardbibliotheken. Für das optionale Diagramm wird `matplotlib` benötigt:

```bash
python3 -m pip install -r requirements.txt
```

## Eigene Daten analysieren

```bash
python3 main.py --input path/to/signals.csv
```

Die Eingabe-CSV benötigt diese Spalten:

```csv
frequency_mhz,signal_strength_dbm
2390,-72
2391,-70
2400,-35
2408,-88
```

## Ausgaben

Standardausgabe:

```txt
output/reports/signal_report.txt
output/reports/anomalies.csv
```

Bei Nutzung von `--plot` entsteht zusätzlich:

```txt
output/plots/signal_spectrum.png
```

## Projektstruktur

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

## Bewerbungsbezug

Das Projekt zeigt praktische Python-Kenntnisse in CSV-Verarbeitung, statistischer Auswertung, Kommandozeilen-Tools, Report-Erstellung und einfacher Visualisierung technischer Messdaten. Für Rollen mit IT-, Monitoring-, Datenanalyse- oder Systembezug ist es ein gut nachvollziehbares Beispielprojekt.
