def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    
    # Vérification si l'index 2 existe
    if len(fruits) > 2:
        fruits.insert(2, "Mangue")
    else:
        print("L'index 2 n'existe pas dans la liste.")

    return fruits

# Appel de la fonction et affichage du résultat
resultat = ajouter_mangue()
print(resultat)
