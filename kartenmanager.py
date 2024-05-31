from karten import *

class Kartenmanager(object):
    def __init__(self, pSpieler):
        self.kartenListe = [Badstrasse(), Turmstrasse(), Chausseestrasse(), Elisenstrasse(), Poststrasse(),
                            Seestrasse(), Hafenstrasse(), Neuestrasse(), Muenchenerstrasse(), Wienerstrasse(), Berlinerstrasse(),
                            Theaterstrasse(), Museumstrasse(), Opernplatz(), Lessingstrasse(), Schillerstrasse(), Goethestrasse(),
                            Rathausplatz(), Hauptstrasse(), Bahnhofstrasse(), Parkstrasse(), Schlossallee(), Suedbahnhof(), Nordbahnhof(), Hauptbahnhof(), Westbahnhof(), Wasserwerk(pSpieler.getSpm().getGui()), Elektrizitaetswerk(pSpieler.getSpm().getGui())]
        self.spm = pSpieler.getSpm()
    
    def auswerten(self, pSpieler, pFaktor):
        aktuelleKarte = None
        for karte in self.kartenListe:
            if pSpieler.getPosition() == karte.getName():
                aktuelleKarte = karte
                break
            
        if aktuelleKarte.getBesitzer() == pSpieler:
            pass
        elif aktuelleKarte.getBesitzer() == None:
            self.karteVerkaufen(pSpieler, aktuelleKarte)
        else:
            self.mieteVerlangen(pSpieler, aktuelleKarte, pFaktor)
            
    def karteVerkaufen(self, pSpieler, aktuelleKarte):
        gui = pSpieler.getSpm().getGui()
        abfrage = gui.abfrageKaufen(pSpieler, aktuelleKarte)
        if abfrage == 'ja':
            aktuelleKarte.setBesitzer(pSpieler)
            pSpieler.geldAuszahlen(aktuelleKarte.getKaufpreis())
            pSpieler.karteHinzufuegen(aktuelleKarte)
            
    def mieteVerlangen(self, pSpieler, aktuelleKarte, pFaktor):
        gui = pSpieler.getSpm().getGui()
        if 'werk' in aktuelleKarte.getName() and pFaktor == 2:
            if aktuelleKarte.getStrasse == True:
                abfrage = gui.mitteilungMiete(aktuelleKarte.getMiete(1))
                pSpieler.geldAuszahlen(aktuelleKarte.getMiete(1))
                aktuelleKarte.getBesitzer().geldEinzahlen(aktuelleKarte.getMiete(1))
            else:
                aktuelleKarte.setStrasse(True)
                abfrage = gui.mitteilungMiete(aktuelleKarte.getMiete(1))
                pSpieler.geldAuszahlen(aktuelleKarte.getMiete(1))
                aktuelleKarte.getBesitzer().geldEinzahlen(aktuelleKarte.getMiete(1))
                aktuelleKarte.setStrasse(False)
        else:
            abfrage = gui.mitteilungMiete((aktuelleKarte.getMiete(pFaktor)))
            pSpieler.geldAuszahlen((aktuelleKarte.getMiete(pFaktor)))
            aktuelleKarte.getBesitzer().geldEinzahlen((aktuelleKarte.getMiete(pFaktor)))
        
        
    

