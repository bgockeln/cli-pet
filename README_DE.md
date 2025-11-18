# CLI Pet
![Python](https://img.shields.io/badge/python-3.12-blue)
![Status](https://img.shields.io/badge/status-finished-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

Ein kleines CLI-Haustier, geschrieben in Python. Dieses Projekt entstand als erster Versuch mit objektorientierter Programmierung (OOP).

## Funktionen

- Gib deinem virtuellen Haustier einen Namen
- Einfache OOP-Struktur mit einer eigenen `Pet`-Klasse
- Spielen, füttern und Wasser geben
- ASCII-Art-Begleiter
- Einfaches Statussystem: Stimmung, Hunger, Durst und Alter

## Aufbau

Das Projekt besteht aus zwei Dateien:

- **main.py** – Entält die Benutzerinteraktion, das Menü und den main loop.
- **pet.py** – Definiert die `Pet`-Klasse und ihr Verhalten.

Das CLI-Haustier besitzt drei Werte:

- **Stimmung** (0–100)
- **Hunger** (100–0)
- **Durst** (100–0)

Durch Interaktionen ändern sich diese Werte.

## Beispiel:

```
Name your pet: Biscuit
(\_/)
(•_•)
/>🍪
```
