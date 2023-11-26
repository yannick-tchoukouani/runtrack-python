def affiche_pos_neg(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("Le nombre est égal à 0")

# Appels de la fonction avec différents paramètres
affiche_pos_neg(5)
affiche_pos_neg(-3)
affiche_pos_neg(0)
