## Implementiere zwei Klassen in einer Aggregations-Beziehung
## One-to-Many-Beziehung
# Klasse Buch
class Buch:
    def __init__(self, titel, autor):
        self.titel = titel
        self.autor = autor
    
    def __str__(self):
        return f"{self.titel} von {self.autor}"

# Klasse Bibliothek
class Bibliothek:
    def __init__(self, name):
        self.name = name
        self.buecher = [] # Aggregation: Eine Bibliothek besitzt mehrere Bücher
    
    # Funktion um ein Buch zur Bibliothek hinzuzufügen
    def buch_hinzufuegen(self, hinzuzufuegendes_buch):
        self.buecher.append(hinzuzufuegendes_buch)
    
    # Funktion um alle Bücher in der Bibliothek anzuzeigen
    def alle_buecher_anzeigen(self):
        for buch in self.buecher:
            print(buch)

## Hier findet die Magie statt zur Laufzeit
## erzeuge 2 Bücher
buch1 = Buch("Harry Potter", "J. K. Rowling")
buch2 = Buch("Der Herr der Ringe", "J. R. R. Tolkien")

# erzeuge 1 Bibliothek
bibliothek_berlin = Bibliothek("Stadtbibliothek Berlin")
# Bücher zur Bibliothek hinzufügen
bibliothek_berlin.buch_hinzufuegen(buch1)
bibliothek_berlin.buch_hinzufuegen(buch2)
# Zeige alle Bücher in der Bibliothek an 
bibliothek_berlin.alle_buecher_anzeigen()