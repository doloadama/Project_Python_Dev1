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

# Exemple d'utilisation :
chaine = "Math[12|11:13]#Francais[4|11|8:13]#Anglais[13,5|11:15]#PC[11:9]#SVT[12|9|16|11:12]#HG[10:13]"
moyennes = calculer_moyennes(chaine)
for matiere, infos in moyennes.items():
    print(f"{matiere} - Devoirs: {infos['notes_devoirs']}, Examen: {infos['note_examen']}, Moyenne: {infos['moyenne']:.2f}")
