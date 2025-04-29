class Kurs:
    def __init__(self, titel):
        self.thema = titel
# Klasse Schüler, ein Schüler besucht den Kurs
class Schueler:
    # Attribute
    name: str
    besuchter_kurs: Kurs
    ## Konstruktur, um ein Schüler-Objekt der Klasse Schüler zu erzeugen
    def __init__(self, name):
        self.name = name
    
    ## Funktion, die sagt, dass ein Schüler einen Kurs besucht
    ## Assoziation zu der Klasse Kurs 
    def besuchen(self, besuchter_kurs: Kurs):
        print(f"Der Schüler {self.name} besucht den Kurs {besuchter_kurs.titel}")

## Verwendung
ein_schueler = Schueler("Hanno")
ein_kurs = Kurs("Python OOP")
## Assoziation testen, indem besuchen-Funktion für Schüler-Objekt aufgerufen wird
ein_schueler.besuchen(ein_kurs)


