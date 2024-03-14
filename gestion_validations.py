import datetime
import csv
from tabulate import tabulate

filename = '/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv'

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

                """"# Si la note d'examen est supérieure à 20, la mettre à zéro
                if note_examen > 20:
                    note_examen = 0"""

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
        moyenne_generale = round((total_notes / nombre_matieres), 2)
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

def traiter_donnees(filename):
    valide = []
    invalide = []
    # Ouvrir le fichier en mode lecture et le lire
    with open('/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:
        # Créer un lecteur CSV qui permet de lire ligne par ligne le fichier
        lecteur = csv.DictReader(f, dialect='unix')
        # Lecture par ligne et vérification de la validité des données
        for ligne in lecteur:
            if number(ligne['Numero']) and name(ligne['Nom']) and firstname(ligne['Prénom']) and est_date_valide(
                    ligne["Date de naissance"]) and valide_classe(ligne['Classe']) and calculer_moyennes(ligne['Note']):
                # Formater la date correctement
                notes = calculer_moyennes(ligne['Note'])
                ligne['Note'] = notes
                formatted_date = format_date(ligne["Date de naissance"])
                formatted_classe = format_classe((ligne['Classe']))
                ligne['Classe'] = formatted_classe
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

        return valide, invalide

# Les deux listes qui se chargeront de stocker les informations à afficher
valide, invalide = traiter_donnees(filename)

def afficher_informations(valide=[], invalide=[]):
    filename = '/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv'
    valide, invalide = traiter_donnees(filename)

    # Demander à l'utilisateur combien de lignes par page il veut paginer
    lignes_par_page = int(input("Combien de lignes par page voulez-vous paginer ? "))

    # Afficher les données paginées
    for i in range(0, len(valide), lignes_par_page):
        print(tabulate(valide[i:i + lignes_par_page], headers="keys", tablefmt="grid"), end="\n")

        # Demander à l'utilisateur s'il veut continuer ou arrêter
        continuer = input("Appuyez sur Entrée pour continuer ou 'q' pour quitter : ")
        if continuer.lower() == 'q':
            break

def afficher_information_par_numero(numero):
    valide = []
    # Ouvrir le fichier en mode lecture et le lire
    with open('/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:
        # Créer un lecteur CSV qui permet de lire ligne par ligne le fichier
        lecteur = csv.DictReader(f, dialect='unix')

        # Lecture par ligne et vérification de la validité des données
        for ligne in lecteur:
            if number(ligne['Numero']) and name(ligne['Nom']) and firstname(ligne['Prénom']) and est_date_valide(
                    ligne["Date de naissance"]) and valide_classe(ligne['Classe']) and calculer_moyennes(ligne['Note']):
                # Formater la date correctement
                notes = calculer_moyennes(ligne['Note'])
                ligne['Note'] = notes
                formatted_date = format_date(ligne["Date de naissance"])
                if formatted_date:
                    # Si la date est formatée avec succès, l'ajouter à la liste des valides
                    ligne["Date de naissance"] = formatted_date  # Mettre à jour la date dans la ligne
                    if numero == ligne['Numero']:
                        valide.append(ligne)
                else:
                    return "Numero inexistant"
    return valide

def afficher_cinq_premiers(filename):
    valide, invalide = traiter_donnees(filename)

    # Check if all elements in valide are dictionaries (modify if needed)
    if not all(isinstance(item, dict) for item in valide):
        raise ValueError("Invalid data format in valide list")

    # Assuming "moyenne" is the key for sorting grades (modify if different)
    def function(d):
        return d.get('moyenne_generale', 0)
    trie = sorted(valide, key=function, reverse=False)
    return trie[:5]

def ajouter_information(valide):
    # Demander à l'utilisateur de saisir les informations pour ajouter
    numero = input("Entrez le numéro : ")
    nom = input("Entrez le nom : ")
    prenom = input("Entrez le prénom : ")
    date_naissance = input("Entrez la date de naissance (format : JJ/MM/AAAA) : ")
    classe = input("Entrez la classe : ")
    note = input("Entrez les notes (format : Matière1[Note1_1|Note1_2:Note1_3]#Matiere2[Note2_1|Note2_2:Note2_3]) : ")

    # Vérifier si les données saisies sont valides
    if (number(numero) and name(nom) and firstname(prenom) and est_date_valide(date_naissance)
            and valide_classe(classe) and calculer_moyennes(note)):
        # Formater les données correctement
        notes = calculer_moyennes(note)
        formatted_date = format_date(date_naissance)
        formatted_classe = format_classe(classe)

        # Créer un dictionnaire pour représenter l'information à ajouter
        information = {
            "Code": "AAD004",
            "Numero": numero,
            "Nom": nom,
            "Prénom": prenom,
            "Date de naissance": formatted_date,
            "Classe": formatted_classe,
            "Note": notes
        }

        # Ajouter l'information à la liste valide
        valide.append(information)
        print("Information ajoutée avec succès à la liste valide.")
    else:
        print("Les données saisies ne sont pas valides. Veuillez réessayer.")
    return valide

def chercher_invalide(filename):
  """
  Finds and records keys of invalid entries in a CSV file based on Numero and Nom validation.

  Args:
      filename: The name of the CSV file.

  Returns:
      A set containing unique keys of invalid entries.
  """

  erreurs = []
  with open(filename, 'r') as f:
      lecteur = csv.DictReader(f, dialect='unix')
      for ligne in lecteur:
          if not number(ligne['Numero']):
              erreurs.append('Numero')
          elif not name(ligne['Nom']):
              erreurs.append('Nom')
          elif not firstname((ligne['Prénom'])):
              erreurs.append('Nom')
          elif not est_date_valide((ligne['Date de naissance'])):
              erreurs.append('Nom')
          elif not valide_classe((ligne['Classe'])):
              erreurs.append('Classe')
          elif not valide_classe((ligne['Note'])):
              erreurs.append('Note')
  return f"les colonnes invalides sont`{erreurs}"

print(chercher_invalide(filename))

def modifier_information(valide, invalide):
    # Demander à l'utilisateur de saisir le numéro de la ligne invalide à modifier
    numero_ligne = input("Entrez le numéro de la ligne invalide à modifier : ")

    # Recherche de l'indice de la ligne invalide dans la liste des invalides
    indice_invalide = None
    for i, ligne in enumerate(invalide):
        if ligne["Numero"] == numero_ligne:
            indice_invalide = i
            break

    if indice_invalide is not None:
        # Récupérer la ligne invalide à modifier
        ligne_a_modifier = invalide[indice_invalide]

        # Afficher les détails de la ligne invalide
        print("Détails de la ligne invalide à modifier :")
        print(ligne_a_modifier)

        # Demander à l'utilisateur de saisir les nouvelles informations
        nouveau_numero = input("Entrez le nouveau numéro : ")
        nouveau_nom = input("Entrez le nouveau nom : ")
        nouveau_prenom = input("Entrez le nouveau prénom : ")
        nouvelle_date_naissance = input("Entrez la nouvelle date de naissance (format : JJ/MM/AAAA) : ")
        nouvelle_classe = input("Entrez la nouvelle classe : ")
        nouvelle_note = input("Entrez les nouvelles notes (format : Matière1[Note1_1|Note1_2:Note1_3]#Matiere2[Note2_1|Note2_2:Note2_3]) : ")

        # Vérifier si les nouvelles données saisies sont valides
        if (number(nouveau_numero) and name(nouveau_nom) and firstname(nouveau_prenom)
                and est_date_valide(nouvelle_date_naissance) and valide_classe(nouvelle_classe)
                and calculer_moyennes(nouvelle_note)):
            # Formater les nouvelles données correctement
            nouvelles_notes = calculer_moyennes(nouvelle_note)
            nouvelle_date_formatee = format_date(nouvelle_date_naissance)
            nouvelle_classe_formatee = format_classe(nouvelle_classe)

            # Mettre à jour la ligne invalide avec les nouvelles informations
            ligne_a_modifier["Numero"] = nouveau_numero
            ligne_a_modifier["Nom"] = nouveau_nom
            ligne_a_modifier["Prénom"] = nouveau_prenom
            ligne_a_modifier["Date de naissance"] = nouvelle_date_formatee
            ligne_a_modifier["Classe"] = nouvelle_classe_formatee
            ligne_a_modifier["Note"] = nouvelles_notes

            # Ajouter la ligne mise à jour à la liste valide
            valide.append(ligne_a_modifier)

            # Supprimer la ligne invalide de la liste des invalides
            del invalide[indice_invalide]

            print("Ligne invalide mise à jour avec succès et déplacée vers la liste valide.")
        else:
            print("Les nouvelles données saisies ne sont pas valides. La ligne invalide n'a pas été mise à jour.")
    else:
        print(f"Aucune ligne invalide trouvée avec le numéro {numero_ligne}.")

    return valide, invalide
