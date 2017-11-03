import sys
import os
import threading
import pandas as pd
import xlrd
from random import choice
from random import randrange

list_dir = os.listdir("data")

# Datei auswählen
print("-------------------------------Inhalt des Ordners-----------------")
print(*list_dir)
print("")

exl_datei = input("Welche Datei?: ")

if exl_datei in list_dir:
	file_path = "data/"+exl_datei
	wb = xlrd.open_workbook(file_path)
	workb = wb.sheet_by_index(0)
	sheet_names = wb.sheet_names()

	# Excel Sheet bzw. Seite auswählen
	print("")
	print("-------------------------------Exel Sheets/Seiten-----------------")
	print(' | ' . join(sheet_names))
	print("")
	exl_sheet = input("Welches Thema?: ")
	if exl_sheet in sheet_names:
		print("Jo ist drinnen!")
	else:
		print("Sorry Bro, is nicht drinnen!")

	data = [[workb.cell_value(r, c) for c in range(workb.ncols)] for r in range(workb.nrows)]

	while True:
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

			sprache = int(input("1) Deutsch,  2) Englisch oder 3) Beenden: "))
			zufall = randrange(0, len(data))
			zuffallswort = 0

			if sprache <= 3:
				if sprache == 1:
					zuffallswort = str(data[zufall][1])
					print("\n")
					print("--------------------------------------------------------------")
					print("Gib bitte die Übersetzung von | " +zuffallswort+ " | ein.")
					print("--------------------------------------------------------------")
					print("\n")
				elif sprache == 2:
					zuffallswort = str(data[zufall][0])
					print("\n")
					print("--------------------------------------------------------------")
					print("Gib bitte die Übersetzung von | " +zuffallswort+ " | ein.")
					print("--------------------------------------------------------------")
					print("\n")
				elif sprache == 3:
					print("Programm wird beendet!")
					break
				elif sprache >= 4:
					print("test")

				auswahl = input("Drücke 1 für die Auflösung oder 2 für die Eingabe: ")

				if auswahl == "1":
					print("################################################################")
					print("   "+data[zufall][0]+ " - bedeutet - " +data[zufall][1])
					print("################################################################")
				else:
					eingabe = input("Übersetzung: ")

					if eingabe == data[zufall][0] or eingabe == data[zufall][1]:
						print("\n")
						print("################################################################")
						print("   "+eingabe+ " ist richtig!")
						print("################################################################")
						print("   "+data[zufall][0]+ " - bedeutet - " +data[zufall][1])
						print("################################################################")
					else:
						print("\n")
						print("################################################################")
						print("   "+eingabe+ " ist falsch oder falsch geschreieben!")
						print("################################################################")
						print("   "+data[zufall][0]+ " - bedeutet - " +data[zufall][1])
			elif sprache >=4:
				sprache = int(input("1) Deutsch,  2) Englisch oder 3) Beenden: "))
else:
	print("Datei nicht vorhanden!")