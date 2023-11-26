def my_long_word(longueur_minimale, phrase):
    mots = []
    mot_actuel = ""

    for caractere in phrase:
        if caractere.isalnum():
            mot_actuel += caractere
        elif mot_actuel:
            if len(mot_actuel) > longueur_minimale:
                mots.append(mot_actuel)
            mot_actuel = ""

    # Vérifier le dernier mot de la phrase
    if mot_actuel and len(mot_actuel) > longueur_minimale:
        mots.append(mot_actuel)

    return " ".join(mots)

# Exemple d'utilisation
resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")

# Afficher le résultat
print("Output :", resultat)
