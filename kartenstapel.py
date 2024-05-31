from random import randint

class Kartenstapel(object):
    def __init__(self, pListe):
        self.kartenListe = pListe
        
    def pop(self):
        karte = self.kartenListe[-1]
        del self.kartenListe[-1]
        return karte
    
    def untenAnfuegen(self, pKarte):
        self.kartenListe = [pKarte] + self.kartenListe
        
    def mischen(self):
        neueListe = []
        aktuelleAnzahl = len(self.kartenListe)
        while aktuelleAnzahl > 0:
            i = randint(0, aktuelleAnzahl-1)
            neueListe = neueListe + [self.kartenListe[i]]
            del self.kartenListe[i]
            aktuelleAnzahl = len(self.kartenListe)
        self.kartenListe = neueListe
        
    