import csv


with open('/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:
    # Créer un lecteur CSV qui permet de lire ligne par ligne le fichier
    lecteur = csv.DictReader(f, dialect='unix')

    # Lecture par ligne et vérification de la validité des données
    # Lecture par ligne et vérification de la validité des données
    for ligne in lecteur:
        ligne['Note'].strip().split("#")
        print(ligne['Note'])
        
        