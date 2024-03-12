import csv
import re



def calculer_moyennes(chaine_notes):
  """
  Fonction pour calculer les moyennes des notes pour chaque matière.

  Args:
    chaine_notes: La chaîne de caractères contenant les notes au format spécifié.

  Returns:
    Un dictionnaire contenant les moyennes pour chaque matière, ou une exception si le format est invalide.

  Raises:
    ValueError: If an error occurs during parsing due to invalid format.
  """

  matieres_notes = chaine_notes.split('#')
  resultats = {}
  for matiere_note in matieres_notes:
    try:
      nom_matiere, notes = matiere_note.split('[')
      notes_devoirs, note_examen = notes.strip(']').split(':')

      # Nettoyage des notes de devoirs
      notes_devoirs = notes_devoirs.replace(" ", "")
      notes_devoirs = notes_devoirs.replace(',', '|').strip('|')

      # Extraction et conversion des notes en nombres flottants en gérant les caractères indésirables
      notes_devoirs = [float(note[:-1]) if note[-1] == ']' else float(note) for note in notes_devoirs.split('|')]

      # Calcul de la moyenne des devoirs et conversion de la note d'examen
      moyenne_devoirs = round(sum(notes_devoirs) / len(notes_devoirs), 2)
      note_examen = float(note_examen)

      # Calcul de la moyenne selon la formule fournie
      moyenne = round((moyenne_devoirs + 2 * note_examen) / (3), 2)
      resultats[nom_matiere] = {moyenne
      }
    except ValueError:
        continue

  return resultats


valide = []
invalide = []
# Ouvrir le fichier en mode lecture et le lire
with open('/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:
    # Créer un lecteur CSV qui permet de lire ligne par ligne le fichier
    lecteur = csv.DictReader(f, dialect='unix')

    # Lecture par ligne et vérification de la validité des données
    for ligne in lecteur:
        if calculer_moyennes(ligne['Note']):
            notes = calculer_moyennes(ligne['Note'])
            ligne['Note'] = notes
            valide.append(ligne)
        else:
            invalide.append(ligne)

print("Valide: ", end="\n"*3)
for char in valide:
    print(char['Note'])

print("\n"*3)


print("Invalide: ", end="\n"*3)
for char in invalide:
    print(char['Note'])
