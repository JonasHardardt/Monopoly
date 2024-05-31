from kartenmanager import Kartenmanager
from ereignisstapel import Ereignisstapel
from gemeinschaftsstapel import Gemeinschaftsstapel

class Ereignismanager(object):
    def __init__(self, pSpieler):
        self.spezielleEreignisse = ['los', 'gemeinschaftsfeld1', 'gemeinschaftsfeld2', 'einkommensteuer', 'ereignisfeld1', 'ereignisfeld2', 'nurzubesuch', 'gefaengnis', 'freiparken', 'gehensieindasgefaengnis', 'zusatzsteuer']
        self.kartenmanager = Kartenmanager(pSpieler)
        self.spm = pSpieler.getSpm()
        self.ereignisstapel = Ereignisstapel()
        self.ereignisstapel.mischen()
        self.gemeinschaftsstapel = Gemeinschaftsstapel()
        self.gemeinschaftsstapel.mischen()
        
    def setSpielmanager(self, pSpm):
        self.spm = pSpm
        
    def auswerten(self, pSpieler, pFaktor):
        position = pSpieler.getPosition()
        if pSpieler.getPosition() not in self.spezielleEreignisse:
            self.kartenmanager.auswerten(pSpieler, pFaktor)
        else:
            if position == 'gemeinschaftsfeld1' or position == 'gemeinschaftsfeld2':
                karte = self.gemeinschaftsstapel.pop()
                self.gemeinschaftsstapel.untenAnfuegen(karte)
                self.spm.getGui().mitteilungKarte(karte)
                print(karte.getText(), karte.getName())
                karte.ausfuehren(pSpieler)
            elif position == 'einkommensteuer':
                pSpieler.geldAuszahlen(200)
                self.spm.getGui().mitteilungText('Einkommensteuer\n Sie müssen 200$ bezahlen')
                self.spm.freiParkenEinzahlen(200)
            elif position == 'ereignisfeld1' or position == 'ereignisfeld2':
                karte = self.ereignisstapel.pop()
                self.ereignisstapel.untenAnfuegen(karte)
                self.spm.getGui().mitteilungKarte(karte)
                rueckgabe = karte.ausfuehren(pSpieler)
                if rueckgabe == 1:
                    self.auswerten(pSpieler, 1)
                elif rueckgabe == 2:
                    self.auswerten(pSpieler, 2)
            elif position == 'nurzubesuch':
                pass
            elif position == 'los':
                pass
            elif position == 'gefaengnis':
                pass
            elif position == 'freiparken':
                self.spm.getGui().mitteilungText('Sie sind auf Freiparken und erhalten' + str(self.spm.getFreiParkenWert))
                pSpieler.geldEinzahlen(self.spm.freiParkenAuszahlen())
            elif position == 'gehensieindasgefaengnis':
                pSpieler.setGefaengnis(True)
                self.spm.getGui().mitteilungText('Sie müssen in das Gefängnis')
                pSpieler.setPosition('gefaengnis', [60, 60])
            elif position == 'zusatzsteuer':
                pSpieler.geldAuszahlen(100)
                self.spm.getGui().mitteilungText('Zusatzsteuer\n Sie müssen 100$ bezahlen')
                self.spm.freiParkenEinzahlen(100)