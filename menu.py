import csv, datetime
from tabulate import tabulate
from gestion_validations import*

#Les deux listes qui se chargeront de stocker les informations à afficher
invalide = []
valide = []

def traiter_donnees(filename='/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv'):
        valide = []
        invalide = []
        # Ouvrir le fichier en mode lecture et le lire
        with open('/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:
            # Créer un lecteur CSV qui permet de lire ligne par ligne le fichier
            lecteur = csv.DictReader(f, dialect='unix')

            # Lecture par ligne et vérification de la validité des données
            for ligne in lecteur:
                if number(ligne['Numero']) and name(ligne['Nom']) and firstname(ligne['Prénom']) and est_date_valide(ligne["Date de naissance"]) and valide_classe(ligne['Classe']) and calculer_moyennes(ligne['Note']):
                    # Formater la date correctement
                    notes = calculer_moyennes(ligne['Note'])
                    ligne['Note'] = notes
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
                    
            return valide, invalide

def afficher_informations():
    def traiter_donnees(filename='/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv'):
        valide = []
        invalide = []
        # Ouvrir le fichier en mode lecture et le lire
        with open('/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:
            # Créer un lecteur CSV qui permet de lire ligne par ligne le fichier
            lecteur = csv.DictReader(f, dialect='unix')

            # Lecture par ligne et vérification de la validité des données
            for ligne in lecteur:
                if number(ligne['Numero']) and name(ligne['Nom']) and firstname(ligne['Prénom']) and est_date_valide(ligne["Date de naissance"]) and valide_classe(ligne['Classe']) and calculer_moyennes(ligne['Note']):
                    # Formater la date correctement
                    notes = calculer_moyennes(ligne['Note'])
                    ligne['Note'] = notes
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
                    
            return valide, invalide
    filename='/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv'
    invalide = []
    valide = []
    valide, invalide = traiter_donnees(filename)
    print(tabulate(valide, headers= "keys",tablefmt="pipe"), end="\n")

def afficher_information_par_numero(numero):
        valide = []
        # Ouvrir le fichier en mode lecture et le lire
        with open('/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:
            # Créer un lecteur CSV qui permet de lire ligne par ligne le fichier
            lecteur = csv.DictReader(f, dialect='unix')

            # Lecture par ligne et vérification de la validité des données
            for ligne in lecteur:
                if number(ligne['Numero']) and name(ligne['Nom']) and firstname(ligne['Prénom']) and est_date_valide(ligne["Date de naissance"]) and valide_classe(ligne['Classe']) and calculer_moyennes(ligne['Note']):
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

def afficher_cinq_premieres_informations(informations):
    pass

def ajouter_information():
    choix = ['CODE','Numero','Nom','Prénom','Date de naissance','Classe','Note']
    choisir = input("Saisissez la ligne")

def modifier_information_invalide(information):
    pass

def afficher_par_pagination(informations, lignes_par_page=5):
    pass

# Menu interactif
while True:
    print("Menu interactif :")
    print("1. Afficher les informations")
    print("2. Afficher une information par son numéro")
    print("3. Afficher les cinq premières informations")
    print("4. Ajouter une information")
    print("5. Modifier une information invalide")
    print("6. Quitter")
    
    choix = input("Choisissez une option : ")
    
    if choix == "1":
        filename='/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv'
        valide, invalide = traiter_donnees(filename)
        traiter_donnees(filename)
        print("Données valides :",end="\n"*2 )
        print(tabulate(valide, headers= "keys",tablefmt="plain", maxcolwidths=[None, 8]), end="\n")
        print("Données invalides :",end="\n"*2 )
        print(tabulate(invalide, headers= "keys",tablefmt="plain", maxcolwidths=[None, 8]), end="\n")

    elif choix == "2":
        print()
        numero = input("Entrez le numéro de l'information : ")
        valide = afficher_information_par_numero(numero)
        for ligne in valide:
            if valide:
                print(tabulate(valide, headers= "keys",tablefmt="simple"), end="\n")
                print()
            else:
                print("Numero inexistant!")
    elif choix == "3":
        afficher_cinq_premieres_informations()
    elif choix == "4":
        ajouter_information()
    elif choix == "5":
        information = input("Entrez les informations de l'information à modifier : ")
        modifier_information_invalide(information)
    elif choix == "6":
        print("Fin du programme.")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")
    print("\n"*2)
