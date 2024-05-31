from tkinter import *
import tkinter as tk
from time import sleep
from random import randint

class GUI(object):
    def __init__(self, pSpm):
        self.spm = pSpm
        self.kuerzel = []
        self.root = Tk()
        self.root.title('Monopoly')
        self.root.geometry('900x901')
        self.bg = PhotoImage(file = "Bilder\Spielplan_deutsch2.gif") 
        self.background = Label( self.root, image = self.bg) 
        self.background.place(x = 0, y = 0)
        def buttonStartClick():
            self.neuesFenster.quit()
            self.neuesFenster.destroy()
            self.abfrageAnzahlSpieler()
        # Neues Fenster öffnen
        self.neuesFenster = Toplevel()
        self.neuesFenster.title('Start')
        self.neuesFenster.geometry('300x200')
        # Label mit der Fehlermeldung
        self.text = Label(master = self.neuesFenster,
                            text ='Möchten Sie das Spiel starten?')
        self.text.pack(pady = 50)
        # Button zum Schließen des Fensters
        self.buttonStart = Button(master = self.neuesFenster, text='Start',
                          command = buttonStartClick)
        self.buttonStart.pack()
        
        
    def setSpm(self, pSpm):
        self.spm = pSpm
    
    def abfrageAnzahlSpieler(self):
        #self.spm.erzeugeSpieler(2, ['J', 'H'], self.spm)
        anzahl = 0
        neuesFenster = Toplevel()
        neuesFenster.title('Anzahl Spieler')
        neuesFenster.geometry('300x200')
        text = Label(master = neuesFenster,
                            text = 'Wie viele Spieler möchten mitspielen?')
        text.pack(pady = 30)
        entryZahl1 = Entry(master = neuesFenster, bg='white', width='4')
        entryZahl1.pack(pady = 10)
        def buttonOkClick():
            anzahl = int(entryZahl1.get())
            neuesFenster.quit()
            neuesFenster.destroy()
            self.abfrageKuerzel(anzahl)
        buttonOk = Button(master = neuesFenster, text='Ok',
                          command = buttonOkClick)
        buttonOk.pack()
        neuesFenster.mainloop()
        
    def abfrageKuerzel(self, pAnzahl):
        if pAnzahl == 0:
            self.spm.erzeugeSpieler(len(self.kuerzel), self.kuerzel, self.spm)
            pass
        else:
            neuesFenster = Toplevel()
            text = Label(master = neuesFenster,
                        text='Welches Kürzel soll der '+ str(len(self.kuerzel)+1) + '. Spieler haben?')
            text.pack(pady = 30)
            entryKuerzel = Entry(master = neuesFenster, bg='white', width='4')
            entryKuerzel.pack(pady = 10)
            def buttonOkClick():
                self.kuerzel += [entryKuerzel.get()]
                neuesFenster.quit()
                neuesFenster.destroy()
                self.abfrageKuerzel(pAnzahl-1)
            buttonOk = Button(master = neuesFenster, text='Ok',
                      command = buttonOkClick)
            buttonOk.pack(pady = 10)
            neuesFenster.mainloop()
    
    def wuerfeln(self):
#         global augenzahl1
#         global augenzahl2
#         global augenzahl3
#         global augenzahl4
#         global augenzahl5
#         global augenzahl6
        augenzahl1 = PhotoImage(file='Bilder\A1.gif')
        augenzahl2 = PhotoImage(file='Bilder\A2.gif')
        augenzahl3 = PhotoImage(file='Bilder\A3.gif')
        augenzahl4 = PhotoImage(file='Bilder\A4.gif')
        augenzahl5 = PhotoImage(file='Bilder\A5.gif')
        augenzahl6 = PhotoImage(file='Bilder\A6.gif')
        global augenzahlWuerfel1
        global augenzahlWuerfel2
        augenzahlWuerfel1 = 0
        augenzahlWuerfel2 = 0
        
        def buttonWuerfelnClick():
            zeit = 10
            #for i in range(1):
            augenzahl1 = PhotoImage(file='Bilder\A1.gif')
            augenzahl2 = PhotoImage(file='Bilder\A2.gif')
            augenzahl3 = PhotoImage(file='Bilder\A3.gif')
            augenzahl4 = PhotoImage(file='Bilder\A4.gif')
            augenzahl5 = PhotoImage(file='Bilder\A5.gif')
            augenzahl6 = PhotoImage(file='Bilder\A6.gif')
            global augenzahlWuerfel1
            global augenzahlWuerfel2
            global labelWuerfel1
            global labelWuerfel2
            augenzahlWuerfel1 = randint(1,6)
            
            if augenzahlWuerfel1 == 1:
                 labelWuerfel1.config(image = augenzahl1)
            elif augenzahlWuerfel1 == 2:
                 labelWuerfel1.config(image = augenzahl2)
            elif augenzahlWuerfel1 == 3:
                 labelWuerfel1.config(image = augenzahl3)
            elif augenzahlWuerfel1 == 4:
                 labelWuerfel1.config(image = augenzahl4)
            elif augenzahlWuerfel1 == 5:
                 labelWuerfel1.config(image = augenzahl5)
            elif augenzahlWuerfel1 == 6:
                 labelWuerfel1.config(image = augenzahl6)
                 
            augenzahlWuerfel2 = randint(1,6)
            if augenzahlWuerfel2 == 1:
                 labelWuerfel2.config(image = augenzahl1)
            elif augenzahlWuerfel2 == 2:
                 labelWuerfel2.config(image = augenzahl2)
            elif augenzahlWuerfel2 == 3:
                 labelWuerfel2.config(image = augenzahl3)
            elif augenzahlWuerfel2 == 4:
                 labelWuerfel2.config(image = augenzahl4)
            elif augenzahlWuerfel2 == 5:
                 labelWuerfel2.config(image = augenzahl5)
            elif augenzahlWuerfel2 == 6:
                 labelWuerfel2.config(image = augenzahl6)
            sleep(zeit/1000)
            zeit += 25
            sleep(0.5)
            neuesFenster.quit()
            neuesFenster.destroy()
            
            
        neuesFenster = Toplevel()
        global labelWuerfel1
        global labelWuerfel2
        labelWuerfel1 = Label(master = neuesFenster, image = augenzahl1)
        labelWuerfel1.pack(side = 'left', padx = 10, pady = 10)

        labelWuerfel2 = Label(master = neuesFenster, image = augenzahl1)
        labelWuerfel2.pack(side = 'right', padx = 10, pady = 10)
        
        buttonWuerfeln = Button(master = neuesFenster, text = 'würfeln', command = buttonWuerfelnClick)
        buttonWuerfeln.pack(side = 'bottom')
        neuesFenster.mainloop()
        return [augenzahlWuerfel1, augenzahlWuerfel2]
        
            
    def abfrageKaufen(self, pSpieler, pKarte):
        #return 'ja'
        global entscheidung
        global spieler
        spieler = pSpieler
        entscheidung = ''
        neuesFenster = Toplevel()
        neuesFenster.title('Abfrage Kaufen')
        #neuesFenster.geometry('300x200')
        text = Label(master = neuesFenster,
                            text = str(pSpieler.getKuerzel()) + ' befindet sich auf:\n '+ str(pKarte.getName()) + '\n Möchtest du diese Karte für ' + str(pKarte.getKaufpreis()) + ' $ kaufen?')
        text.pack(pady = 30)
        def buttonJaClick():
            global entscheidung
            entscheidung = 'ja'
            neuesFenster.quit()
            neuesFenster.destroy()
        def buttonNeinClick():
            global entscheidung
            entscheidung = 'nein'
            neuesFenster.quit()
            neuesFenster.destroy()
        def buttonInfoClick():
            global spieler
            self.mitteilungInfo(spieler)
            
        buttonJa = Button(master = neuesFenster, text='Ja',
                          command = buttonJaClick)
        buttonNein = Button(master = neuesFenster, text='Nein',
                          command = buttonNeinClick)
        
        buttonJa.place(width = 100)
        buttonJa.pack(side = 'left', padx = 10)
        buttonNein.pack(side = 'right', padx = 10)
        buttonInfo = Button(master = neuesFenster, text='Info',
                          command = buttonInfoClick)
        buttonInfo.pack(side = 'right', padx = 10)
        neuesFenster.mainloop()
        return entscheidung
    
    def abfrageEndeDerRunde(self, pSpieler, pZustand):
        neuesFenster = Toplevel()
        neuesFenster.title('Ende der Runde')
        #neuesFenster.geometry('500x500')
        text = Label(master = neuesFenster,
                            text = 'Möchten Sie noch Häuser bauen/abbauen,\n Karten mit Hypotheken belasten oder diese wieder aufheben?')
        text.pack(pady = 30)
        global spieler
        spieler = pSpieler
        def buttonHaeuserBauenClick():
            self.haeuserBau(pSpieler)
        
        def buttonHypothekBelastenClick():
            self.hypothekAufnehmen(pSpieler)
        
        def buttonHypothekAufhebenClick():
            self.hypothekAufloesen(pSpieler)
        
        def buttonNaechsterSpielerClick():
            neuesFenster.quit()
            neuesFenster.destroy()
        
        def buttonInfoClick():
            global spieler
            self.mitteilungInfo(spieler)
            
        def buttonTauschClick():
            self.tauschen(pSpieler)
        
        def buttonAufhoerenClick():
            self.spm.spielerAbmelden(pSpieler)
        
        def buttonWeitermachenClick():
            if pSpieler.getGeld() >= 0:
                neuesFenster.quit()
                neuesFenster.destroy() 
            
        buttonHaeuserBauen = Button(master = neuesFenster, text='Häuser bauen',
                          command = buttonHaeuserBauenClick, state = tk.DISABLED)
        buttonHaeuserBauen.pack(side = 'left', padx = 10)
        
        
        buttonHypothekBelasten = Button(master = neuesFenster, text='Hypothek belasten',
                          command = buttonHypothekBelastenClick, )
        buttonHypothekBelasten.pack(side = 'left', padx = 10)
        
        buttonHypothekAufheben = Button(master = neuesFenster, text='Hypothek aufheben',
                          command = buttonHypothekAufhebenClick, state = tk.DISABLED)
        buttonHypothekAufheben.pack(side = 'left', padx = 10)
        
        buttonTausch = Button(master = neuesFenster, text='Tausch',
                          command = buttonTauschClick)
        buttonTausch.pack(side = 'left', padx = 10)
        
        buttonInfo = Button(master = neuesFenster, text='Info',
                          command = buttonInfoClick)
        buttonInfo.pack(side = 'left', padx = 10)
        
        buttonNaechsterSpieler = Button(master = neuesFenster, text='Nächster Spieler',
                          command = buttonNaechsterSpielerClick)
        buttonNaechsterSpieler.pack(side = 'left')
        
        
        if pZustand == 'geld':
            buttonNaechsterSpieler['state'] = tk.DISABLED
            buttonHypothekAufheben['state'] = tk.DISABLED
            buttonAufhoeren = Button(master = neuesFenster, text='Aufhören',
                          command = buttonAufhoerenClick)
            buttonAufhoeren.pack(side = 'left')
            buttonWeitermachen = Button(master = neuesFenster, text='Weitermachen',
                          command = buttonWeitermachenClick)
            buttonWeitermachen.pack(side = 'left')
        if len(pSpieler.getKarten()) > 0:
            for karte in pSpieler.getKarten():
                if karte.getStrasse() == True:
                    buttonHaeuserBauen['state'] = tk.NORMAL
                if karte.getHypothek() == True:
                    buttonHypothekAufheben['state'] = tk.NORMAL
        neuesFenster.mainloop()
        
        
    def abfrageGefaengnis(self, pSpieler):
        global entscheidung
        entscheidung = ''
        neuesFenster = Toplevel()
        neuesFenster.title('Abfrage Gefängnis')
        #neuesFenster.geometry('300x200')
        text = Label(master = neuesFenster,
                            text = 'Sie sind im Gefängnis. Was möchten Sie machen?')
        text.pack(pady = 30)
        def buttonFreiKarteClick():
            entscheidung = 'gefaengnisFreiKarte'
            neuesFenster.quit()
            neuesFenster.destroy()
            
        def buttonWuerfelnClick():
            entscheidung = 'wuerfeln'
            neuesFenster.quit()
            neuesFenster.destroy()
            
        def buttonBezahlenClick():
            entscheidung = 'bezahlen'
            neuesFenster.quit()
            neuesFenster.destroy()
            
        
        buttonFreiKarte = Button(master = neuesFenster, text='Gefängnisfreikarte verwenden',
                          command = buttonFreiKarteClick)
        buttonFreiKarte.pack(side = 'left')
        
        buttonWuerfeln = Button(master = neuesFenster, text='3 mal versuchen einen Pasch zu würfeln',
                          command = buttonWuerfelnClick)
        buttonWuerfeln.pack(side = 'left')
        
        buttonBezahlen = Button(master = neuesFenster, text='50$ zahlen',
                          command = buttonBezahlenClick)
        buttonBezahlen.pack(side = 'left')
        
        neuesFenster.mainloop()
        return entscheidung
    
    def mitteilungInfo(self, pSpieler):
        neuesFenster = Toplevel()
        neuesFenster.title('Info')
        #neuesFenster.geometry('300x200')
        text = Label(master = neuesFenster,
                            text = 'Info:\n Ihr Kontostand: ' + str(pSpieler.getGeld()) )
        text.pack(pady = 30)
        def buttonSchliessenClick():
            neuesFenster.quit()
            neuesFenster.destroy()
        def buttonStrassenClick():
            self.infoStrassen(pSpieler)
        def buttonHypothekClick():
            self.infoHypothek(pSpieler)
#         def buttenHaeuserClick():
#             self.infoHaeuser(pSpieler)
            
        buttonStrassen = Button(master = neuesFenster, text='Info Strassen',
                          command = buttonStrassenClick)
        buttonStrassen.pack(side = 'left', padx = 10)
        
        buttonHypothek = Button(master = neuesFenster, text='Info Hypothek',
                          command = buttonHypothekClick)
        buttonHypothek.pack(side = 'left', padx = 10)
        
#         buttonHaeuser = Button(master = neuesFenster, text='Info Häuser',
#                           command = buttenHaeuserClick)
#         buttonHaeuser.pack(side = 'left', padx = 10)
#         
        buttonSchliessen = Button(master = neuesFenster, text='schließen',
                          command = buttonSchliessenClick)
        buttonSchliessen.pack(side = 'left', padx = 10)
        neuesFenster.mainloop()
    
    def infoStrassen(self, pSpieler):
        strassen = []
        for karte in pSpieler.getKarten():
            if karte.getStrasse() == True:
                strassen += [karte.getFarbe()]
        neuesFenster = Toplevel()
        neuesFenster.title('Info Straßen')
        neuesFenster.geometry('300x200')
        text = Label(master = neuesFenster,
                            text = 'Sie besitzen folgende Strassen:\n' + str(strassen) )
        text.pack(pady = 30)
        def buttonOkClick():
            neuesFenster.quit()
            neuesFenster.destroy()
        
        buttonOk = Button(master = neuesFenster, text='Ok',
                          command = buttonOkClick)
        buttonOk.pack(side = 'left', padx = 40)
        neuesFenster.mainloop()
    
#     def infoHypothek(self, pSpieler):
#         pass
    
#     def infoHaeuser(self, pSpieler):
#         pass
    
    def mitteilungKarte(self, pKarte):
        neuesFenster = Toplevel()
        neuesFenster.title(str(pKarte.getName()))
        #neuesFenster.geometry('300x200')
        text = Label(master = neuesFenster,
                            text = str(pKarte.getText()) )
        text.pack(pady = 30)
        def buttonOkClick():
            neuesFenster.quit()
            neuesFenster.destroy()
        
        buttonOk = Button(master = neuesFenster, text='Ok',
                          command = buttonOkClick)
        buttonOk.pack(side = 'left', padx = 40)
        neuesFenster.mainloop()
    
    def mitteilungText(self, pText):
        neuesFenster = Toplevel()
        neuesFenster.title('Mitteilung')
        #neuesFenster.geometry('300x200')
        text = Label(master = neuesFenster,
                            text = pText )
        text.pack(pady = 30)
        def buttonOkClick():
            neuesFenster.quit()
            neuesFenster.destroy()
        
        buttonOk = Button(master = neuesFenster, text='Ok',
                          command = buttonOkClick)
        buttonOk.pack(side = 'left', padx = 40)
        neuesFenster.mainloop()
    
    def mitteilungMiete(self, pMiete):
        neuesFenster = Toplevel()
        neuesFenster.title('Miete')
        #neuesFenster.geometry('300x200')
        text = Label(master = neuesFenster,
                            text = 'Sie müssen ' + str(pMiete) + '$ Miete zahlen.' )
        text.pack(pady = 30)
        def buttonOkClick():
            neuesFenster.quit()
            neuesFenster.destroy()
        
        buttonOk = Button(master = neuesFenster, text='Ok',
                          command = buttonOkClick)
        buttonOk.pack(side = 'left', padx = 40)
        neuesFenster.mainloop()
        
    def haeuserBau(self, pSpieler):
        neuesFenster = Toplevel()
        neuesFenster.title('Häuser bauen')
        #neuesFenster.geometry('300x200')
        text = Label(master = neuesFenster,
                            text = 'Häuser bauen' )
        text.pack(pady = 30)
        def buttonOkClick():
            neuesFenster.quit()
            neuesFenster.destroy()
        def braun():
            self.zweiHaeuser(pSpieler, 'braun', pSpieler.getBraun())
        def hellblau():
            self.dreiHaeuser(pSpieler, 'hellblau', pSpieler.getHellblau())
        def pink():
            self.dreiHaeuser(pSpieler, 'orange', pSpieler.getPink())
        def orange():
            self.dreiHaeuser(pSpieler, 'orange', pSpieler.getOrange())
        def rot():
            self.dreiHaeuser(pSpieler, 'rot', pSpieler.getRot())
        def gelb():
            self.dreiHaeuser(pSpieler, 'gelb', pSpieler.getGelb())
        def gruen():
            self.dreiHaeuser(pSpieler, 'gruen', pSpieler.getGruen())
        def dunkelblau():
            self.zweiHaeuser(pSpieler, 'dunkelblau', pSpieler.getDunkelblau())
        if len(pSpieler.getBraun()) == 2:
            buttonBraun = Button(master = neuesFenster, text = 'braun', command = braun)
            buttonBraun.pack(padx = 10, side = 'left')
        if len(pSpieler.getHellblau()) == 3:
            buttonHellblau = Button(master = neuesFenster, text = 'hellblau', command = hellblau)
            buttonHellblau.pack(padx = 10, side = 'left')
        if len(pSpieler.getPink()) == 3:
            buttonPink = Button(master = neuesFenster, text = 'pink', command = pink)
            buttonPink.pack(padx = 10, side = 'left')
        if len(pSpieler.getOrange()) == 3:
            buttonOrange = Button(master = neuesFenster, text = 'orange', command = orange)
            buttonOrange.pack(padx = 10, side = 'left')
        if len(pSpieler.getRot()) == 3:
            buttonRot = Button(master = neuesFenster, text = 'rot', command = rot)
            buttonRot.pack(padx = 10, side = 'left')
        if len(pSpieler.getGelb()) == 3:
            buttonGelb = Button(master = neuesFenster, text = 'gelb', command = gelb)
            buttonGelb.pack(padx = 10, side = 'left')
        if len(pSpieler.getGruen()) == 3:
            buttonGruen = Button(master = neuesFenster, text = 'gruen', command = gruen)
            buttonGruen.pack(padx = 10, side = 'left')
        if len(pSpieler.getDunkelblau()) == 2:
            buttonDunkelblau = Button(master = neuesFenster, text = 'dunkelblau', command = dunkelblau)
            buttonDunkelblau.pack(padx = 10, side = 'left')
        buttonOk = Button(master = neuesFenster, text='Ok',
                          command = buttonOkClick)
        buttonOk.pack()
        neuesFenster.mainloop()
        
    def zweiHaeuser(self, pSpieler, farbe, karten):
        farbe = ['braun', 'dunkelblau']
        neuesFenster = Toplevel()
        neuesFenster.title('Häuser kaufen')
        #neuesFenster.geometry('300x200')
        text = Label(master = neuesFenster,
                            text = 'Häuser kaufen' )
        text.grid(row = 0, column = 0)
        label1 = Label(master = neuesFenster,
                            text = str(karten[0].getName())+ ': ' + str(karten[0].getHaeuser()) )
        label1.grid(row = 1, column = 0)
        label2 = Label(master = neuesFenster,
                            text = str(karten[1].getName())+ ': ' + str(karten[1].getHaeuser()) )
        label2.grid(row = 2, column = 0)
        def buttonOkClick():
            neuesFenster.quit()
            neuesFenster.destroy()
        def button1Click():
            karten[0].hausKaufen(1)
            if abs(karten[1].getHaeuser() - karten[0].getHaeuser()) > 1:
                karten[1].hausKaufen(1)
            label1.config(text = str(karten[0].getName())+ ': ' + str(karten[0].getHaeuser()))
            label2.config(text = str(karten[1].getName())+ ': ' + str(karten[1].getHaeuser()))
        def button2Click():
            karten[1].hausKaufen(1)
            if abs(karten[1].getHaeuser() - karten[0].getHaeuser()) > 1:
                karten[0].hausKaufen(1)
            label1.config(text = str(karten[0].getName())+ ': ' + str(karten[0].getHaeuser()))
            label2.config(text = str(karten[1].getName())+ ': ' + str(karten[1].getHaeuser()))
        def button3Click():
            karten[1].hausVerkaufen(1)
            if abs(karten[1].getHaeuser() - karten[0].getHaeuser()) > 1:
                karten[0].hausVeraufen(1)
            label1.config(text = str(karten[0].getName())+ ': ' + str(karten[0].getHaeuser()))
            label2.config(text = str(karten[1].getName())+ ': ' + str(karten[1].getHaeuser()))
        def button4Click():
            karten[1].hausVerkaufen(1)
            if abs(karten[1].getHaeuser() - karten[0].getHaeuser()) > 1:
                karten[0].hausVerkaufen(1)
            label1.config(text = str(karten[0].getName())+ ': ' + str(karten[0].getHaeuser()))
            label2.config(text = str(karten[1].getName())+ ': ' + str(karten[1].getHaeuser()))
        button1 = Button(master = neuesFenster, text='+',
                          command = button1Click)
        button1.grid(row = 1, column = 1)
        button2 = Button(master = neuesFenster, text='+',
                          command = button2Click)
        button2.grid(row = 2, column = 1)
        button3 = Button(master = neuesFenster, text='-',
                          command = button3Click)
        button3.grid(row = 1, column = 2)
        button4 = Button(master = neuesFenster, text='-',
                          command = button4Click)
        button4.grid(row = 2, column = 2)
        buttonOk = Button(master = neuesFenster, text='Ok',
                          command = buttonOkClick)
        buttonOk.grid(row = 3, column = 0)
        neuesFenster.mainloop()
        
    def dreiHaeuser(self, pSpieler, farbe, karten):
        neuesFenster = Toplevel()
        neuesFenster.title('Häuser kaufen')
        #neuesFenster.geometry('300x200')
        text = Label(master = neuesFenster,
                            text = 'Häuser kaufen' )
        text.grid(row = 0, column = 0)
        label1 = Label(master = neuesFenster,
                            text = str(karten[0].getName())+ ': ' + str(karten[0].getHaeuser()) )
        label1.grid(row = 1, column = 0)
        label2 = Label(master = neuesFenster,
                            text = str(karten[1].getName())+ ': ' + str(karten[1].getHaeuser()) )
        label2.grid(row = 2, column = 0)
        label3 = Label(master = neuesFenster,
                            text = str(karten[2].getName())+ ': ' + str(karten[2].getHaeuser()) )
        label3.grid(row = 3, column = 0)
        def buttonOkClick():
            neuesFenster.quit()
            neuesFenster.destroy()
            
        def button1Click():
            if karten[0].getHaeuser() == 5:
                button1['state'] = tk.DISABLED
            karten[0].hausKaufen(1)
            if abs(karten[1].getHaeuser() - karten[0].getHaeuser()) > 1:
                karten[1].hausKaufen(1)
            if abs(karten[1].getHaeuser() - karten[2].getHaeuser()) > 1:
                karten[2].hausKaufen(1)
            label1.config(text = str(karten[0].getName())+ ': ' + str(karten[0].getHaeuser()))
            label2.config(text = str(karten[1].getName())+ ': ' + str(karten[1].getHaeuser()))
            label3.config(text = str(karten[2].getName())+ ': ' + str(karten[2].getHaeuser()))
            
        def button2Click():
            if karten[1].getHaeuser() == 5:
                button2['state'] = tk.DISABLED
            karten[1].hausKaufen(1)
            if abs(karten[1].getHaeuser() - karten[0].getHaeuser()) > 1:
                karten[0].hausKaufen(1)
            if abs(karten[1].getHaeuser() - karten[2].getHaeuser()) > 1:
                karten[2].hausKaufen(1)
            label1.config(text = str(karten[0].getName())+ ': ' + str(karten[0].getHaeuser()))
            label2.config(text = str(karten[1].getName())+ ': ' + str(karten[1].getHaeuser()))
            label3.config(text = str(karten[2].getName())+ ': ' + str(karten[2].getHaeuser()))
            
        def button3Click():
            if karten[2].getHaeuser() == 5:
                button3['state'] = tk.DISABLED
            karten[2].hausKaufen(1)
            if abs(karten[0].getHaeuser() - karten[2].getHaeuser()) > 1:
                karten[0].hausKaufen(1)
            if abs(karten[1].getHaeuser() - karten[2].getHaeuser()) > 1:
                karten[1].hausKaufen(1)
            label1.config(text = str(karten[0].getName())+ ': ' + str(karten[0].getHaeuser()))
            label2.config(text = str(karten[1].getName())+ ': ' + str(karten[1].getHaeuser()))
            label3.config(text = str(karten[2].getName())+ ': ' + str(karten[2].getHaeuser()))
            
        def button4Click():
            karten[0].hausVerkaufen(1)
            if abs(karten[1].getHaeuser() - karten[0].getHaeuser()) > 1:
                karten[1].hausVerkaufen(1)
            if abs(karten[1].getHaeuser() - karten[2].getHaeuser()) > 1:
                karten[2].hausVerkaufen(1)
            label1.config(text = str(karten[0].getName())+ ': ' + str(karten[0].getHaeuser()))
            label2.config(text = str(karten[1].getName())+ ': ' + str(karten[1].getHaeuser()))
            label3.config(text = str(karten[2].getName())+ ': ' + str(karten[2].getHaeuser()))
            
        def button5Click():
            karten[1].hausKaufen(1)
            if abs(karten[1].getHaeuser() - karten[0].getHaeuser()) > 1:
                karten[0].hausKaufen(1)
            if abs(karten[1].getHaeuser() - karten[2].getHaeuser()) > 1:
                karten[2].hausKaufen(1)
            label1.config(text = str(karten[0].getName())+ ': ' + str(karten[0].getHaeuser()))
            label2.config(text = str(karten[1].getName())+ ': ' + str(karten[1].getHaeuser()))
            label3.config(text = str(karten[2].getName())+ ': ' + str(karten[2].getHaeuser()))
            
        def button6Click():
            karten[2].hausVerkaufen(1)
            if abs(karten[0].getHaeuser() - karten[2].getHaeuser()) > 1:
                karten[0].hausVerkaufen(1)
            if abs(karten[1].getHaeuser() - karten[2].getHaeuser()) > 1:
                karten[1].hausVerkaufen(1)
            label1.config(text = str(karten[0].getName())+ ': ' + str(karten[0].getHaeuser()))
            label2.config(text = str(karten[1].getName())+ ': ' + str(karten[1].getHaeuser()))
            label3.config(text = str(karten[2].getName())+ ': ' + str(karten[2].getHaeuser()))
        
        button1 = Button(master = neuesFenster, text='+',
                          command = button1Click)
        button1.grid(row = 1, column = 1)
        button2 = Button(master = neuesFenster, text='+',
                          command = button2Click)
        button2.grid(row = 2, column = 1)
        button3 = Button(master = neuesFenster, text='+',
                          command = button3Click)
        button3.grid(row = 3, column = 1)
        button4 = Button(master = neuesFenster, text='-',
                          command = button4Click)
        button4.grid(row = 1, column = 2)
        button5 = Button(master = neuesFenster, text='-',
                          command = button5Click)
        button5.grid(row = 2, column = 2)
        button6 = Button(master = neuesFenster, text='-',
                          command = button6Click)
        button6.grid(row = 3, column = 2)
        buttonOk = Button(master = neuesFenster, text='Ok',
                          command = buttonOkClick)
        buttonOk.grid(row = 4, column = 0)
        neuesFenster.mainloop()
        
        
    def hypothekAufnehmen(self, pSpieler):
        neuesFenster = Toplevel()
        neuesFenster.title('Hypothek')
        #neuesFenster.geometry('300x200')
        text = Label(master = neuesFenster,
                            text = 'Hypothek' )
        text.pack(pady = 30)
        liste = []
        for karte in pSpieler.getKarten():
            liste += [karte.getName()]
        label1 = Label(master = neuesFenster,
                            text = 'Sie haben folgende Karten' + str(liste) )
        label1.pack()
        input1 = Entry(master = neuesFenster, bg='white', width='20')
        input1.pack()
        def buttonOkClick():
            neuesFenster.quit()
            neuesFenster.destroy()
        def buttonHypothekClick():
            kartennamen = input1.get()
            for karte in pSpieler.getKarten():
                if karte.getName() == kartennamen:
                    for karte2 in pSpieler.getKarten():
                        if karte.getFarbe() == karte2.getFarbe() and karte.getFarbe() != 'bahnhof' and karte.getFarbe() != 'werk':
                            karte2.hausVerkaufen(karte2.getHaeuser())
                    karte.setHypothek(True)
                    
                    
                    
        buttonOk = Button(master = neuesFenster, text='Ok',
                          command = buttonOkClick)
        
        buttonHypothek = Button(master = neuesFenster, text='Hypothek',
                          command = buttonHypothekClick)
        buttonHypothek.pack()
        buttonOk.pack()
        neuesFenster.mainloop()
        
        
        
    def hypothekAufloesen(self, pSpieler):
        neuesFenster = Toplevel()
        neuesFenster.title('Hypothek')
        #neuesFenster.geometry('300x200')
        text = Label(master = neuesFenster,
                            text = 'Hypothek' )
        text.pack(pady = 30)
        liste = []
        for karte in pSpieler.getKarten():
            if karte.getHypothek() == True:
                liste += [karte.getName()]
        label1 = Label(master = neuesFenster,
                            text = 'Sie haben folgende Karten mit Hypothek belastet' + str(liste) )
        label1.pack()
        input1 = Entry(master = neuesFenster, bg='white', width='20')
        input1.pack()
        def buttonOkClick():
            neuesFenster.quit()
            neuesFenster.destroy()
        def buttonHypothekClick():
            kartennamen = input1.get()
            for karte in pSpieler.getKarten():
                if karte.getName() == kartennamen:
                    karte.setHypothek(False)
                    
                    
                    
        buttonOk = Button(master = neuesFenster, text='Ok',
                          command = buttonOkClick)
        
        buttonHypothek = Button(master = neuesFenster, text='Hypothek',
                          command = buttonHypothekClick)
        buttonHypothek.pack()
        buttonOk.pack()
        neuesFenster.mainloop()
    
    def tauschen(self, pSpieler1):
        neuesFenster = Toplevel()
        neuesFenster.title('Tauschen')
        #neuesFenster.geometry('300x200')
        text = Label(master = neuesFenster,
                            text = 'Tauschen' )
        text.grid(row = 0)
        liste = []
        label1 = Label(master = neuesFenster,
                            text = 'Kuerzel Spieler 2:' )
        label1.grid(row = 1, column = 0)
        kuerzel2 = Entry(master = neuesFenster, bg='white', width='20')
        kuerzel2.grid(row = 1, column = 1)
        
        label2 = Label(master = neuesFenster,
                            text = 'Karte Spieler1:')
        label2.grid(row = 2, column = 0)
        karten1 = Entry(master = neuesFenster, bg='white', width='20')
        karten1.grid(row = 2, column = 1)
                       
        label3 = Label(master = neuesFenster,
                            text = 'Geld Spieler1:')
        label3.grid(row = 3, column = 0)
        geld1 = Entry(master = neuesFenster, bg='white', width='20')
        geld1.grid(row = 3, column = 1)
        
        label4 = Label(master = neuesFenster,
                            text = 'Karte Spieler2:')
        label4.grid(row = 4, column = 0)
        karten2 = Entry(master = neuesFenster, bg='white', width='20')
        karten2.grid(row = 4, column = 1)
        
        label5 = Label(master = neuesFenster,
                            text = 'Geld Spieler2:')
        label5.grid(row = 5, column = 0)
        geld2 = Entry(master = neuesFenster, bg='white', width='20')
        geld2.grid(row = 5, column = 1)
        
                       
        def buttonOkClick():
            neuesFenster.quit()
            neuesFenster.destroy()
        def buttonTauschClick():
            spieler2 = ''
            for spieler in self.spm.getSpieler():
                if spieler.getKuerzel() == kuerzel2.get():
                    spieler2 = spieler
            for karten in pSpieler1.getKarten():
                if karten.getName() == karten1.get():
                    karte1 = [karten]
            for karten in spieler2.getKarten():
                if karten.getName() == karten2.get():
                    karte2 = [karten]
            self.spm.tauschen(pSpieler1, spieler2, karte1, karte2, int(geld1.get()), int(geld2.get()))
            neuesFenster.quit()
            neuesFenster.destroy()
                    
        buttonOk = Button(master = neuesFenster, text='Ok',
                          command = buttonOkClick)
        
        buttonTausch = Button(master = neuesFenster, text='Tausch',
                          command = buttonTauschClick)
        buttonTausch.grid(row = 6, column = 0)
        buttonOk.grid(row = 6, column = 1)
        neuesFenster.mainloop()
    