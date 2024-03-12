import csv

def valide_note(note):
    for i in note:
        if i.isalpha():
            return False
        else:
            continue
    return True


def calculer_moyennes(chaine_notes):
    matieres_notes = chaine_notes.split('#')
    resultats = {}
    liste = []

    for matiere_note in matieres_notes:
        nom_matiere, notes = matiere_note.split('[')
        notes_devoirs, note_examen = notes.strip(']').split(':')
        notes_devoirs = [float(note.replace(',', '.')) for note in notes_devoirs.split('|')]
        
        moyenne_devoirs = sum(notes_devoirs) / len(notes_devoirs)

        note_examen = float(note_examen.replace(',', '.').strip("]").replace(" ",""))
        
        moyenne = float((moyenne_devoirs + (2 * note_examen) ))/ 3
        
        resultats[nom_matiere] = {
            'notes_devoirs': notes_devoirs,
            'note_examen': note_examen,
            'moyenne': moyenne
        }
    
    return resultats

# Ouvrir le fichier en mode lecture et le lire
with open('/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:
    # Créer un lecteur CSV qui permet de lire ligne par ligne le fichier
    lecteur = csv.DictReader(f, dialect='unix')

    # Lecture par ligne et vérification de la validité des données
    for ligne in lecteur:
        if valide_note(ligne['Note']):
            date = calculer_moyennes(ligne['Note'])
            print(date)
