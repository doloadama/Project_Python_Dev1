import datetime
import re
import csv

def valider_numero(numero):
    return len(numero) == 7 and numero.isalnum() and numero.isupper()

def valider_prenom(prenom):
    return prenom[0].isalpha() and len(prenom) >= 3

def valider_nom(nom):
    return nom[0].isalpha() and len(nom) >= 2

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
        date_str: La date à vérifier sous forme de chaîne de caractères.

    Returns:
        True si la date est valide, False sinon.
    """
    date_formats = ["%d/%m/%y", "%d/%m/%Y", "%d %m %Y", "%d %B %Y", "%d,%m,%Y", "%d:%m:%Y", "%d-%m-%Y", "%d|%m|%Y", "%d.%m.%Y",
                    "%d/%B/%Y", "%d.%B.%Y", "%d-%B-%Y", "%d:%B:%Y", "%d_%m_%Y", "%d-%m-%y", "%d %m %y", "%d %B %y", "%d,%m,%y",
                    "%d:%m:%y", "%d|%m|%y", "%d|%B|%y", "%d.%m.%y", "%d.%B.%y", "%d-%B-%y", "%d:%B:%y", "%d_%m_%y", "%m/%d/%y",
                    "%m/%d/%Y", "%m-%d-%Y", "%m-%d-%y", "%Y-%m-%d", "%d-%m-%y", "%d %m %Y", "%d %B %Y", "%d,%m,%Y", "%d:%m:%Y",
                    "%d/%m/%y", "%d-%m-%y", "%d %m %y", "%d %B %y", "%d,%m,%y", "%d:%m:%y", "%d|%m|%y", "%d|%B|%y", "%d.%m.%y",
                    "%d.%B.%y", "%d-%B-%y", "%d:%B:%y", "%d,%B,%y", "%d/%B/%y", "%d.%B.%y", "%d|%B|%Y", "%d-%B-%Y", "%d:%B:%Y",
                    "%d_%m_%y", "%d_%m_%Y", "%d-%B-%Y", "%d-%m-%Y"
                    ]

    for format_str in date_formats:
        try:
            # Tenter de convertir la chaîne de caractères en objet datetime
            datetime.datetime.strptime(date_str, format_str)
            return True  # La conversion a réussi, la date est valide
        except ValueError:
            pass  # Si une erreur de conversion se produit, essayer le format suivant

    # Si aucun format ne fonctionne, la date n'est pas valide
    return False


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
                valider_nom(ligne['Nom']) and est_date_valide(ligne['Date de naissance']) and
                format_classe(ligne['Classe']) and valider_notes(ligne['Notes'])):
                donnees_valides.append(ligne)
            else:
                donnees_invalides.append(ligne)
        
        return donnees_valides, donnees_invalides

filename='/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv'


valide = []
invalide = []

