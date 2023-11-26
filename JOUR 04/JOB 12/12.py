def tri_insertion(liste):
    for i in range(1, len(liste)):
        valeur_actuelle = liste[i]
        position = i

        # Déplacer les éléments plus grands vers la droite
        while position > 0 and liste[position - 1] > valeur_actuelle:
            liste[position] = liste[position - 1]
            position -= 1

        # Insérer la valeur actuelle à sa position correcte
        liste[position] = valeur_actuelle

# Exemple d'utilisation
ma_liste = [7, 11, 42, 39, 2]

# Afficher la liste avant le tri
print("Liste avant le tri :", ma_liste)

# Appeler la fonction de tri
tri_insertion(ma_liste)

# Afficher la liste après le tri
print("Liste après le tri :", ma_liste)
