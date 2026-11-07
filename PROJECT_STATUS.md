# PipelineShield – Projektstatus & Lernstand

> **Ziel:** Python 3.11 von Grund auf beherrschen (inkl. aller Fallen) und 100 % prüfungsreif für den schriftlichen IHK-Teil (FIAE nach AO 2020) und das Fachgespräch werden.  
> **Repository:** Öffentliches Entwickler-Portfolio auf GitHub (`PipelineShield`)  
> **Letzter Stand:** Stufe 0 komplett abgeschlossen und in `main.py` lauffähig verifiziert.

---

## 1. Was bisher vollständig umgesetzt wurde (Stufe 0)

### Stufe 0.0: Lokales Setup & DevOps-Basis
* **VS Code Extensions:** Python, Pylance (`python.analysis.typeCheckingMode = "standard"`), Ruff Formatter/Linter.
* **Isolierte Umgebung:** Python 3.12 `.venv` eingerichtet, `$PATH`-Aktivierung mit `source .venv/bin/activate` verstanden und geprüft.
* **Secret-Schutz:** `.gitignore` von Sekunde 0 an scharf geschaltet (`.env`, `.venv/`, `__pycache__/`).
* **Git & GitHub:** Git initialisiert (`branch -M main`), Initial Commit erstellt und mit GitHub (`origin/main`) synchronisiert.

### Stufe 0.1: Variablen & Strikte Type Hints
* Die 4 primitiven Grundtypen von Hand geschrieben: `str`, `int`, `float`, `bool`.
* Moderne formatierte Ausgabe mit f-Strings (`f"[{app_name} v{version}]"`).
* Pylance-Typwächter getestet (Typverletzung `port: int = "achttausend"` sofort erkannt).

### Stufe 0.2: IHK-Mathematik & Operatoren
* **Division:** Echte Division (`/` -> liefert immer `float`) vs. Ganzzahldivision (`//` -> schneidet Nachkommastellen ab, liefert `int`).
* **Modulo (`%`):** Divisionsrest für Zyklen, Audit-Trigger und Lastverteilung (`request_id % 5 == 0`).
* **Kaufmännische Rundung:** Formatierung auf 2 Nachkommastellen mit `:.2f`.
* **Zero-Division-Guard:** Schutzschalter `if active_nodes == 0:` vor Division durch 0 (verhindert fatale `ZeroDivisionError`-Serverabstürze).

### Stufe 0.3: Bedingungen & Logik
* Verzweigungen mit `if`, `elif`, `else` und logischen Operatoren (`and`, `or`, `not`).
* **Truthy & Falsy:** Verstanden, warum `""`, `0`, `[]` und `None` als `False` gewertet werden, während befüllte Werte `True` sind (`if not raw_magic_token:`).

### Stufe 0.4: Eigene Funktionen & Guard Clauses
* `def validate_magic_token(token: str, min_length: int = 16) -> bool`.
* Unterschied zwischen **Parametern** (Funktionskopf) und **Argumenten** (Aufruf).
* **Default-Parameter:** Standardwerte bei fehlenden Argumenten.
* **Guard-Clause-Pattern (Early Return):** Fehlerzustände am Anfang der Funktion sofort mit `return False` abweisen, statt tiefe `if/else`-Verschachtelungen zu bauen.

### Stufe 0.5: Schleifensteuerung
* **Zählschleife `for ... in range(1, max_retries + 1)`:** Grenzen in Python verstehen (`Start` inklusive, `Ende` exklusiv).
* **`break`:** Sofortiger Abbruch der Schleife bei erfolgreicher Verbindung.
* **`for ... else`:** Spezialkonstrukt, das nur auslöst, wenn die Schleife *nicht* durch `break` abgebrochen wurde.
* **Bedingte Schleife `while queue_length > 0`:** Zähler dekrementieren (`queue_length -= 1`), um Endlosschleifen zu verhindern.
* **`continue`:** Nur den aktuellen Durchlauf überspringen (Heartbeat-Ping) und mit der nächsten Runde weitermachen.

### Stufe 0.6: Sammlungen (Listen, Dictionaries & Mutability)
* **Listen (`list[str]`):** 0-basierte Indexierung `[0]`, Zählen von hinten mit `[-1]`, Länge mit `len()`, Anhängen mit `.append()`.
* **Vergleich C# vs. Python:** Python-Listen verhalten sich wie `List<T>` in C# (dynamisch wachsend) und decken das IHK-Pseudocode-Konzept `FELD[...]` vollständig ab.
* **Dictionaries (`dict[str, str]`):** Assoziative Speicher (Key-Value wie JSON).
* **Schutz vor `KeyError`:** Zugriff mit `.get("scope")` liefert sicher `None`, statt bei fehlenden Schlüsseln abzustürzen.
* **Die Mutability-Falle:** Verstanden, dass Zuweisungen wie `b = a` nur Referenzen (Zeiger auf denselben Speicher) kopieren. Echte, unabhängige Duplikate erfordern `.copy()`.

---

## 2. Der nächste Schritt (Hier machen wir im nächsten Python-Chat weiter)

### 👉 Stufe 1: OOP-Fundament (Objektorientierung)
1. **1.1 Konzept-Lektion:** Was ist eine Klasse vs. ein Objekt? (Bauplan vs. Haus).
2. **1.2 Konstruktor:** `__init__` und das magische `self`.
3. **1.3 Kapselung:** Warum Daten schützen? Private Attribute (`_variable`) vs. `@property` und `@setter` mit Validierungswächtern (`ValueError`).

### Zukünftige Stufen:
* **Stufe 2:** Methoden & Architektur (Instanzmethoden mit Rückgabe vs. `None`).
* **Stufe 3:** IHK-Standard-Schleifen & Sammlungen (`List[SecurityFinding]`, Summen-Akkumulatoren, Durchschnittsberechnung mit Pflicht-Wächter).
* **Stufe 4:** Die 5 IHK-Kern-Algorithmen (Live von Hand: Lineare Suche, Min/Max-Extremwertsuche, Dreieckstausch, BubbleSort, SelectionSort, Binäre Suche).
* **Stufe 5:** AP2-Endgame (Vererbung, `abc.ABC` & `@abstractmethod` Interfaces, Polymorphie).

---

## 3. Start-Prompt für den nächsten Python-Chat

Kopiere diesen Text, wenn du später wieder an Python weiterarbeiten möchtest:

```text
Hallo Coach! Wir setzen unser technisches Trainings-Projekt "PipelineShield" in Python 3.11 fort.
Ich habe die Datei PROJECT_STATUS.md im Repository liegen – Stufe 0 (0.0 bis 0.6) ist komplett abgeschlossen, main.py ist lauffähig und formatiert.

Wir steigen genau jetzt bei Stufe 1 ein:
Stufe 1.1: Konzept-Lektion Klasse vs. Objekt (Bauplan vs. Haus), Konstruktor (__init__) und das magische 'self'.

Didaktische Regeln wie bisher:
1. Immer nur GENAU EINE kleine Teilaufgabe pro Nachricht.
2. Kurze Lektion mit Alltags-Vergleich vor neuem Code.
3. Brücke zum IHK-ZPA-Pseudocode & UML-Klassendiagramm (+, -, #, <<interface>>).
4. Modernes Python mit strikten Type Hints.
5. Nach Meilensteinen 2 kurze Verständnisfragen.

Lass uns mit der Konzept-Lektion zu Stufe 1.1 starten!
```
