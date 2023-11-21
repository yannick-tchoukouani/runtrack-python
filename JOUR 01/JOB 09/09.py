# Définition des variables du produit
nom_produit = "Ordinateur portable"
prix_unitaire = 1000.0
quantite_stock = 50

# Afficher les informations du produit
print("Informations du produit :")
print("Nom du produit :", nom_produit)
print("Prix unitaire :", prix_unitaire, "euros")
print("Quantité en stock :", quantite_stock)

# Ajouter des produits en stock
quantite_ajoutee = int(input("Entrez la quantité de produits à ajouter au stock : "))
quantite_stock += quantite_ajoutee

# Mettre à jour le prix en raison de l'inflation
taux_inflation = 0.10
prix_unitaire *= (1 + taux_inflation)

# Afficher à nouveau les informations du produit après les modifications
print("\nInformations mises à jour du produit :")
print("Nom du produit :", nom_produit)
print("Nouveau prix unitaire (avec inflation) :", prix_unitaire, "euros")
print("Quantité en stock après ajout :", quantite_stock)