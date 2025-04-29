## self-Attribut
- Das self-Attribut bezieht sich auf das Objekt, das verwendet wird
- z.B. bei der init-Funktion (Konstruktor), auf das zu erstellende Objekt

## Magic Methoden (Dunder)
Beispiele
- `__init__`: Konstruktor, der beim Instanziieren des Objektes von einer Klasse aufgerufen wird
- `__name__ == "__main__"`: `__name__` ist eine spezielle Variable, wenn wir die auf `"__main__"` setzen, gibt es quasi eine Konvention, dass wir die Befehle, die innerhalb dessen stehen, nur ausführen, wenn die Datei direkt gestartet wird und nicht durch Aufruf innerhalb eines anderen Moduls -> Achtung ist keine klassiche Magic Methode, nur eine Konvention
- `__eq__`: Damit können wir den Operator == nutzen, das heißt auf Gleichheit testen
- `__str__(self)`: Lesbare String-Repräsentation meines Objektes dieser Klasse. Rufe ich mit print(object) oder str(object) auf.
- `__repr__(self)`: Wichtig fürs Debugging oder Logging in der Entwicklung, rufe ich auf mit repr(object) z.B. auch in Listen
- auch interessant: Container-Methoden wie z.B. `__len__(self)` wenn ich z.B. die Länge des Objekts herausfinden möchte
---
- Magic Methoden sind spezielle Methoden, die wir in Python in Klassen benutzen wollen. Sie zeichnen sich durch doppelte Unterstriche aus (Dunder). 
- Sie können bestimmte Standardoperationen für eigene Klassen implementieren, wie z.B. die Gleichheitsfunktion `__eq__`