import datetime as date
import csv

# Fonction pour convertir les dates au format YYYY-MM-DD
def format_date(date_str):
    with open('C:/Users/doloa/Masterclass/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv') as f:
        ligne = csv.DictReader(f)
        # Liste de formats de date possibles
        formats = ["%d/%m/%y", "%d/%m/%Y", "%m/%d/%y", "%m/%d/%Y", "%dm%Y", "%d %b %Y", "%H:%M:%S"]
        # Ajoutez d'autres formats au besoin

        for line in ligne:
            formats.append(line['Date de naissance'])
        # Essayez de convertir la date avec différents formats
        for fmt in formats:
            try:
                date_obj = date.datetime.strptime(date_str, fmt)
                return date_obj.strftime("%Y-%m-%d")
            except ValueError:
                continue
        # Si aucun format ne correspond, retournez la date d'origine
        return date_str

# Liste pour stocker les dates converties
dates_converties = []

# Lecture du fichier CSV et conversion des dates
with open('C:/Users/doloa/Masterclass/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        # Convertir la date de naissance au format YYYY-MM-DD et l'ajouter à la liste
        dates_converties.append(format_date(ligne['Date de naissance']))

# Affichage des dates converties
for date_convertie in dates_converties:
    print(date_convertie)
