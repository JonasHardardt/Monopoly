from tkinter import *
class Karte(object):
    def __init__(self):
        self.mietpreis = 0
        self.haeuser = 0
        self.hypothek = None
        self.besitzer = None
        self.strasse = False
        self.label = None
        
    def setBesitzer(self, pSpieler):
            self.besitzer = pSpieler
            self.label = Label(master = self.besitzer.getSpm().getGui().root, bg = 'white', text = str(self.besitzer.getKuerzel()))
            koordinaten = self.besitzer.getSpm().getKoordinaten()[self.besitzer.getSpm().getKoordinatenNamen().index(self.name)]
            if koordinaten[0] == 35:
                #koordinaten[0] = 95
                #koordinaten[1] -= 8
                newheight = 50
                newwidth = 20
                self.label.place(x = koordinaten[0] + 60, y = koordinaten[1] - 8, width = newwidth, height = newheight)
            elif koordinaten[1] == 35:
                #koordinaten[1] = 95
                #koordinaten[0] -= 8
                newheight = 20
                newwidth = 50
                self.label.place(x = koordinaten[0] - 8, y = koordinaten[1] + 60, width = newwidth, height = newheight)
            elif koordinaten[0] == 835:
                #koordinaten[0] = 785
                #koordinaten[1] -= 8
                newheight = 50
                newwidth = 20
                self.label.place(x = koordinaten[0] - 50, y = koordinaten[1] - 8, width = newwidth, height = newheight)
            elif koordinaten[1] == 835:
                #koordinaten[1] = 785
                #koordinaten[0] -= 8
                newheight = 20
                newwidth = 50
                self.label.place(x = koordinaten[0] - 8, y = koordinaten[1] - 50, width = newwidth, height = newheight)
            
    def setHypothekWert(self):
        self.hypothek = 0.5 * self.kaufpreis
            
    def hausKaufen(self, pAnzahl):
            #if self.besitzer.getName() == pSpieler:
            if self.besitzer.getGeld() >= self.hauspreis:
                self.haeuser += pAnzahl
                self.besitzer.geldAuszahlen(self.hauspreis*pAnzahl)
                self.label.config(text = str(self.haeuser), bg = 'green')
                if self.haeuser == 5:
                    self.label.config(text = '', bg = 'red')
            
    def hausVerkaufen(self, pAnzahl):
        #if self.besitzer.getName() == pSpieler:
        self.haeuser -= pAnzahl
        self.besitzer.geldEinzahlen(self.hauspreis*pAnzahl)
        self.label.config(text = str(self.haeuser), bg = 'green')
    
    def setStrasse(self, pZustand):
            self.strasse = pZustand
        
    def getFarbe(self):
        return self.farbe
    
    def getHypothek(self):
        if self.hypothek < 0:
            return True
        else:
            return False
    
    def getHaeuser(self):
        return self.haeuser
    
    def getMiete(self, pFaktor):
        self.mietpreisBestimmen()
        return self.mietpreis*pFaktor
    
    def getStelle(self):
        return self.stelle
    
    def getHauspreis(self):
        return self.hauspreis
    
    def getName(self):
        return self.name
    
    def getBesitzer(self):
        return self.besitzer
    
    def getStrasse(self):
        return self.strasse
    
    def setHypothek(self, pStatus):
        if pStatus == True:
            self.hypothek *= -1
            self.besitzer.geldEinzahlen(abs(self.hypothek))
        if pStatus == False:
            self.hypothek *= -1
            self.besitzer.geldEinzahlen(abs(self.hypothek)*1.1)
    
    def setHaeuser(self, pAnzahl):
        self.haeuser = pAnzahl
    
    def getKaufpreis(self):
        return self.kaufpreis
            
            
class Badstrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 60
        self.hauspreis = 50
        self.stelle = 1
        self.name = 'badstrasse'
        self.farbe = 'braun'
        self.setHypothekWert()
            
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 4
            elif self.haeuser == 1:
                self.mietpreis = 10
            elif self.haeuser == 2:
                self.mietpreis = 30
            elif self.haeuser == 3:
                self.mietpreis = 90
            elif self.haeuser == 4:
                self.mietpreis = 160
            elif self.haeuser == 5:
                self.mietpreis = 250
        else:
            self.mietpreis = 2 
    
class Turmstrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 60
        self.hauspreis = 50
        self.stelle = 3
        self.name = 'turmstrasse'
        self.farbe = 'braun'
        self.setHypothekWert()
    
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 8
            elif self.haeuser == 1:
                self.mietpreis = 20
            elif self.haeuser == 2:
                self.mietpreis = 60
            elif self.haeuser == 3:
                self.mietpreis = 180
            elif self.haeuser == 4:
                self.mietpreis = 320
            elif self.haeuser == 5:
                self.mietpreis = 450
        else:
            self.mietpreis = 4 
   
class Chausseestrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 100
        self.hauspreis = 50
        self.stelle = 6
        self.name = 'chausseestrasse'
        self.farbe = 'hellblau'
        self.setHypothekWert()
    
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 12
            elif self.haeuser == 1:
                self.mietpreis = 30
            elif self.haeuser == 2:
                self.mietpreis = 90
            elif self.haeuser == 3:
                self.mietpreis = 270
            elif self.haeuser == 4:
                self.mietpreis = 400
            elif self.haeuser == 5:
                self.mietpreis = 550
        else:
            self.mietpreis = 6 
        
class Elisenstrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 100
        self.hauspreis = 50
        self.stelle = 8
        self.name = 'elisenstrasse'
        self.farbe = 'hellblau'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 12
            elif self.haeuser == 1:
                self.mietpreis = 30
            elif self.haeuser == 2:
                self.mietpreis = 90
            elif self.haeuser == 3:
                self.mietpreis = 270
            elif self.haeuser == 4:
                self.mietpreis = 400
            elif self.haeuser == 5:
                self.mietpreis = 550
        else:
            self.mietpreis = 6
        
class Poststrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 120
        self.hauspreis = 50
        self.stelle = 9
        self.name = 'poststrasse'
        self.farbe = 'hellblau'
        self.setHypothekWert()
    
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 16
            elif self.haeuser == 1:
                self.mietpreis = 40
            elif self.haeuser == 2:
                self.mietpreis = 100
            elif self.haeuser == 3:
                self.mietpreis = 300
            elif self.haeuser == 4:
                self.mietpreis = 450
            elif self.haeuser == 5:
                self.mietpreis = 600
        else:
            self.mietpreis = 8 
        
class Seestrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 140
        self.hauspreis = 100
        self.stelle = 10
        self.name = 'seestrasse'
        self.farbe = 'pink'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 20
            elif self.haeuser == 1:
                self.mietpreis = 50
            elif self.haeuser == 2:
                self.mietpreis = 150
            elif self.haeuser == 3:
                self.mietpreis = 450
            elif self.haeuser == 4:
                self.mietpreis = 625
            elif self.haeuser == 5:
                self.mietpreis = 750
        else:
            self.mietpreis = 10 
        
class Hafenstrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 140
        self.hauspreis = 100
        self.stelle = 12
        self.name = 'hafenstrasse'
        self.farbe = 'pink'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 20
            elif self.haeuser == 1:
                self.mietpreis = 50
            elif self.haeuser == 2:
                self.mietpreis = 150
            elif self.haeuser == 3:
                self.mietpreis = 450
            elif self.haeuser == 4:
                self.mietpreis = 625
            elif self.haeuser == 5:
                self.mietpreis = 750
        else:
            self.mietpreis = 10 
        
class Neuestrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 160
        self.hauspreis = 100
        self.stelle = 6
        self.name = 'neuestrasse'
        self.farbe = 'pink'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 24
            elif self.haeuser == 1:
                self.mietpreis = 60
            elif self.haeuser == 2:
                self.mietpreis = 180
            elif self.haeuser == 3:
                self.mietpreis = 500
            elif self.haeuser == 4:
                self.mietpreis = 700
            elif self.haeuser == 5:
                self.mietpreis = 900
        else:
            self.mietpreis = 12 
        
class Muenchenerstrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 180
        self.hauspreis = 100
        self.stelle = 7
        self.name = 'muenchenerstrasse'
        self.farbe = 'orange'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 28
            elif self.haeuser == 1:
                self.mietpreis = 70
            elif self.haeuser == 2:
                self.mietpreis = 200
            elif self.haeuser == 3:
                self.mietpreis = 550
            elif self.haeuser == 4:
                self.mietpreis = 750
            elif self.haeuser == 5:
                self.mietpreis = 950
        else:
            self.mietpreis = 14 
        
class Wienerstrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 180
        self.hauspreis = 100
        self.stelle = 8
        self.name = 'wienerstrasse'
        self.farbe = 'orange'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 28
            elif self.haeuser == 1:
                self.mietpreis = 70
            elif self.haeuser == 2:
                self.mietpreis = 200
            elif self.haeuser == 3:
                self.mietpreis = 550
            elif self.haeuser == 4:
                self.mietpreis = 750
            elif self.haeuser == 5:
                self.mietpreis = 950
        else:
            self.mietpreis = 14
            
        
class Berlinerstrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 200
        self.hauspreis = 100
        self.stelle = 9
        self.name = 'berlinerstrasse'
        self.farbe = 'orange'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 32
            elif self.haeuser == 1:
                self.mietpreis = 80
            elif self.haeuser == 2:
                self.mietpreis = 220
            elif self.haeuser == 3:
                self.mietpreis = 600
            elif self.haeuser == 4:
                self.mietpreis = 800
            elif self.haeuser == 5:
                self.mietpreis = 1000
        else:
            self.mietpreis = 16
            
        
class Theaterstrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 220
        self.hauspreis = 150
        self.stelle = 10
        self.name = 'theaterstrasse'
        self.farbe = 'rot'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 36
            elif self.haeuser == 1:
                self.mietpreis = 90
            elif self.haeuser == 2:
                self.mietpreis = 250
            elif self.haeuser == 3:
                self.mietpreis = 700
            elif self.haeuser == 4:
                self.mietpreis = 875
            elif self.haeuser == 5:
                self.mietpreis = 1050
        else:
            self.mietpreis = 18
            
        
class Museumstrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 220
        self.hauspreis = 150
        self.stelle = 11
        self.name = 'museumstrasse'
        self.farbe = 'rot'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 36
            elif self.haeuser == 1:
                self.mietpreis = 90
            elif self.haeuser == 2:
                self.mietpreis = 250
            elif self.haeuser == 3:
                self.mietpreis = 700
            elif self.haeuser == 4:
                self.mietpreis = 875
            elif self.haeuser == 5:
                self.mietpreis = 1050
        else:
            self.mietpreis = 18
            
        
class Opernplatz(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 240
        self.hauspreis = 150
        self.stelle = 12
        self.name = 'opernplatz'
        self.farbe = 'rot'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 40
            elif self.haeuser == 1:
                self.mietpreis = 100
            elif self.haeuser == 2:
                self.mietpreis = 300
            elif self.haeuser == 3:
                self.mietpreis = 750
            elif self.haeuser == 4:
                self.mietpreis = 925
            elif self.haeuser == 5:
                self.mietpreis = 1100
        else:
            self.mietpreis = 20 
        
class Lessingstrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 260
        self.hauspreis = 150
        self.stelle = 13
        self.name = 'lessingstrasse'
        self.farbe = 'gelb'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 44
            elif self.haeuser == 1:
                self.mietpreis = 110
            elif self.haeuser == 2:
                self.mietpreis = 330
            elif self.haeuser == 3:
                self.mietpreis = 800
            elif self.haeuser == 4:
                self.mietpreis = 975
            elif self.haeuser == 5:
                self.mietpreis = 1150
        else:
            self.mietpreis = 22 
        
class Schillerstrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 260
        self.hauspreis = 150
        self.stelle = 14
        self.name = 'schillerstrasse'
        self.farbe = 'gelb'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 44
            elif self.haeuser == 1:
                self.mietpreis = 110
            elif self.haeuser == 2:
                self.mietpreis = 330
            elif self.haeuser == 3:
                self.mietpreis = 800
            elif self.haeuser == 4:
                self.mietpreis = 975
            elif self.haeuser == 5:
                self.mietpreis = 1150
        else:
            self.mietpreis = 22 
        
class Goethestrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 280
        self.hauspreis = 150
        self.stelle = 15
        self.name = 'goethestrasse'
        self.farbe = 'gelb'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 48
            elif self.haeuser == 1:
                self.mietpreis = 120
            elif self.haeuser == 2:
                self.mietpreis = 360
            elif self.haeuser == 3:
                self.mietpreis = 850
            elif self.haeuser == 4:
                self.mietpreis = 1025
            elif self.haeuser == 5:
                self.mietpreis = 1200
        else:
            self.mietpreis = 24
            
        
class Rathausplatz(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 300
        self.hauspreis = 200
        self.stelle = 16
        self.name = 'rathausplatz'
        self.farbe = 'gruen'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 52
            elif self.haeuser == 1:
                self.mietpreis = 130
            elif self.haeuser == 2:
                self.mietpreis = 390
            elif self.haeuser == 3:
                self.mietpreis = 900
            elif self.haeuser == 4:
                self.mietpreis = 1100
            elif self.haeuser == 5:
                self.mietpreis = 1275
        else:
            self.mietpreis = 26
            
        
class Hauptstrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 300
        self.hauspreis = 200
        self.stelle = 17
        self.name = 'hauptstrasse'
        self.farbe = 'gruen'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 52
            elif self.haeuser == 1:
                self.mietpreis = 130
            elif self.haeuser == 2:
                self.mietpreis = 390
            elif self.haeuser == 3:
                self.mietpreis = 900
            elif self.haeuser == 4:
                self.mietpreis = 1100
            elif self.haeuser == 5:
                self.mietpreis = 1275
        else:
            self.mietpreis = 26
            
        
class Bahnhofstrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 320
        self.hauspreis = 200
        self.stelle = 18
        self.name = 'bahnhofstrasse'
        self.farbe = 'gruen'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 56
            elif self.haeuser == 1:
                self.mietpreis = 150
            elif self.haeuser == 2:
                self.mietpreis = 450
            elif self.haeuser == 3:
                self.mietpreis = 1000
            elif self.haeuser == 4:
                self.mietpreis = 1200
            elif self.haeuser == 5:
                self.mietpreis = 1400
        else:
            self.mietpreis = 28
            
        
class Parkstrasse(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 350
        self.hauspreis = 200
        self.stelle = 19
        self.name = 'parkstrasse'
        self.farbe = 'dunkelblau'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 70
            elif self.haeuser == 1:
                self.mietpreis = 175
            elif self.haeuser == 2:
                self.mietpreis = 500
            elif self.haeuser == 3:
                self.mietpreis = 1100
            elif self.haeuser == 4:
                self.mietpreis = 1300
            elif self.haeuser == 5:
                self.mietpreis = 1500
        else:
            self.mietpreis = 35
            
        
class Schlossallee(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 400
        self.hauspreis = 200
        self.stelle = 20
        self.name = 'schlossallee'
        self.farbe = 'dunkelblau'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            if self.haeuser == 0:
                self.mietpreis = 100
            elif self.haeuser == 1:
                self.mietpreis = 200
            elif self.haeuser == 2:
                self.mietpreis = 600
            elif self.haeuser == 3:
                self.mietpreis = 1400
            elif self.haeuser == 4:
                self.mietpreis = 1700
            elif self.haeuser == 5:
                self.mietpreis = 2000
        else:
            self.mietpreis = 50
            
        
class Suedbahnhof(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 200
        self.stelle = 21
        self.name = 'suedbahnhof'
        self.farbe = 'bahnhof'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        self.mietpreis = 25*(2**(self.haeuser-1))
            
        
class Westbahnhof(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 200
        self.stelle = 22
        self.name = 'westbahnhof'
        self.farbe = 'bahnhof'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        self.mietpreis = 25*(2**(self.haeuser-1))
            
        
class Nordbahnhof(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 200
        self.stelle = 23
        self.name = 'nordbahnhof'
        self.farbe = 'bahnhof'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        self.mietpreis = 25*(2**(self.haeuser-1))
            
        
class Hauptbahnhof(Karte):
    def __init__(self):
        super().__init__()
        self.kaufpreis = 200
        self.stelle = 24
        self.name = 'hauptbahnhof'
        self.farbe = 'bahnhof'
        self.setHypothekWert()
        
    def mietpreisBestimmen(self):
        self.mietpreis = 25*(2**(self.haeuser-1))
            
        
class Elektrizitaetswerk(Karte):
    def __init__(self, pGui):
        super().__init__()
        self.kaufpreis = 150
        self.stelle = 25
        self.name = 'elektrizitaetswerk'
        self.farbe = 'werk'
        self.setHypothekWert()
        self.gui = pGui
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            a1, a2 = self.gui.wuerfeln()
            summe = a1 + a2
            print(summe)
            self.mietpreis = 10 * summe
        else:
            a1, a2 = self.gui.wuerfeln()
            summe = a1 + a2
            self.mietpreis = 4 * summe
            
        
class Wasserwerk(Karte):
    def __init__(self, pGui):
        super().__init__()
        self.kaufpreis = 150
        self.stelle = 26
        self.name = 'wasserwerk'
        self.farbe = 'werk'
        self.setHypothekWert()
        self.gui = pGui
        
    def mietpreisBestimmen(self):
        if self.strasse == True:
            a1, a2 = self.gui.wuerfeln()
            summe = a1 + a2
            print(summe)
            self.mietpreis = 10 * summe
        else:
            a1, a2 = self.gui.wuerfeln()
            summe = a1 + a2
            self.mietpreis = 4 * summe
            
        
class Gemeinschaftsfeld(Karte):
    def __init__(self):
        #self.stelle =
        self.name = 'gemeinschaftsfeld'
        s#elf.kartenListe =
        
class Ereignisfeld(Karte):
    def __init__(self):
        #self.stelle =
        self.name = 'ereignisfeld'
        #self.kartenListe =
        
class Einkommenssteuer(Karte):
    def __init__(self):
        #self.stelle =
        self.name = 'einkommenssteuer'
        
class ImGefaengnis(Karte):
    def __init__(self):
        #self.stelle =
        self.name = 'imgefaengnis'

class NurZuBesuch(Karte):
    def __init__(self):
        #self.stelle =
        self.name = 'nurzubesuch'
        
class FreiParken(Karte):
    def __init__(self):
        #self.stelle =
        self.name = 'freiparken'  
        
class GehenSieInDasGefaengnis(Karte):
    def __init__(self):
        #self.stelle =
        self.name = 'gehensieindasgefaengnis'
        
class ZusatzSteuer(Karte):
    def __init__(self):
        #self.stelle =
        self.name = 'zusatzsteuer'
        
class Los(Karte):
    def __init__(self):
        #self.stelle =
        self.name = 'los'
        
        
    