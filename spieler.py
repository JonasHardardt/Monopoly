from wuerfel import Wuerfel
from tkinter import *

class Spieler(object):
    def __init__(self, pKuerzel, pGui, pSpm):
        self.kuerzel = pKuerzel
        self.karten = []
        self.position = ''
        self.positionKoordinaten = []
        self.label1 = Label(master = pGui.root, text = self.kuerzel)
        self.spm = pSpm
        self.geld = 3000
        self.wuerfel1 = Wuerfel()
        self.wuerfel2 = Wuerfel()
        self.gefaengnis = False
        self.gefaengnisFreiKarten = []
        self.braun = []
        self.hellblau = []
        self.pink = []
        self.orange = []
        self.rot = []
        self.gelb = []
        self.gruen = []
        self.dunkelblau = []
        self.bahnhof = []
        self.werk = []
        self.strassen = []
        
    def wuerfeln(self):
        return [self.wuerfel1.wuerfeln(), self.wuerfel2.wuerfeln()]
        
    def geldEinzahlen(self, pBetrag):
        self.geld += pBetrag
        
    def geldAuszahlen(self, pBetrag):
        self.geld -= pBetrag
        if self.geld < 0:
            self.spm.getGui().mitteilungText("Du hast nicht genügend Geld auf dem Konto")
            spieler = ''
            for spieler2 in self.spm.getSpieler():
                if spieler2.getKuerzel() == self.kuerzel:
                    spieler = spieler2    
            self.spm.getGui().abfrageEndeDerRunde(spieler, 'geld')
            
        
    def setSpielmanager(self, pSpm):
        self.spm = pSpm
        
    def setPosition(self, pPosition, koordinaten):
        self.position = pPosition
        self.positionKoordinaten = koordinaten
        self.label1.place(x = self.positionKoordinaten[0], y = self.positionKoordinaten[1], width = 30, height = 30)
        
    def karteHinzufuegen(self, pKarte):
        self.karten.append(pKarte)
        if pKarte.getFarbe() == 'braun':
            self.braun.append(pKarte)
            self.strasseUeberpruefen()
        elif pKarte.getFarbe() == 'hellblau':
            self.hellblau.append(pKarte)
            self.strasseUeberpruefen()
        elif pKarte.getFarbe() == 'pink':
            self.pink.append(pKarte)
            self.strasseUeberpruefen()
        elif pKarte.getFarbe() == 'orange':
            self.orange.append(pKarte)
            self.strasseUeberpruefen()
        elif pKarte.getFarbe() == 'rot':
            self.rot.append(pKarte)
            self.strasseUeberpruefen()
        elif pKarte.getFarbe() == 'gelb':
            self.gelb.append(pKarte)
            self.strasseUeberpruefen()
        elif pKarte.getFarbe() == 'gruen':
            self.gruen.append(pKarte)
            self.strasseUeberpruefen()
        elif pKarte.getFarbe() == 'dunkelblau':
             self.dunkelblau.append(pKarte)
             self.strasseUeberpruefen()
        elif pKarte.getFarbe() == 'bahnhof':
             self.bahnhof.append(pKarte)
             self.strasseUeberpruefen()
        elif pKarte.getFarbe() == 'werk':
             self.werk.append(pKarte)
             self.strasseUeberpruefen()
        
    
    def karteEntfernen(self, pKarte):
            self.karten.remove(pKarte)
            if pKarte.getFarbe() == 'braun':
                self.braun.remove(pKarte)
                self.strasseUeberpruefen()
            elif pKarte.getFarbe() == 'hellblau':
                self.hellblau.remove(pKarte)
                self.strasseUeberpruefen()
            elif pKarte.getFarbe() == 'pink':
                self.pink.remove(pKarte)
                self.strasseUeberpruefen()
            elif pKarte.getFarbe() == 'orange':
                self.orange.remove(pKarte)
                self.strasseUeberpruefen()
            elif pKarte.getFarbe() == 'rot':
                self.rot.remove(pKarte)
                self.strasseUeberpruefen()
            elif pKarte.getFarbe() == 'gelb':
                self.gelb.remove(pKarte)
                self.strasseUeberpruefen()
            elif pKarte.getFarbe() == 'gruen':
                self.gruen.remove(pKarte)
                self.strasseUeberpruefen()
            elif pKarte.getFarbe() == 'dunkelblau':
                 self.dunkelblau.remove(pKarte)
                 self.strasseUeberpruefen()
            elif pKarte.getFarbe() == 'bahnhof':
                 self.bahnhof.remove(pKarte)
                 self.strasseUeberpruefen()
            elif pKarte.getFarbe() == 'werk':
                 self.werk.remove(pKarte)
                 self.strasseUeberpruefen()
             
    def strasseUeberpruefen(self):
        if len(self.braun) == 2 and self.braun[0].getHypothek() == False and self.braun[1].getHypothek() == False:
            for karte in self.braun:
                karte.setStrasse(True)
        else: 
            for karte in self.braun:
                karte.setStrasse(False)
                
        if len(self.hellblau) == 3 and self.hellblau[0].getHypothek() == False and self.hellblau[1].getHypothek() == False and self.hellblau[2].getHypothek() == False:
            for karte in self.hellblau:
                karte.setStrasse(True)
        else: 
            for karte in self.hellblau:
                karte.setStrasse(False)
                
        if len(self.pink) == 3 and self.pink[0].getHypothek() == False and self.pink[1].getHypothek() == False and self.pink[2].getHypothek() == False:
            for karte in self.pink:
                karte.setStrasse(True)
        else: 
            for karte in self.pink:
                karte.setStrasse(False)
                
        if len(self.orange) == 3 and self.orange[0].getHypothek() == False and self.orange[1].getHypothek() == False and self.orange[2].getHypothek() == False:
            for karte in self.orange:
                karte.setStrasse(True)
        else: 
            for karte in self.orange:
                karte.setStrasse(False)
                
        if len(self.rot) == 3 and self.rot[0].getHypothek() == False and self.rot[1].getHypothek() == False and self.rot[2].getHypothek() == False:
            for karte in self.rot:
                karte.setStrasse(True)
        else: 
            for karte in self.rot:
                karte.setStrasse(False)
                
        if len(self.gelb) == 3 and self.gelb[0].getHypothek() == False and self.gelb[1].getHypothek() == False and self.gelb[2].getHypothek() == False:
            for karte in self.gelb:
                karte.setStrasse(True)
        else: 
            for karte in self.gelb:
                karte.setStrasse(False)
                        
        if len(self.gruen) == 3 and self.gruen[0].getHypothek() == False and self.gruen[1].getHypothek() == False and self.gruen[2].getHypothek() == False:
                    for karte in self.gruen:
                        karte.setStrasse(True)
        else: 
            for karte in self.gruen:
                karte.setStrasse(False)
        
        if len(self.dunkelblau) == 2 and self.dunkelblau[0].getHypothek() == False and self.dunkelblau[1].getHypothek() == False:
                    for karte in self.dunkelblau:
                        karte.setStrasse(True)
        else: 
            for karte in self.dunkelblau:
                karte.setStrasse(False)
        
        if len(self.werk) == 2 and self.werk[0].getHypothek() == False and self.werk[1].getHypothek() == False:
                    for karte in self.dunkelblau:
                        karte.setStrasse(True)
        else: 
            for karte in self.werk:
                karte.setStrasse(False)
        
        
        for karte in self.bahnhof:
            karte.setStrasse(False)
            karte.setHaeuser(len(self.bahnhof))
            #print(karte.getHaeuser())
                
    def getGeld(self):
        return self.geld
    
    def getPosition(self):
        return self.position
        
    def getPositionKoordinaten(self):
        return self.positionKoordinaten
    
    def getGefaengnis(self):
        return self.gefaengnis
    
    def gefaengnisFreiKarteHinzufuegen(self, pKarte):
        self.gefaengnisFreiKarten += [pKarte]
        
    def gefaengnisFreiKarteEntfernen(self, pKarte):
        self.gefaengnisFreiKarten.remove(pKarte)
        
    def getGefaengnisFreiKarten(self):
        return self.gefaengnisFreiKarten
    
    def setGefaengnis(self, pZustand):
        self.gefaengnis = pZustand
        self.setPosition('gefaengnis', [60, 60])
        
    def getSpm(self):
        return self.spm
    
    def getKarten(self):
        return self.karten
    
    def getKuerzel(self):
        return self.kuerzel
    
    def getBraun(self):
        return self.braun
    
    def getHellblau(self):
        return self.hellblau
    
    def getPink(self):
        return self.pink
    
    def getOrange(self):
        return self.orange
    
    def getRot(self):
        return self.rot
    
    def getGelb(self):
        return self.gelb
    
    def getGruen(self):
        return self.gruen
    
    def getDunkelblau(self):
        return self.dunkelblau
        
        
        
        
        
        
        
        
        
        