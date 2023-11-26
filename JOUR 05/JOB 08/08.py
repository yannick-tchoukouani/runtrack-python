def my_sort(liste):
    # Initialiser le nombre total de coups
    nombre_coups_total = 0
    # Initialiser une variable pour indiquer si des échanges ont été effectués
    echanges_effectues = True

    # Boucle principale du tri à bulles
    while echanges_effectues:
        # Réinitialiser la variable d'échanges
        echanges_effectues = False

        # Parcourir la liste jusqu'à l'avant-dernier élément
        for i in range(len(liste) - 1):
            # Comparer les éléments adjacents et les échanger si nécessaire
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                # Marquer que des échanges ont été effectués
                echanges_effectues = True
                # Incrémenter le nombre total de coups
                nombre_coups_total += 1

    # Retourner la liste triée et le nombre total de coups
    return liste, nombre_coups_total

# Exemple d'utilisation
ma_liste = [5, 2, 9, 1, 5, 6]
liste_triee, nombre_coups = my_sort(ma_liste)

# Afficher le résultat
print("Liste triée :", liste_triee)
print("Nombre total de coups :", nombre_coups)
