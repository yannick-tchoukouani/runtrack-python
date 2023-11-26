def afficher_tapis_diagonale(n):
    if n < 0:
        print("La taille doit être supérieure ou égale à zéro.")
        return

    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                print('\\', end='')
            elif i + j == n:
                print('/', end='')
            else:
                print('_', end='')
        print()

# Exemple d'utilisation avec afficher_tapis_diagonale(5)
afficher_tapis_diagonale(5)
