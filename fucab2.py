import os
import pandas as pd
import xlrd

file_path = "data/vokabeln-englisch.xlsx"
wb = xlrd.open_workbook(file_path)
sheet_names = wb.sheet_names()

cwd = os.getcwd()
print("")
print("---------------Ordner Pfad------------------------")
print(cwd)
print("")
print("---------------Inhalt des Ordners-----------------")
list_dir = os.listdir("data")
print(*list_dir)
exl_datei = input("Welche Datei?: ")
print("")
print("---------------Exel Sheets/Seiten-----------------")
print(' | ' . join(sheet_names))
print("")
exl_sheet = input("Welches Thema?: ")