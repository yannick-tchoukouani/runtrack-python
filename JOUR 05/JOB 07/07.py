def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        if note < 40:
            # Échec, pas d'arrondi
            notes_arrondies.append(note)
        else:
            # Arrondir seulement si la note est à moins de 3 points de son prochain multiple de 5
            reste = note % 5
            if reste >= 3:
                note_arrondie = note + (5 - reste)
            else:
                note_arrondie = note

            # Limiter la note à 100
            note_arrondie = min(note_arrondie, 100)

            notes_arrondies.append(note_arrondie)

    return notes_arrondies

# Exemple d'utilisation
notes_etudiants = [83, 76, 92, 41, 55]
notes_arrondies = arrondir_notes(notes_etudiants)

# Afficher le résultat
print("Notes originales :", notes_etudiants)
print("Notes arrondies :", notes_arrondies)
