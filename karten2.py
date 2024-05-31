class GefaengnisKarte(object):
    def __init__(self):
        self.name = 'Gefängniskarte'
        self.text = 'Gehe ins Gefängnis.\n Begib dich direkt dorthin.\n Gehe nicht über Los\n Ziehe keine 200$ ein.'
        
    def ausfuehren(self, pSpieler):
        pSpieler.setGefaengnis(True)
        
    def getName(self):
        return self.name
    
    def getText(self):
        return self.text
    
class Gefaengnisfreikarte(object):
    def __init__(self):
        self.name = 'Gefängnisfreikarte'
        self.text = 'Gefängnisfreikarte'
        
    def ausfuehren(self, pSpieler):
        pSpieler.gefaengnisFreiKarteHinzufuegen('Gefängnisfreikarte')
        
    def getName(self):
        return self.name
    
    def getText(self):
        return self.text
        
class ZieheAufKarte(object):
    def __init__(self, pName, pText, pFeld):
        self.name = pName
        self.text = pText
        self.feld = pFeld
        
    def ausfuehren(self, pSpieler):
        spm = pSpieler.getSpm()
        indexNeuesFeld = spm.getKoordinatenNamen().index(self.feld)
        indexAltesFeld = spm.getKoordinatenNamen().index(pSpieler.getPosition())
        anzahl = indexNeuesFeld - indexAltesFeld
        if anzahl < 0:
            anzahl = 40 + anzahl
        spm.ruecken(anzahl, pSpieler)
        return 1
        
    def getName(self):
        return self.name
    
    def getText(self):
        return self.text
    
        
class ZieheZumNaechsten(object):
    def __init__(self, pName, pText, pFeld):
        self.name = pName
        self.text = pText
        self.feld = pFeld
        
    def ausfuehren(self, pSpieler):
        spm = pSpieler.getSpm()
        indexAltesFeld = spm.getKoordinatenNamen().index(pSpieler.getPosition())
        listeNamenKoordinaten = spm.getKoordinatenNamen()
        i = indexAltesFeld
        while True:
            if i == 40:
                i = 0
            if self.feld in listeNamenKoordinaten[i]:
                indexNeuesFeld = i
                break
            i += 1
        anzahl = indexNeuesFeld - indexAltesFeld
        if anzahl < 0:
            anzahl = 40 + anzahl
        spm.ruecken(anzahl, pSpieler)
        return 2
        
    def getName(self):
        return self.name
    
    def getText(self):
        return self.text
        
class BekommeGeld(object):
    def __init__(self, pName, pText, pWert):
        self.name = pName
        self.text = pText
        self.wert = pWert
        
    def ausfuehren(self, pSpieler):
        spm = pSpieler.getSpm()
        if self.wert < 0:
            pSpieler.geldAuszahlen(-self.wert)
            spm.freiParkenEinzahlen(self.wert)
        else:
            pSpieler.geldEinzahlen(self.wert)
    
    def getName(self):
        return self.name
    
    def getText(self):
        return self.text
            
            
class ZahleJedemSpieler(object):
    def __init__(self, pName, pText, pWert):
        self.name = pName
        self.text = pText
        self.wert = pWert
    
    def ausfuehren(self, pSpieler):
        spm = pSpieler.getSpm()
        spieler = spm.getSpieler()
        for spieler1 in spieler:
            if spieler1 != pSpieler:
                spieler1.geldEinzahlen(self.wert)
                pSpieler.geldAuszahlen(self.wert)
    
    def getName(self):
        return self.name
    
    def getText(self):
        return self.text
            
class JederSpielerSchenktDir(object):
    def __init__(self, pName, pText, pWert):
        self.name = pName
        self.text = pText
        self.wert = pWert
    
    def ausfuehren(self, pSpieler):
        spm = pSpieler.getSpm()
        spieler = spm.getSpieler()
        for spieler1 in spieler:
            if spieler1 != pSpieler:
                spieler1.geldAuszahlen(self.wert)
                pSpieler.geldEinzahlen(self.wert)
            
    def getName(self):
        return self.name
    
    def getText(self):
        return self.text

class RueckeUm(object):
    def __init__(self, pName, pText, pAnzahl):
        self.name = pName
        self.text = pText
        self.anzahl = pAnzahl
    
    def ausfuehren(self, pSpieler):
        spm = pSpieler.getSpm()
        spm.ruecken(self.anzahl, pSpieler)
        return 1
        
    def getName(self):
        return self.name
    
    def getText(self):
        return self.text
    
class Renovieren(object):
    def __init__(self, pName, pText, pKostenHaus, pKostenHotel):
        self.name = pName
        self.text = pText
        self.kostenHaus = pKostenHaus
        self.kostenHotel = pKostenHotel
        
    def ausfuehren(self, pSpieler):
        karten = pSpieler.getKarten()
        for karte in karten:
            haeuser = karte.getHaeuser()
            if haeuser == 5:
                pSpieler.geldAuszahlen(self.kostenHotel)
                pSpieler.getSpm().freiParkenEinzahlen(self.kostenHotel)
            else:
                pSpieler.geldAuszahlen(self.kostenHaus*haeuser)
                pSpieler.getSpm().freiParkenEinzahlen(self.kostenHaus*haeuser)
                
    def getName(self):
        return self.name
    
    def getText(self):
        return self.text