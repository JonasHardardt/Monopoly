from kartenstapel import Kartenstapel
from karten2 import *

class Ereignisstapel(Kartenstapel):
    def __init__(self):
        kartenliste = [BekommeGeld('Bausparvertrag', 'Dein Bausparvertrag wird fällig. Du erhältst 150$.', 150) , 
                        BekommeGeld('Dividende', 'Die Bank zahlt dir eine Dividende von 50$.', 50) , 
                        BekommeGeld('Strafzettel', 'Strafzettel! Zahle 15$.',-15) , 
                        ZahleJedemSpieler('Wahl zum Vorstand', 'Du bist zum Vorstand gewählt worden. Zahle jedem Spieler 50$.', 50) , 
                        Renovieren('Häuser renovieren', 'Du lässt deine Häuser renovieren. Zahle: 25$ pro Haus, 100$ pro Hotel.', 25, 100) , 
                        ZieheAufKarte('Ausflug zum Südbahnhof', 'Mache einen Ausflug zum Südbahnhof. Wenn du über Los kommst, ziehe 200$ ein.', 'suedbahnhof') , 
                        ZieheAufKarte('Seestraße', 'Rücke vor bis zur Seestraße. Wenn du über Los kommst, ziehe 200$ ein.', 'seestrasse') , 
                        ZieheAufKarte('Rücke auf Los', 'Rücke vor bis auf Los. Ziehe 200$ ein.', 'los') , 
                        ZieheAufKarte('Opernplatz', 'Rücke vor bis zum Opernplatz. Wenn du über Los kommst, ziehe 200$ ein.', 'opernplatz') , 
                        ZieheAufKarte('Schlossallee', 'Rücke vor bis zur Schlossallee.', 'schlossallee') , 
                        RueckeUm('', 'Gehe 3 Felder zurück.', -3) , 
                        ZieheZumNaechsten('Nächstes Werk', 'Rücke vor bis zum nächsten Werk. Wird die Würfel und zahle dem Eigentümer den zehnfachen Betrag deines Würfelergebnisses. Wenn das Werk noch niemandem gehört, kannst du es von der Bank kaufen.', 'werk') , 
                        ZieheZumNaechsten('Nächster Bahnhof', 'Rücke vor bis zum nächsten Bahnhof. Der Eigentümer erhält das Doppelte der normalen Miete. Wenn der Bahnhof noch niemandem gehört, kannst du ihn von der Bank kaufen.', 'bahnhof') , 
                        ZieheZumNaechsten('Nächster Bahnhof', 'Rücke vor bis zum nächsten Bahnhof. Der Eigentümer erhält das Doppelte der normalen Miete. Wenn der Bahnhof noch niemandem gehört, kannst du ihn von der Bank kaufen.', 'bahnhof'),                           
                        GefaengnisKarte() , 
                        Gefaengnisfreikarte()]
        super().__init__(kartenliste)
        
    