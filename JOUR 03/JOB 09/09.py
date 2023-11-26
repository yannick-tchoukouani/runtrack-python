def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3

# Demander à l'utilisateur de saisir trois notes
note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))

# Calculer la moyenne
moyenne_etudiant = moyenne(note1, note2, note3)

# Afficher la moyenne de l'étudiant
print(f"La moyenne de l'étudiant est : {moyenne_etudiant}")

# Afficher la phrase en fonction de la moyenne
if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")
elif 11 <= moyenne_etudiant <= 14:
    print("Bon élève")
elif 8 <= moyenne_etudiant <= 10:
    print("Élève moyen")
elif 0 <= moyenne_etudiant <= 7:
    print("Élève devant faire des efforts")
else:
    print("Moyenne non valide")
