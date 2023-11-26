# Créer une liste d'au moins 5 entiers
L = [1, 2, 3, 4, 5]

# Afficher la deuxième valeur de la liste
deuxieme_valeur = L[1]
print(f"Deuxième valeur de la liste : {deuxieme_valeur}")

# Écrire une fonction pour remplacer L[3] par la somme des cases voisines L[2] & L[4]
def remplacer_element(liste):
    if len(liste) >= 5:
        liste[3] = liste[2] + liste[4]

# Appeler la fonction pour effectuer la modification
remplacer_element(L)

# Afficher le tableau après modification
print("Tableau après modification :", L)

# Afficher la dernière valeur de la liste
derniere_valeur = L[-1]
print(f"Dernière valeur de la liste : {derniere_valeur}")
