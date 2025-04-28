# ### 1. 🚗 **Tankstelle / Auto-Simulator**

# **Aufgabenstellung:**
# Erstelle eine Klasse **Auto**, die folgende Funktionen bietet:

# - **Tankfüllung anzeigen**: Zeigt den aktuellen Benzinstand an.
# - **Tanken**: Das Auto kann Benzin tanken.
# - **Fahren**: Beim Fahren wird Benzin verbraucht.

class Auto:
    tank_volumen: int
    marke: str
    verbrauch_pro_km: float
    tankinhalt: int

    def __init__(self, tank_volumen, marke, verbrauch_pro_km, tankinhalt):
        self.tank_volumen = tank_volumen
        self.marke = marke
        self.verbrauch_pro_km = verbrauch_pro_km
        self.tankinhalt = tankinhalt

    def tankanzeige(self):
        print(f"Das Auto {self.marke} hat den aktuellen Tankinhalt {self.tankinhalt} Liter")

    def tanken(self, liter):
        if liter > 0 and liter <= self.tank_volumen: 
            self.tankinhalt += liter
            print(f"{liter} Liter getankt!")
        else:
            print("Ungültige Tankmenge")

    def fahren(self, kilometer):
        verbrauchter_sprit = self.verbrauch_pro_km * kilometer
        if verbrauchter_sprit <= self.tankinhalt:
            print(f"Wir haben {verbrauchter_sprit} Liter für {kilometer} KM verbraucht")
            self.tankinhalt -= verbrauchter_sprit
            print(f"Der neue Tankinhalt beträgt {self.tankinhalt}")
        else:
            print("Nicht genug Benzin für die Fahrt!")



mein_auto = Auto(40, "Skoda", 0.06, 35)
mein_auto.tankanzeige()
print("Wir wollen tanken")
mein_auto.tanken(6)
mein_auto.tankanzeige()
print("Wir fahren ein Stück ..")
mein_auto.fahren(5)