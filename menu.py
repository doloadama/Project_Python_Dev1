from tabulate import tabulate
import csv
from gestion_validations import *

# Les deux listes qui se chargeront de stocker les informations à afficher
invalide = []
valide = []
filename = '/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv'
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
