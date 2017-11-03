import os, xlrd
from random import randrange
################################ header ###################################
def header():
	try:
		print("")
		print("**************************************************************************************")
		print("+                                                                                    +")
		print("+      88888888888  888    888     8888888888      88888         888888888           +")
		print("+      8888888888   888    888    888    888      888 888        888     88          +")
		print("+      8888         888    888    888            888   888       888    88           +")
		print("+      8888         888    888   888            888     888      8888888>            +")
		print("+      888888888    888    888   888           8888888888888     888    88           +")
		print("+      8888         8888888888  888    888   888          888    888     88          +")
		print("+      8888          88888888   8888888888  88888        88888  8888888888    V1.0   +")
		print("+                                                                                    +")
		print("**************************************************************************************")
		print("")
	except Exception:
		print("Fehler in Funktion header()!")
		sys.exit()
################################ Dateien auflisten ###################################
def welcheDatei():
	global exl_datei
	global list_dir

	try:
		list_dir = os.listdir("data")
		print("----------------------------------    Excel auswählen    -----------------------------")
		print(*list_dir)
		print("")
		exl_datei = input("Welche Datei?: ")
	except Exception:
		print("Fehler in Funktion welcheDatei()!")
		sys.exit()
################################ Excel Seite wählen ###################################
def welchesSheet():
	global exl_sheet
	global sheet_names
	global workb

	try:
		file_path = "data/"+exl_datei
		wb = xlrd.open_workbook(file_path)
		workb = wb.sheet_by_index(0)
		sheet_names = wb.sheet_names()

		# Excel Sheet bzw. Seite auswählen
		print("")
		print("-------------------------------    Exel Sheets/Seiten    -----------------------------")
		print(' | ' . join(sheet_names))
		print("")
		exl_sheet = input("Welches Thema?: ")
	except Exception:
		print("Fehler in Funktion welchesSheet!()")
		sys.exit()
################################ excel einlesen ###################################
def readExel():
	global data
	data = [[workb.cell_value(r, c) for c in range(workb.ncols)] for r in range(workb.nrows)]
################################ Spalte wählen #####################################
def spWaehlen():
	global sprache
	try:
		sprache = int(input("1) Deutsch,  2) Englisch oder 3) Beenden: "))
	except Exception:
		print("Fehler in der Sprachauswahl!")
################################ Auswahl generell #####################################
# text und text2 sind Ausgabefelder, todo ist ein Eingabetext der übernommen wird
def auswahlInt(text, text2, todo):
	global auswahl
	try:
		print("")
		print(text)
		print(text2)
		print("")
		auswahl = input(todo)
		if auswahl.isalpha() == True:
			print("Ist String: "+auswahl)
			auswahl = str(auswahl)
		else:
			print("Ist Int: "+auswahl)
			auswahl = int(auswahl)
			if auswahl == 1:
				print("Auswahl wurde zu Integer Umgewandelt!")
	except:
		print("Fehler in der generellen Auswahl!")