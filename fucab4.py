# -*- coding: utf-8 -*-
import sys, funktionen, os
from funktionen import auswahl

# from funktionen import auswahlInt

waehlen = "Bitte auswählen: "
list_dir = os.listdir("excel")

funktionen.header()
for dateien in list_dir:
    if not (dateien.endswith(".xlsx") or dateien.endswith(".xls")):
        print("Datei ist keine Excel-Datei!")
    else:
        funktionen.auswahlInt("-------Inhalt des Ordners------", list_dir, "Welche Datei?: ")

        sheet_names = funktionen.excelSheet()
        sheet_mit_style = ' | '.join(sheet_names)
        funktionen.auswahlInt("-------Seite / Sheet (Thema)---", sheet_mit_style, waehlen)
        funktionen.readExel()
        funktionen.auswahlInt("-------Spalte Wählen (Sprache)-", "1) Erste Spalte 2) Zweite Spalte 3) Beenden", waehlen)
        if funktionen.auswahl == "1":
            funktionen.zufall(1)
            funktionen.aufloesung()
        elif funktionen.auswahl == "2":
            print("Zahl 2")
            funktionen.zufall(0)
            funktionen.aufloesung()
        elif funktionen.auswahl == "3":
            funktionen.aufloesung()
            sys.exit()
        else:
            print("Auswahl existiert nicht!")
            sys.exit()