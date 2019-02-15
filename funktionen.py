# -*- coding: utf-8 -*-
import sys
import xlrd
from random import randrange

# -------------------------------- header --------------------------------
def header():
    try:
        print("")
        print("**************************************************************************************")
        print("+                                                                                    +")
        print("+                              FUCAB VocabelReader V1.2                              +")
        print("+     Liest zwei Spalten einer Excel-Datei ein und gibt zufällig eine Zelle aus.     +")
        print("+                                                                                    +")
        print("**************************************************************************************")
        print("")
    except ValueError:
        print("Fehler in Funktion header()!")
        sys.exit()
# -------------------------------- Auswahl generell --------------------------------
# text und text2 sind Ausgabefelder, todo ist der Text für die Eingabe (input())

auswahl = None
data = None

def auswahlInt(text, text2, todo):
    global auswahl
    try:
        if text == "":
            auswahl = input(todo)
            print(text)
        elif text2 == "":
            auswahl = input(todo)
            print("")
        else:
            print("")
            print(text)
            print (text2)
            print("")
            auswahl = input(todo)
        #if auswahl.isdigit():
            #print("Nummer " + auswahl + " wurde ausgewählt")
            #auswahl = int(auswahl)
            # print("Auswahl wurde zu Integer Umgewandelt!")
        #else:
            #print("Auswahl: " + auswahl)
    except ValueError:
        print("Fehler in der generellen Auswahl!")
        sys.exit()
# -------------------------------- Excel Sheets / Seiten anzeigen --------------------------------
def excelSheet():
    global workb
    try:
        file_path = "excel/" + auswahl
        wb = xlrd.open_workbook(file_path)
        workb = wb.sheet_by_index(0)
        sheet_names = wb.sheet_names()

        return sheet_names
    except ValueError:
        print("Fehlerhafte Eingabe!")
        sys.exit()
# -------------------------------- Excel Daten einlesen --------------------------------
def readExel():
    global data
    data = [[workb.cell_value(r, c) for c in range(workb.ncols)] for r in range(workb.nrows)]
    return data
# -------------------------------- Zufallsvokabel --------------------------------
def zufall(x):
  global zufall_var
  global txt_translate
  zufall_var = randrange(0, len(readExel()))
  #zuffallswort = 0
  zuffallswort = str(data[zufall_var][x])
  txt_translate = "Gib bitte die Übersetzung von | " +zuffallswort+ " | ein."
  trenner(txt_translate)
  print(txt_translate)
  trenner(txt_translate)
# -------------------------------- Auflösung --------------------------------
def aufloesung():
    txt_aufl = "   " + data[zufall_var][0] + " - bedeutet - " + data[zufall_var][1]
    trenner(txt_aufl)
    print(txt_aufl)
    trenner(txt_aufl)
# -------------------------------- Trenner --------------------------------
def trenner(satz_laenge):
  for i in satz_laenge:
    print("-", end='')
  print("-----")
