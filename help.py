"""import datetime as date
import csv

#def date(periode):
with open('/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:
    ligne = csv.DictReader(f, ",")
    dates = []
    for date in ligne:
        dates.append(date(['Date de naissance']))

print(dates)"""

with open('/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:
    ligne = f.readlines()
    for line in ligne:
        print(line)