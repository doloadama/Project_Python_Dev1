def calculer_moyennes(chaine_notes):
    """
    Fonction pour calculer les moyennes des notes pour chaque matière.

    Paramètre:
      chaine_notes: La chaîne de caractères contenant les notes.

    Returns:
      Un dictionnaire contenant les moyennes pour chaque matière.
    """

    matieres_notes = chaine_notes.split('#')
    resultats = {}
    for matiere_note in matieres_notes:
        nom_matiere, notes = matiere_note.split('[')
        notes_devoirs, note_examen = notes.split(':')
        note_examen = note_examen.split(']')[0]

        # Nettoyage des notes de devoirs
        notes_devoirs = notes_devoirs.replace(" ", "")
        notes_devoirs = notes_devoirs.replace(',', '|').strip('|')
        notes_devoirs = [float(note) for note in notes_devoirs.split('|') if note.isdigit()]

        # Calcul de la moyenne des devoirs
        moyenne_devoirs = sum(notes_devoirs) / len(notes_devoirs)

        # Conversion de la note d'examen en float
        note_examen = float(note_examen)

        # Calcul de la moyenne selon la formule fournie
        moyenne = (moyenne_devoirs + 2 * note_examen) / 3
        try:
            resultats[nom_matiere] = {
                'notes_devoirs': notes_devoirs,
                'note_examen': note_examen,
                'moyenne': moyenne
            }
        except:
            continue

    return resultats


# Exemple d'utilisation
chaine = "Math[04|03:05] #Francais[15|16:14] #Anglais[15|16:17] #PC[04|03:07] #SVT[12|09:10] #HG[16|15:17]"
moyennes = calculer_moyennes(chaine)
for matiere, infos in moyennes.items():
    print(f"{matiere} :{infos['moyenne']:.2f}")