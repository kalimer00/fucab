# -*- coding: utf-8 -*-
import sys, funktionen, os
#from funktionen import auswahl

waehlen = "Bitte auswählen: "
trenner = "-----------"
list_dir = os.listdir("excel")

funktionen.header()
for dateien in list_dir:
    if not (dateien.endswith(".xlsx") or dateien.endswith(".xls")):
        print("Datei ist keine Excel-Datei!")
    else:
        funktionen.auswahlInt(trenner + " Inhalt des Ordners ------" + trenner, list_dir, "Welche Datei?: ")
        sheet_names = funktionen.excelSheet()
        sheet_mit_style = ' | '.join(sheet_names)
        funktionen.auswahlInt(trenner + " Seite / Sheet (Thema) ---" + trenner, sheet_mit_style, waehlen)
        funktionen.readExel()
        while True:
            funktionen.auswahlInt(trenner + " Spalte Wählen (Sprache) -" + trenner, "1) Erste Spalte 2) Zweite Spalte 3) Beenden", waehlen)
            if funktionen.auswahl == "1":
                funktionen.zufall(1)
                print("1) Für Auflösung oder gib die ", end='')
                funktionen.auswahlInt("","","Übersetzung: ")
                if funktionen.auswahl == "1":
                    print("   " + funktionen.data[funktionen.zufall_var][0] + " - bedeutet - " +funktionen.data[funktionen.zufall_var][1])
                else:
                    if funktionen.auswahl == funktionen.data[funktionen.zufall_var][0] or funktionen.auswahl == funktionen.data[funktionen.zufall_var][1]:
                        print("   " +funktionen.auswahl+ " ist richtig!")
                        funktionen.aufloesung()
                    else:
                        print("   " +funktionen.auswahl+ " ist falsch oder falsch geschreieben!")
                        funktionen.aufloesung()

            elif funktionen.auswahl == "2":
                funktionen.zufall(0)
                print("1) Für Auflösung oder gib die ", end ='')
                funktionen.auswahlInt("","","Übersetzung: ")
                if funktionen.auswahl == "1":
                    print("   " + funktionen.data[funktionen.zufall_var][0] + " - bedeutet - " +funktionen.data[funktionen.zufall_var][1])
                else:
                    if funktionen.auswahl == funktionen.data[funktionen.zufall_var][0] or funktionen.auswahl == funktionen.data[funktionen.zufall_var][1]:
                        print("   " +funktionen.auswahl+ " ist richtig!")
                        funktionen.aufloesung()
                    else:
                        print("   " +funktionen.auswahl+ " ist falsch oder falsch geschreieben!")
                        funktionen.aufloesung()
            elif funktionen.auswahl == "3":
                sys.exit()
            else:
                print("Auswahl existiert nicht!\nProgramm wird beendet!")
                break
                sys.exit()
