def arrondir_et_trier(liste):
    # Arrondir les nombres dans la liste
    liste_arrondie = [int(nombre + 0.5) for nombre in liste]

    # Algorithme de tri par insertion
    for i in range(1, len(liste_arrondie)):
        valeur_actuelle = liste_arrondie[i]
        position = i

        while position > 0 and liste_arrondie[position - 1] > valeur_actuelle:
            liste_arrondie[position] = liste_arrondie[position - 1]
            position -= 1

        liste_arrondie[position] = valeur_actuelle

    return liste_arrondie

# Exemple d'utilisation
ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Appeler la fonction pour arrondir et trier la liste
resultat = arrondir_et_trier(ma_liste)

# Afficher le résultat
print("Liste arrondie et triée :", resultat)
