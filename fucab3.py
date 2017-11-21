# coding=utf-8
# coding=utf-8
# coding=utf-8
# coding=utf-8
# coding=utf-8
import sys, funktionen, xlrd
from random import randrange
while True:
	################################ Header ###############################################
	funktionen.auswahlInt("fiken: ", "f asdf asf")
	print(funktionen.auswahl)
	funktionen.header()
	################################ Dateien wählen ####################################
	funktionen.welcheDatei()
	################################ Excel Seite / Sheet wählen ###################################
	if funktionen.exl_datei in funktionen.list_dir:
		funktionen.welchesSheet()
		if funktionen.exl_sheet in funktionen.sheet_names:
			################################ Spalte wählen #####################################
			funktionen.spWaehlen()
			funktionen.readExel()
			if funktionen.sprache <= 3:
				zufall = randrange(0, len(funktionen.data))
				zuffallswort = 0
				zuffallswort = str(funktionen.data[zufall][1])
				if funktionen.sprache == 1:
					print("\n")
					print("--------------------------------------------------------------")
					print("Gib bitte die Übersetzung von | " +zuffallswort+ " | ein.")
					print("--------------------------------------------------------------")
					print("\n")
				elif funktionen.sprache == 2:
					zuffallswort = str(funktionen.data[zufall][0])
					print("\n")
					print("--------------------------------------------------------------")
					print("Gib bitte die Übersetzung von | " +zuffallswort+ " | ein.")
					print("--------------------------------------------------------------")
					print("\n")
				elif funktionen.sprache == 3:
					print("Programm wird beendet!")
					sys.exit()
			elif funktionen.sprache >= 4:
				print("Programm wird beendet, Zahl zu hoch!")
				break
		else:
			print("Falsch geschrieben oder Seite/Sheet nicht vorhanden!\nProgramm wird beendet!")
			sys.exit()
	else:
		print("Falsch geschrieben oder Datei nicht vorhanden!\nProgramm wird beendet!")
		sys.exit()