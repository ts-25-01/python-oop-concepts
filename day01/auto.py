## Auto-Beispiel
class Auto:
    ## Attribute definieren
    marke: str
    modell: str
    geschwindkeit: int

    ## Konstruktor (Erstellung und Initialisierung der Objekte)
    def __init__(self, marke, farbe, geschwindigkeit=80):
        ## Setze Attribute mit Parametern
        self.marke = marke
        self.farbe = farbe
        self.geschwindigkeit = geschwindigkeit
    ## Achtung in anderen Programmiersprachen gibt es den leeren Konstruktor:
    # def __init__():
    #     self.marke = ""
    #     self.farbe = ""
    #     self.geschwindkeit = ""
    ## leerer Konstruktor in python
    # def __init__(self):
    #     self.marke = ""
    #     self.farbe = ""
    #     self.geschwindkeit = 0
    ## Methode: Fahren
    def fahren(self):
        print(f"{self.marke} fährt mit {self.geschwindigkeit} km/h")

mein_auto = Auto("VW", "rot") # Bei der Erstellung/Instanziierung des Objekts übergeben wir diese Werte. Diese werden dann im Konstruktor verwurschtelt 
# mein_leeres_auto = Auto()
mein_auto.fahren()
print(mein_auto)
# print(mein_leeres_auto)
