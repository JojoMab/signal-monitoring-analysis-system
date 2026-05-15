# Advanced Signal Analyzer

Python-Projekt zur Analyse technischer Sensordaten mit Anomalieerkennung, Health Score, Report-Erstellung und Bezug zu Digital Maintenance im Luftfahrt- und Industrieumfeld.

## Kurzprofil fuer Recruiter

Dieses Bewerberprojekt zeigt, wie technische Messdaten aus CSV-Dateien eingelesen, statistisch ausgewertet und in einem nachvollziehbaren Report zusammengefasst werden koennen. Die Anwendung erkennt Signalabbrueche, starke Peaks und statistische Auffaelligkeiten, berechnet einen einfachen Health Score und erzeugt Ergebnisdateien fuer die weitere Pruefung.

Das Projekt ist bewusst auf Niveau eines Bewerberprojekts fuer ein duales Studium gehalten: modular, testbar, dokumentiert und mit synthetischen Beispieldaten.

## Bewerbungsbezug: MTU Aero Engines

Dieses Projekt passt besonders zu einem dualen Informatikstudium bei MTU Aero Engines, da es technische Messdaten, Monitoring, Anomalieerkennung und digitale Wartungsprozesse verbindet. Die Anwendung liest Sensordaten aus CSV-Dateien ein, erkennt Auffaelligkeiten und erstellt automatisch Reports. Damit zeigt das Projekt Grundlagen, die fuer Digital Maintenance, Engineering-Systeme, technische Informatik und datengetriebene Prozessverbesserung in der Luftfahrt relevant sind.

## Weitere passende Zielunternehmen

| Unternehmen / Bereich | Warum das Projekt passt |
| --- | --- |
| Rohde & Schwarz | Messdaten, Monitoring, technische Auswertung |
| KNDS | technische Informatik, Sensorik, Diagnoseprozesse |
| Siemens Energy | Industrieprozesse, Monitoring, datenbasierte Wartung |
| Infineon | technische Daten, Software Engineering, Statistik |
| ASMPT | Scientific Computing, Datenaufbereitung, Visualisierung |
| Truma | technische Produkte, Sensordaten, Prozessanalyse |

## Tech Stack

- Python 3
- CSV-Verarbeitung mit Standardbibliothek
- Statistik mit Standardbibliothek
- Optionale Visualisierung mit matplotlib
- Unit Tests mit unittest
- GitHub Actions fuer automatische Tests

## Funktionen

- CSV-Sensordaten einlesen
- Eingabedaten validieren
- Grundstatistiken berechnen
- Signalabbrueche anhand eines Schwellwerts erkennen
- Starke Signal-Peaks anhand eines Schwellwerts erkennen
- Statistische Anomalien mit Z-Score erkennen
- Anomalietypen als `dropout` oder `strong_peak` einordnen
- Signalqualitaet klassifizieren
- Einfachen Health Score berechnen
- Textreport und Anomalie-CSV erzeugen
- Optionalen PNG-Plot generieren

## Projektstruktur

```txt
advanced-signal-analyzer/
├── main.py
├── requirements.txt
├── data/
│   └── signal_samples.csv
├── signal_analyzer/
│   ├── analysis.py
│   ├── plotter.py
│   ├── reader.py
│   └── report.py
├── tests/
│   ├── test_analysis.py
│   └── test_reader.py
├── docs/
│   ├── application_fit.md
│   ├── data_dictionary.md
│   ├── recruiter_summary_de.md
│   └── screenshots/
├── examples/
│   └── terminal_output.txt
└── .github/
    └── workflows/
        └── python-ci.yml
```

## Eingabedaten

Die Eingabedatei ist eine CSV-Datei mit diesen Spalten:

```csv
frequency_mhz,signal_strength_dbm
2390,-72
2391,-70
2400,-35
2408,-88
```

Die Beispieldaten in `data/signal_samples.csv` sind synthetisch und dienen nur zur Demonstration.

## Schnellstart

```bash
python3 -m pip install -r requirements.txt
python3 main.py
```

Analyse mit Plot:

```bash
python3 main.py --plot
```

Eigene Datei analysieren:

```bash
python3 main.py --input path/to/signals.csv
```

Tests ausfuehren:

```bash
python3 -m unittest discover -s tests
```

## CLI-Optionen

| Option | Standard | Beschreibung |
| --- | --- | --- |
| `--input` | `data/signal_samples.csv` | Pfad zur Eingabe-CSV |
| `--dropout-threshold` | `-80` | Schwellwert fuer schwache Signale |
| `--peak-threshold` | `-40` | Schwellwert fuer starke Peaks |
| `--sensitivity` | `2.0` | Z-Score-Sensitivitaet |
| `--report` | `output/reports/signal_report.txt` | Pfad fuer Textreport |
| `--anomalies` | `output/reports/anomalies.csv` | Pfad fuer Anomalie-CSV |
| `--plot` | deaktiviert | Erzeugt einen PNG-Plot |
| `--plot-output` | `output/plots/signal_spectrum.png` | Pfad fuer den Plot |

## Beispielausgabe

```txt
Signal analysis completed.
Report: output/reports/signal_report.txt
Anomalies CSV: output/reports/anomalies.csv
Signal quality: good
Health score: 49/100
Dropouts detected: 5
Strong peaks detected: 5
Statistical anomalies detected: 2
```

Eine versionierte Beispielausgabe liegt unter `examples/terminal_output.txt`.

## Was ich mit dem Projekt zeige

- Technische Datenanalyse mit Python
- Saubere Trennung von Einlesen, Analyse, Reporting und Visualisierung
- Einfache Fehler- und Auffaelligkeitserkennung
- Report-Erstellung fuer technische Entscheidungen
- Grundlagen von Digital Maintenance und Monitoring
- Tests und CI als Basis fuer nachvollziehbare Softwareentwicklung

## Level-Einschaetzung

Level 2: bewerberfaehig. Das Projekt hat eine klare technische Problemstellung, modulare Struktur, Tests, CI, Beispielausgaben und einen Bewerbungsbezug. Fuer Level 3 waeren zusaetzlich umfangreichere synthetische Sensordaten, mehrere Reports und eine kleine ML-Erweiterung sinnvoll.

## Hinweis

Dies ist kein echtes Unternehmenssystem und verwendet keine echten Unternehmensdaten. Alle Daten sind synthetisch und dienen als Bewerberprojekt fuer duale Studiengaenge in Informatik, Wirtschaftsinformatik, Data Science und technischer Informatik.

## English Summary

Advanced Signal Analyzer is a small Python CLI for technical signal monitoring. It loads synthetic sensor data from CSV files, calculates statistics, detects dropouts, strong peaks and z-score anomalies, computes a simple health score and creates reports. The project is designed as an applicant portfolio project for dual study programs in computer science, business information systems and data-oriented technical fields.

## Autor

Johannes Maboudou
