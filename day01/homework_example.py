class Film:
    def __init__(self, titel, regisseur, jahr, genre):
        self.titel = titel
        self.regisseur = regisseur
        self.jahr = jahr
        self.genre = genre
        self.bewertungen = []

    def info(self):
        print(f"{self.titel} ({self.jahr}) - Regie: {self.regisseur}, Genre: {self.genre}")

    def bewerten(self, punkte):
        if 1 <= punkte <= 10:
            self.bewertungen.append(punkte)
            print(f"Bewertung ({punkte}/10) hinzugefügt.")
        else:
            print("Bewertung muss zwischen 1 und 10 liegen.")

    def durchschnittsbewertung(self):
        if self.bewertungen:
            durchschnitt = sum(self.bewertungen) / len(self.bewertungen)
            return round(durchschnitt, 1)
        else:
            return "Noch keine Bewertungen"

# Beispiel
inception = Film("Inception", "Christopher Nolan", 2010, "Sci-Fi")
inception.info()
inception.bewerten(9)
inception.bewerten(8)
print(f"Durchschnittsbewertung: {inception.durchschnittsbewertung()}")
