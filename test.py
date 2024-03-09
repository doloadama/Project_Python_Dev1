import csv
import datetime as date

def number(num):
    """
    Fonction qui permet de verifier la validité
        * Le Numéro doit contenir des lettres en majuscules et des chiffres
        * Le numéro doit avoir une longueur de 7 (len(num) == 7)
    param: 
        num : le numero à vérifier
    """
    """
    Function that verifies the validity
    * The number must contain uppercase letters and digits
    * The number must have a length of 7 (len(num) == 7)
    param:
    num : the number to be checked
    """
    return num.isalnum() and len(num) == 7 and num.isupper()

def is_valid_date(date_str):
    try:
        date.strptime(date_str)
        return True
    except ValueError:
        return False

# Fonction pour convertir les dates au format YYYY-MM-DD
def format_date(date_str):
        # Liste de formats de date possibles
        formats = ["%d/%m/%y", "%d/%m/%Y", "%m/%d/%y", "%m/%d/%Y", "%dm%Y", "%d %b %Y", "%H:%M:%S"]

        #Convertir la date avec différents formats
        for fmt in formats:
            try:
                date_obj = date.datetime.strptime(date_str, fmt)
                return date_obj.strftime("%Y-%m-%d")
            except ValueError:
                continue
        # Si aucun format ne correspond, retournez la date d'origine
        return date_str


def compte_lettres(mot):
    """
    Function that takes a parameter and return the number of letters in that parameter
    """
    """
    Fonction qui prend en paramètre un mot et retourne le nombre de lettres qu'il contient"""
    compte = 0
    for lettre in mot:
        if lettre.isalpha():
            compte += 1
        else:
            continue
    return compte


def name(nom):
    debut = nom[0]
    return debut.isalpha() and compte_lettres(nom) >= 2

def firstname(prenom):
    debut = prenom[0]
    return debut.isalpha() and compte_lettres(prenom) >= 3

# Création de deux listes qui contiendront les lignes valides et invalides
valide, invalide = [], []

# Ouvrir le fichier en mode lecture et le lire
with open('/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:

    # Création et affectation d'un lecteur CSV
    lecteur = csv.DictReader(f, delimiter=',')

    # Lecture par ligne et vérification de la validité du numéro
    for ligne in lecteur:
        #On vérifie que la colonne numéro est valide
        if ligne.items == "":
            invalide.append(ligne)
        else:
            valide.append(ligne)
        if number(ligne['Numero']):
            valide.append(ligne)
        else:
            invalide.append(ligne)
        #Vérification de la validité des noms et prénoms
        if name(ligne(['Nom'])) and firstname(ligne['Prenom']):
            valide.append
        else:
            invalide.append(ligne)
