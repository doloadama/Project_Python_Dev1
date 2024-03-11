def afficher_informations(informations):
    
def afficher_information_par_numero(numero):


def afficher_cinq_premieres_informations(informations):


def ajouter_information():


def modifier_information_invalide(information):


def afficher_par_pagination(informations, lignes_par_page=5):
    

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
        afficher_informations(donnees_valides)
    elif choix == "2":
        numero = input("Entrez le numéro de l'information : ")
        afficher_information_par_numero(numero)
    elif choix == "3":
        afficher_cinq_premieres_informations(donnees_valides)
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
