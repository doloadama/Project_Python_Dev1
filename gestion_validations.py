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
        date_str: La date à vérifier sous forme de chaîne de caractères.

    Returns:
        True si la date est valide, False sinon.
    """
    date_formats = ["%d/%m/%y", "%d/%m/%Y", "%d %m %Y", "%d %B %Y", "%d,%m,%Y", "%d:%m:%Y", "%d-%m-%Y", "%d|%m|%Y",
                    "%d.%m.%Y",
                    "%d/%B/%Y", "%d.%B.%Y", "%d-%B-%Y", "%d:%B:%Y", "%d_%m_%Y", "%d-%m-%y", "%d %m %y", "%d %B %y",
                    "%d,%m,%y",
                    "%d:%m:%y", "%d|%m|%y", "%d|%B|%y", "%d.%m.%y", "%d.%B.%y", "%d-%B-%y", "%d:%B:%y", "%d_%m_%y",
                    "%m/%d/%y",
                    "%m/%d/%Y", "%m-%d-%Y", "%m-%d-%y", "%Y-%m-%d", "%d-%m-%y", "%d %m %Y", "%d %B %Y", "%d,%m,%Y",
                    "%d:%m:%Y",
                    "%d/%m/%y", "%d-%m-%y", "%d %m %y", "%d %B %y", "%d,%m,%y", "%d:%m:%y", "%d|%m|%y", "%d|%B|%y",
                    "%d.%m.%y",
                    "%d.%B.%y", "%d-%B-%y", "%d:%B:%y", "%d,%B,%y", "%d/%B/%y", "%d.%B.%y", "%d|%B|%Y", "%d-%B-%Y",
                    "%d:%B:%Y",
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


def calculer_moyennes(chaine_notes):
    """
    Fonction pour calculer les moyennes des notes pour chaque matière et la moyenne générale.

    Args:
        chaine_notes: La chaîne de caractères contenant les notes au format spécifié.

    Returns:
        Un dictionnaire contenant les notes, les moyennes pour chaque matière, et la moyenne générale.

    Raises:
        ValueError: Si une erreur se produit lors de l'analyse en raison d'un format invalide.
    """
    resultats = {}
    total_notes = 0
    nombre_matieres = 0

    for matiere_note in chaine_notes.split('#'):
        try:
            nom_matiere, notes = matiere_note.split('[')
            notes_devoirs, note_examen = notes.strip(']').split(':')

            # Nettoyage des notes de devoirs
            notes_devoirs = notes_devoirs.replace(" ", "")
            notes_devoirs = notes_devoirs.replace(',', '|').strip('|')

            # Extraction et conversion des notes en nombres flottants
            notes_devoirs = [float(note) for note in notes_devoirs.split('|') if note.isdigit()]

            # Vérifier si des notes de devoirs valides ont été trouvées
            if notes_devoirs:
                # Conversion de la note d'examen en flottant
                note_examen = float(note_examen) if float(note_examen) else 0

                # Si la note d'examen est supérieure à 20, la mettre à zéro
                if note_examen > 20:
                    note_examen = 0

                # Calcul de la moyenne des devoirs
                moyenne_devoirs = sum(notes_devoirs) / len(notes_devoirs)

                # Calcul de la moyenne selon la formule fournie
                moyenne_matiere = (moyenne_devoirs + 2 * note_examen) / 3

                # Stocker les résultats pour cette matière
                resultats[nom_matiere] = {
                    'notes_devoirs': notes_devoirs,
                    'note_examen': note_examen,
                    'moyenne': round(moyenne_matiere, 2)
                }

                total_notes += moyenne_matiere
                nombre_matieres += 1
        except (ValueError, IndexError):
            continue

    # Calcul de la moyenne générale
    if nombre_matieres > 0:
        moyenne_generale = round((total_notes / 6), 2)
    else:
        raise ValueError("Aucune note valide trouvée dans la chaîne d'entrée.")

    resultats['moyenne_generale'] = moyenne_generale

    return resultats


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
    classe = classe.replace(" ", "")
    classe = classe[0]+"eme"+classe[-1]
    return classe

def traiter_donnees():
    donnees_valides = []
    donnees_invalides = []

    return donnees_valides, donnees_invalides

