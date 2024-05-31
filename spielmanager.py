from gui import GUI
from spieler import Spieler
from ereignismanager import Ereignismanager
from time import sleep
class Spielmanager(object):
    def __init__(self):
        self.gui = None
        self.spieler = []
        self.ereignismanager = None
        self.koordinaten = [[35, 822.5], [35, 728], [35, 654], [35, 580], [35, 506], [35, 432], [35, 358], [35, 284], [35, 210], [35, 136],
                            [5, 5], [141, 35], [215, 35], [289, 35], [363, 35], [437, 35], [511, 35], [585, 35], [659, 35], [733, 35],
                            [835, 35], [835, 141], [835, 215], [835, 289], [835, 363], [835, 437], [835, 511], [835, 585], [835, 659], [835, 733],
                            [835, 835],[733, 835], [659, 835], [585, 835], [511, 835], [437, 835], [363, 835], [289, 835], [215, 835], [141, 835]]
        self.koordinatenNamen = ['los', 'badstrasse', 'gemeinschaftsfeld1', 'turmstrasse', 'einkommensteuer', 'suedbahnhof', 'chausseestrasse', 'ereignisfeld1', 'elisenstrasse', 'poststrasse',
                                 'nurzubesuch', 'seestrasse', 'elektrizitaetswerk', 'hafenstrasse', 'neuestrasse', 'westbahnhof', 'muenchenerstrasse', 'gemeinschaftsfeld2', 'wienerstrasse', 'berlinerstrasse',
                                 'freiparken', 'theaterstrasse', 'ereignisfeld2', 'museumstrasse', 'opernplatz', 'nordbahnhof', 'lessingstrasse', 'schillerstrasse', 'wasserwerk', 'goethestrasse',
                                 'gehensieindasgefaengnis', 'rathausplatz', 'hauptstrasse', 'gemeinschaftsfeld', 'bahnhofstrasse', 'hauptbahnhof', 'ereignisfeld2', 'parkstrasse', 'zusatzsteuer', 'schlossallee']
        self.freiParkenWert = 0
        #self.setKoordinaten()
        #self.erzeugeSpieler()
    
    def start(self, pSpm):
        self.gui = GUI(pSpm)
        self.gui.root.mainloop()
        
    
    def setKoordinaten(self):
        xPosition = gui.getXPosition()
        yPosition = gui.getYPosition()
        for i in range(40):
            if i == 0:
                self.position += [[35 + xPosition, 822.5 + yPosition]]
            if i < 10 and i != 0:
                gesamt = 728
                self.position += [[35 + xPosition, 728-(i-1)*74 + yPosition]]
            if i == 10:
                self.position += [[0 + xPosition, 0 + yPosition]]
            if i > 10 and i < 20:
                gesamt = 728
                self.position += [[728-(i-10)*74 + xPosition, 35 + yPosition]]
            if i == 20:
                self.position += [[835 + xPosition, 35 + yPosition]]
            if i > 20 and i < 30:
                gesamt = 728
                self.position += [[835 + xPosition, 728-(10-(i-20))*74 + yPosition]]
        
#     def erzeugeSpieler(self):
#         print('test')
#         print(self.gui)
#         self.gui.abfrageAnzahlSpieler()
    
    def erzeugeSpieler(self, pAnzahl, pKuerzel, pSpm):
        #self.gui.abfrageAnzahlSpieler()
        print(pAnzahl, pKuerzel)
        for i in range(pAnzahl):
            self.spieler += [Spieler(pKuerzel[i], self.gui, pSpm)]
            self.spieler[i].setPosition('los', [35, 822.5])
#         self.ereignismanager = Ereignismanager(self.spieler[0])
#         self.ereignismanager.kartenmanager.karteVerkaufen(self.spieler[0], self.ereignismanager.kartenmanager.kartenListe[22])
#         self.ereignismanager.kartenmanager.karteVerkaufen(self.spieler[0], self.ereignismanager.kartenmanager.kartenListe[23])
#         self.ereignismanager.kartenmanager.karteVerkaufen(self.spieler[0], self.ereignismanager.kartenmanager.kartenListe[0])
#         self.ereignismanager.kartenmanager.karteVerkaufen(self.spieler[0], self.ereignismanager.kartenmanager.kartenListe[1])
#         self.ereignismanager.kartenmanager.karteVerkaufen(self.spieler[0], self.ereignismanager.kartenmanager.kartenListe[17])
#         self.ereignismanager.kartenmanager.karteVerkaufen(self.spieler[0], self.ereignismanager.kartenmanager.kartenListe[18])
#         self.ereignismanager.kartenmanager.karteVerkaufen(self.spieler[0], self.ereignismanager.kartenmanager.kartenListe[19])
#         self.ereignismanager.kartenmanager.karteVerkaufen(self.spieler[1], self.ereignismanager.kartenmanager.kartenListe[11])
#         self.ereignismanager.kartenmanager.karteVerkaufen(self.spieler[1], self.ereignismanager.kartenmanager.kartenListe[12])
#         self.ereignismanager.kartenmanager.karteVerkaufen(self.spieler[1], self.ereignismanager.kartenmanager.kartenListe[13])
#         self.ereignismanager.kartenmanager.karteVerkaufen(self.spieler[1], self.ereignismanager.kartenmanager.kartenListe[24])
        #self.spieler[1].karteHinzufuegen()
        #self.spieler[0].setPosition('los', [35, 822.5])
        #self.spieler[1].setPosition('los', [35, 822.5])
        self.ereignismanager = Ereignismanager(self.spieler[0])
        self.spielen()
    
    def spielerAbmelden(self):
        for z in self.spieler:
            if z.getGeld() < 0:
                self.spieler.remove(z)
    
    def spielen(self):
         while len(self.spieler) > 1:
             for z in self.spieler:
                pasch = True
                paschZaehler = 0
                if z.getGefaengnis() == True:
                    rueckgabe = self.gefaengnisFrei(z)
                if z.getGefaengnis() == False:                    
                    while pasch == True:
                        pasch = False
                        ergebnis = self.gui.wuerfeln()
                        print(ergebnis)
                        print(z.getKuerzel(), z.getGeld())
                        if ergebnis[0] == ergebnis[1]:
                            pasch = True
                            paschZaehler += 1
                            if paschZaehler == 3:
                                z.setGefaengnis(True)
                        self.ruecken(ergebnis[0]+ergebnis[1], z)
                        sleep(0.2)
                        self.ereignismanager.auswerten(z, 1)
                        if pasch == True:
                            self.gui.mitteilungText('Da Sie einen Pasch gewürfelt haben, dürfen Sie nochmals würfeln')
                        print(z.getKuerzel(), z.getGeld())
                    print()
                    self.gui.abfrageEndeDerRunde(z, '')
#                     sleep(0.5)
#                     #print(self.spieler)
#                     print(z.getKuerzel(), z.getGeld())
#                     z.setPosition('ereignisfeld1', [35, 284])
#                     self.ereignismanager.auswerten(z, 1)
#                     print(z.getKuerzel(), z.getGeld())
#                     
    def ruecken(self, pAnzahl, pSpieler):
        aktuellePosition = pSpieler.getPositionKoordinaten()
        aktuellerIndex = self.koordinaten.index(aktuellePosition)
        neuerIndex = aktuellerIndex + pAnzahl
        if neuerIndex > 39:
            neuerIndex -= 40
            pSpieler.geldEinzahlen(200)
        pSpieler.setPosition(self.koordinatenNamen[neuerIndex], self.koordinaten[neuerIndex])
        
    def gefaengnisFrei(self, pSpieler):
        abfrage = self.gui.abfrageGefaengnis(pSpieler)
        if abfrage == 'bezahlen':
            pSpieler.geldAuszahlen(50)
            pSpieler.setPosition(self.koordinatenNamen[10], self.koordinaten[10])
            pSpieler.setGefaengnis(False)
        elif abfrage == 'gefaengnisFreiKarte':
            karten = pSpieler.getGefaengnisFreiKarten()
            if len(karten) > 0:
                pSpieler.gefaengnisFreiKarteEntfernen(karten[0])
                pSpieler.setPosition(self.koordinatenNamen[10], self.koordinaten[10])
                pSpieler.setGefaengnis(False)
        elif abfrage == 'wuerfeln':
            i = 1
            pasch = False
            while 1 <= 3 and pasch == False:
                ergebnis = pSpieler.wuerfeln()
                if ergebnis[0] == ergebnis[1]:
                    pasch = True
                    pSpieler.gefaengnisFreiKarteEntfernen(karten[0])
                    pSpieler.setPosition(self.koordinatenNamen[10], self.koordinaten[10])
                    pSpieler.setGefaengnis(False)
                ruecken(ergebnis[0]+ergebnis[1], z)
                ereignismanager.auswerten(pSpieler.getPosition())
                
    def freiParkenEinzahlen(self, pBetrag):
        self.freiParkenWert += pBetrag
        
    def freiParkenAuszahlen(self):
        merke = self.freiParkenWert
        self.freiParkenWert = 0
        return merke
    
    def getKoordinatenNamen(self):
        return self.koordinatenNamen
    
    def getKoordinaten(self):
        return self.koordinaten
    
    def getSpieler(self):
        return self.spieler
    
    def getGui(self):
        return self.gui
    
    def getFreiParkenWert(self):
        return self.freiParkenWert
            
    def tauschen(self, pSpieler1, pSpieler2, pListeKarten1, pListeKarten2, pGeld1, pGeld2):
        tausch = True
        for karten in pListeKarten1:
            if karten not in pSpieler1.getKarten():
                print("Dieser Tausch ist nicht möglich.")
                tausch = False
        if tausch == False:
            for karten in pListeKarten2:
                if karten not in pSpieler2.getKarten():
                    print("Dieser Tausch ist nicht möglich.")
                    tausch = False
        if tausch == True:
            for karten in pListeKarten1:
                pSpieler1.karteEntfernen(karten)
                pSpieler2.karteHinzufuegen(karten)
                karten.setBesitzer(pSpieler2)
            for karten in pListeKarten2:
                pSpieler2.karteEntfernen(karten)
                pSpieler1.karteHinzufuegen(karten)
                karten.setBesitzer(pSpieler1)
            pSpieler1.geldAuszahlen(pGeld1)
            pSpieler2.geldEinzahlen(pGeld1)
            pSpieler2.geldAuszahlen(pGeld2)
            pSpieler1.geldEinzahlen(pGeld2)
                
        
        
        
                
            