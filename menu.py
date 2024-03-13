from tabulate import tabulate
import csv
from gestion_validations import *

# Les deux listes qui se chargeront de stocker les informations à afficher
invalide = []
valide = []
filename = '/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv'


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
        return d.get('moyenne_generale', 10)

    trie = sorted(valide, key=function, reverse=True)
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


# Menu interactif
while True:
    print("Menu interactif :")
    print("1. Afficher les informations")
    print("2. Afficher une information par son numéro")
    print("3. Afficher les cinq premiers")
    print("4. Ajouter une information")
    print("5. Modifier une information invalide")
    print("6. Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        afficher_informations(valide, invalide)

    elif choix == "2":
        print()
        numero = input("Entrez le numéro de l'information : ")
        valide = afficher_information_par_numero(numero)
        for ligne in valide:
            if valide:
                print(tabulate(valide, headers="keys", tablefmt="simple"), end="\n")
                print()
            else:
                print("Numero inexistant!")
    elif choix == "3":
        trie = afficher_cinq_premiers(filename)
        print(tabulate(trie, headers='keys', tablefmt="simple_grid", maxcolwidths=[None, 8]), end="\n")
    elif choix == "4":
        ajouter_information(valide)
        afficher_informations(valide, invalide)
    elif choix == "5":
        modifier_information(valide, invalide)
        afficher_informations(valide, invalide)
    elif choix == "6":
        print("Fin du programme.")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")
    print("\n" * 2)
