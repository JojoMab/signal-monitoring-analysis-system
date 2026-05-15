# Data Dictionary

Die Datei `data/signal_samples.csv` enthaelt synthetische technische Messwerte fuer das Bewerberprojekt.

| Spalte | Typ | Beschreibung | Beispiel |
| --- | --- | --- | --- |
| `frequency_mhz` | Zahl | Gemessene Frequenz in Megahertz | `2400` |
| `signal_strength_dbm` | Zahl | Signalstaerke in dBm | `-35` |

## Validierung

Die Anwendung prueft:

- ob die erforderlichen Spalten vorhanden sind
- ob die Datei mindestens einen Datenwert enthaelt
- ob Frequenz und Signalstaerke als Zahlen gelesen werden koennen

## Hinweis

Die Daten sind synthetisch. Sie bilden kein echtes Unternehmenssystem und keine echten Messreihen eines Herstellers ab.
