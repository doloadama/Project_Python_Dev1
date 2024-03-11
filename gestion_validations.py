import datetime
import re
import csv

def valider_numero(numero):
    return len(numero) == 7 and numero.isalnum() and numero.isupper()

def valider_prenom(prenom):
    return prenom[0].isalpha() and len(prenom) >= 3

def valider_nom(nom):
    return nom[0].isalpha() and len(nom) >= 2

def valider_date_naissance(date_str):
    try:
        datetime.datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def convertir_format(chaine, format_source, format_cible="%d %b %Y"):
    """
    Fonction pour convertir une chaîne de caractères d'un format source à un format cible.

    Retourne:
        str: La chaîne de caractères convertie dans le format cible.
    """
    try:
        # Convertir la chaîne de caractères du format source au format datetime
        date_obj = datetime.datetime.strptime(chaine, format_source)
        
        # Formater la date dans le format cible
        chaine_convertie = date_obj.strftime(format_cible)
        
        return chaine_convertie
    
    except ValueError:
        # Si une erreur se produit lors de la conversion, retourner la chaîne d'origine
        return chaine

def valider_classe(classe):
    classe.strip()
    if classe[0].isdigit():
        classe.replace("i", "")
        nouvelle_classe = classe[0:2] + "e" + classe[4:]

def format_classe(chaine):
    # Définition des motifs de recherche et de remplacement
    motifs = [
        (r'\bTle\w*\b', 'Tle'),   # Remplace Tlel, TleS, TleA, etc. par Tle
        (r'\b(\d+)ieme\b', r'\1eme'),  # Remplace 4ieme, 5ieme, etc. par 4eme, 5eme, etc.
    ]

    # Appliquer les motifs de recherche et de remplacement
    for motif, remplacement in motifs:
        chaine = re.sub(motif, remplacement, chaine)

    return chaine

def valider_notes(notes):
    pass

def traiter_donnees(filename='/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv'):
    donnees_valides = []
    donnees_invalides = []
    with open(filename, 'r') as f:
    # Créer un lecteur CSV
        data = csv.DictReader(f, dialect='unix')

        # Lecture par ligne et vérification de la validité des données
        # Lecture par ligne et vérification de la validité des données
        for ligne in data:
            ligne['Date de naissance'].strip()
            
            
        
        for ligne in data:
            if (valider_numero(ligne['Numero']) and valider_prenom(ligne['Prénom']) and
                valider_nom(ligne['Nom']) and valider_date_naissance(ligne['Date de naissance']) and
                format_classe(ligne['Classe']) and valider_notes(ligne['Notes'])):
                donnees_valides.append(ligne)
            else:
                donnees_invalides.append(ligne)
        
        return donnees_valides, donnees_invalides

filename='/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv'


valide = []
invalide = []

""