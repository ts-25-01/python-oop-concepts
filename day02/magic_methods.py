# Beispiel für Magic Methoden
class Auto:
    ## Attribute
    marke: str
    modell: str
    tankvolumen: int

    def __init__(self, marke, modell, tankvolumen=80):
        self.marke = marke
        self.modell = modell
        self.tankvolumen = tankvolumen

    def __eq__(self, other):
        return self.marke == other.marke and self.modell == other.modell
    
    def __str__(self):
        return f"Der {self.modell} der Marke {self.marke} hat ein Tankvolumen von {self.tankvolumen} Liter"

    def __repr__(self):
        return f"Auto('{self.marke}', '{self.modell}', {self.tankvolumen})"

mein_auto = Auto("VW", "Golf")
anderes_auto = Auto("VW", "Passat")
print(mein_auto) # ruft str-Methode auf
print([mein_auto]) # ruft repr-Methoden auf
# print(3 == 2)
# print(f"Sind die Autos gleich? {mein_auto == anderes_auto}")

# liste = [1,2]
# liste[1] = 4

# def main_function():
#     print("Das ist die Hauptfunktion")

# if __name__ == "__main__":
#     main_function()