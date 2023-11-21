
# Initialisation des variables
montant_initial = 10000  # Montant initial de l'investissement en euros
taux_rendement_annuel = 5  # Taux de rendement annuel en pourcentage

# Afficher le gain annuel initial
gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Gain annuel initial à un taux de {taux_rendement_annuel}% : {gain_annuel} euros")

# L'investisseur augmente son capital de 5 000 euros et le taux augmente de 2%
montant_initial += 5000
taux_rendement_annuel += 2

# Calculer le nouveau gain annuel
nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Nouveau gain annuel après augmentation de capital et augmentation de taux : {nouveau_gain_annuel} euros")

# L'investisseur retire 10% du montant total, le rendement diminue de 1%
retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1

# Calculer le montant final de l'investissement et le nouveau gain annuel
montant_final = montant_initial * (1 + taux_rendement_annuel / 100)
nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_final

# Afficher les résultats finaux
print(f"Montant final de l'investissement après retrait et diminution du taux : {montant_final} euros")
print(f"Nouveau gain annuel : {nouveau_gain_annuel} euros")

