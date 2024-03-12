import csv
import datetime
import re

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

def valide_note(note):
    bonne_note = re.match("[\d|\d:\d]", note)
    return bonne_note

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

def format_date(date_str):
    date_formats = [
        '%d/%m/%y', '%d-%m-%y', '%m/%d/%y', '%m|%d|%y', '%m/%d/%Y', '%m-%d-%Y',
        '%d %m %Y', '%d %B %Y', '%d,%m,%Y', '%d:%m:%Y', '%d|%m|%Y', '%d,%B,%y',
        '%d/%B/%y', '%d.%B.%y', '%d|%B|%y', '%d-%B-%y', '%d:%B:%y', '%d,%B,%Y',
        '%d/%B/%Y', '%d.%B.%Y', '%d|%B|%Y', '%d-%B-%Y', '%d:%B:%Y', '%d_%m_%Y',
        '%d_%m_%y'
    ]
    
    for fmt in date_formats:
        try:
            # Essayer de convertir la date avec le format actuel
            date_obj = datetime.datetime.strptime(date_str, fmt)
            # Si la conversion réussit, formater la date dans le format et la retourner
            formatted_date = date_obj.strftime("%d/%m/%Y")
            return formatted_date
        except ValueError:
            # Si la conversion échoue, essayer avec le prochain format
            continue
    
    # Si aucun format ne correspond, retourner None ou une valeur par défaut
    return None  # ou raise ValueError("Format de date invalide")

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

def extraire_notes(chaine):
    # Diviser la chaîne en fonction du séparateur '#'
    matieres = chaine.split('#')
    
    notes_matiere = {}
    
    for matiere in matieres:
        # Diviser chaque matière en fonction du séparateur '['
        nom_et_notes = matiere.split('[')
        if len(nom_et_notes) > 1:
            nom_matiere = nom_et_notes[0]
            liste = []
            # Extraire les notes de la matière en fonction du séparateur '|'
            notes_sans_crochets = nom_et_notes[1].split(']')[0]
            notes = notes_sans_crochets.split('|')
            
            # Convertir les notes en nombres flottants
            notes = [float(note) for note in notes]
            
            notes_matiere[nom_matiere] = notes
        
    return notes_matiere

def calculer_moyennes(chaine_notes):
    matieres_notes = chaine_notes.split('#')
    resultats = {}

    for matiere_note in matieres_notes:
        nom_matiere, notes = matiere_note.split('[')
        notes_devoirs, note_examen = notes.strip(']').split(':')
        notes_devoirs = [float(note.replace(',', '.')) for note in notes_devoirs.split('|')]
        
        moyenne_devoirs = sum(notes_devoirs) / len(notes_devoirs)
        note_examen = float(note_examen.replace(',', '.'))
        
        moyenne = (moyenne_devoirs + 2 * note_examen) / 3
        resultats[nom_matiere] = {
            'notes_devoirs': notes_devoirs,
            'note_examen': note_examen,
            'moyenne': moyenne
        }
    
    return resultats

# Ouvrir le fichier en mode lecture et le lire
# Création de deux listes qui contiendront les lignes valides et invalides
valide = []
invalide = []

def valide_classe(classe):
    classe.replace(" ", "")
    debut = ['6', '5', '4', '3']
    fin = ['A', 'B', 'C', 'D']
    if not classe:
        return False
    elif not classe[0] in debut or classe[-1] not in fin:
        return False
    else:
        return True

def format_classe(classe):
    classe.replace(" ", "")
    debut = ['6', '5', '4', '3']
    fin = ['A', 'B', 'C', 'D']
    if classe[0] in debut and classe[-1].upper() in fin:
        return f"{classe[0]}em{classe[-1].upper()}"

# Ouvrir le fichier en mode lecture et le lire
with open('/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:
    # Créer un lecteur CSV qui permet de lire ligne par ligne le fichier
    lecteur = csv.DictReader(f, dialect='unix')

    # Lecture par ligne et vérification de la validité des données
    for ligne in lecteur:
        if number(ligne['Numero']) and name(ligne['Nom']) and firstname(ligne['Prénom']) and est_date_valide(ligne["Date de naissance"]) :
            # Formater la date correctement
            formatted_date = format_date(ligne["Date de naissance"])
            if formatted_date:
                # Si la date est formatée avec succès, l'ajouter à la liste des valides
                ligne["Date de naissance"] = formatted_date  # Mettre à jour la date dans la ligne
                valide.append(ligne)
            else:
                # Si la date ne peut pas être formatée, ajouter la ligne à la liste des invalides
                invalide.append(ligne)
        else:
            # Si la date n'est pas valide, ajouter la ligne à la liste des invalides
            invalide.append(ligne)

print("Les données valides: ")
for a in valide:
  print(a, end="\n"*3)

print("\n"*3)

print("Les données invalides: ")
for a in invalide:
  print(a, end="\n"*3)
