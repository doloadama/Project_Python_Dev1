import csv
import datetime

def changer_format_date(date_str):
    """
    Fonction pour changer le format d'une date.

    Args:
        date_str (str): La date à convertir au format de chaîne de caractères.

    Returns:
        str: La date convertie dans un nouveau format, ou None si une erreur se produit.
    """
    try:
        # Convertir la date en objet datetime avec l'ancien format "%d/%m/%Y"
        date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
        
        # Changer le format de la date au format "%Y-%m-%d"
        formatted_date = date_obj.strftime("%Y-%m-%d")
        
        return formatted_date
    
    except ValueError:
        # Si une erreur se produit lors de la conversion, retourner None
        return date_str

def est_date_valide(date_str):
    """
    Fonction pour vérifier si une date est valide.

    Args:
        date_str: La date à tester sous forme de chaîne de caractères.

    Returns:
        True si la date est valide, False sinon.
    """

    try:
        # Convertir la date en format datetime
        datetime.datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        # La date n'est pas au format attendu
        return False

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

def gestion_notes(notes):

# Ouvrir le fichier en mode lecture et le lire
# Création de deux listes qui contiendront les lignes valides et invalides
valide, invalide = [], []

def format_classe(classe):
    classe.strip()
    if classe[0].isdigit():
        classe.replace("i", "")
        nouvelle_classe = classe[0:2] + "e" + classe[4:]

# Ouvrir le fichier en mode lecture et le lire
with open('/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:
    # Créer un lecteur CSV qui permet de lire ligne par ligne le fichier
    lecteur = csv.DictReader(f, dialect='unix')

    # Lecture par ligne et vérification de la validité des données
    # Lecture par ligne et vérification de la validité des données
    for ligne in lecteur:
        valide.append(ligne)
        
        

print("Les données valides: ")
for a in valide:
  print(a['Note'])

print()

"""print("Les données invalides: ")
for a in invalide:
  print(a['Date de naissance'])"""
