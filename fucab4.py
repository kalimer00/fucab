import sys, funktionen, xlrd, os
from random import randrange
from funktionen import auswahlInt
list_dir = os.listdir("data")
funktionen.auswahlInt("-------Inhalt des Ordners------", *list_dir, "Welche Datei?: ")