## Komposition
# Haus besteht aus vielen Räumen
# Räume können ohne Haus nicht existieren

# Klasse Raum (many-Seite)
class Raum:
    def __init__(self, groesse):
        self.groesse = groesse

    def __str__(self):
        return f"Raum mit {self.groesse} Quadratmetern"

# Klasse Haus (one-Seite)
class Haus:
    def __init__(self, farbe, hoehe, flaeche, adresse):
        self.farbe = farbe
        self.hoehe = hoehe
        self.flaeche = flaeche
        self.adresse = adresse
        self.raeume = [Raum(20), Raum(40)] # Komposition, d.h. initialisiere hier direkt die Objekte innerhalb der zugeordneten Klasse

    def __str__(self):
        raeume_string = ", ".join(str(raum) for raum in self.raeume)
        return f"Haus an der {self.adresse} mit den Räumen {raeume_string}"

# Verwendung
# raeume = [Raum(20), Raum(40)]
haus = Haus("gelb", 12, 200, "Neue Strasse 1")
print(haus)