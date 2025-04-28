# Erstelle einen einfachen Bankkonto-Simulator, der folgende Funktionen bietet:
#- Kontostand anzeigen
#- Geld einzahlen
#- Geld abheben

## Baue Klasse Bankkonto
class BankKonto:
    ## das kann auch weggelassen werden
    inhaber: str
    kontonummer: int
    kontostand: float
    ## Konstruktor
    def __init__(self, inhaber, kontonummer, empfänger, kontostand=0):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.kontostand = kontostand
        self.empfänger = empfänger

    ## Kontostand anzeigen
    def kontostand_anzeigen(self):
        print(f"Kontoauszug für {self.inhaber} mit Kontonummer {self.kontonummer}")
        print(f"Aktueller Kontostand: {self.kontostand}")

    ## Geld einzahlen
    def einzahlen(self, betrag):
        if betrag > 0:
            print(f"Es soll der Betrag {betrag} eingezahlt werden")
            self.kontostand += betrag
            print(f"Der neue Kontostand beträgt {self.kontostand}")
        else:
            print("Diese Transaktion war ungültig")

    ## Geld abheben
    def abheben(self, betrag):
        ## Beim Abheben drauf achten, dass genug Geld auf dem Konto
        ## und Betrag positiv
        if betrag > 0 and self.kontostand >= betrag:
            print(f"Es soll der Betrag {betrag} abgehoben werden")
            self.kontostand -= betrag
            print(f"Der neue Kontostand beträgt {self.kontostand}")
        else:
            print("Transaktion ungültig, vielleicht ist das Konto nicht gedeckt")


joels_bankkonto = BankKonto("Joel", 123456, 50, ["Katja", "Helen"])
joels_bankkonto.kontostand_anzeigen()
print(f"Es soll 50 Euro eingezahlt werden")
joels_bankkonto.einzahlen(50)
joels_bankkonto.kontostand_anzeigen()
print(f"Es soll 50 Euro abgehoben werden")
joels_bankkonto.abheben(150)

helens_bankkonto = BankKonto("Helen", 56789)
helens_bankkonto.kontostand_anzeigen()
print(f"Es soll 50 Euro eingezahlt werden")
helens_bankkonto.einzahlen(50)
helens_bankkonto.kontostand_anzeigen()
print(f"Es soll 50 Euro abgehoben werden")
helens_bankkonto.abheben(150)
