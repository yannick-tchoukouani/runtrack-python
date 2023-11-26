# Fonction pour échanger les valeurs de la première et de la dernière case d'une liste
def echanger_premiere_derniere(liste):
    if len(liste) >= 2:
        premiere_valeur = liste[0]
        derniere_valeur = liste[-1]

        # Échanger les valeurs
        liste[0] = derniere_valeur
        liste[-1] = premiere_valeur

# Exemple d'utilisation avec une liste non vide
ma_liste = [1, 2, 3, 4, 5]

# Afficher la liste avant l'échange
print("Avant l'échange :", ma_liste)

# Appeler la fonction pour échanger les valeurs
echanger_premiere_derniere(ma_liste)

# Afficher la liste après l'échange
print("Après l'échange :", ma_liste)
