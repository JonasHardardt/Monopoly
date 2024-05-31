from kartenstapel import Kartenstapel
from karten2 import *

class Gemeinschaftsstapel(Kartenstapel):
    def __init__(self):
        kartenliste = [BekommeGeld('Lagerverkäufe', 'Aus Lagerverkäufen erhältst du 50$.', 50) , 
                        BekommeGeld('Einkommenssteuerrückzahlung', 'Einkommenssteuerrückzahlung. Du erhältst 20$.', 20) , 
                        BekommeGeld('Lebensversicherung', 'Deine Lebensversicherung wird fällig. Du erhältst 100$.', 100) , 
                        BekommeGeld('Bank-Irrtum', 'Bank-Irrtum zu deinen Gunsten. Ziehe 200$ ein.', 200) , 
                        BekommeGeld('Erbe', 'Du erbst 100$.', 100) , 
                        BekommeGeld('Beratungsgebühr', 'Du erhältst eine Beratungsgebühr von 25$.', 25) , 
                        BekommeGeld('Schönheitswettbewerb', 'Zweiter Preis beim Schönheitswettbewerb. Du erhältst 10$.', 10) , 
                        BekommeGeld('Urlaubsgeld', 'Urlaubsgeld! Du erhältst 100$.', 100) , 
                        JederSpielerSchenktDir('Geburtstag', 'Du hast Geburtstag! Jeder Spieler schenkt dir 10$.', 10) , 
                        BekommeGeld('Krankenhausgebühren', 'Krankenhausgebühren. Du zahlst 100$.', -100) , 
                        BekommeGeld('Schulgeld', 'Zahle Schulgeld: 50$.', -50)  , 
                        BekommeGeld('Arztkosten', 'Arztkosten. Zahle 50$.', -50) , 
                        Renovieren('Strassenausbesserungen', 'Kosten für Strassenausbesserungen! Zahle: 40$ pro Haus, 115$ pro Hotel.', 40, 115) , 
                        ZieheAufKarte('Rücke auf Los', 'Rücke vor bis auf Los. (Ziehe 200$ ein.)', 'los') , 
                        GefaengnisKarte() , 
                        Gefaengnisfreikarte()]
        super().__init__(kartenliste)
        