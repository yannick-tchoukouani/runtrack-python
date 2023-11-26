def draw_rectangle(width, height):
    if width < 1 or height < 1:
        print("Les dimensions doivent être supérieures à zéro.")
        return

    for i in range(height):
        if i == 0 or i == height - 1:
            # Première et dernière ligne : afficher des '-'
            print('-' * width)
        else:
            # Lignes intérieures : afficher '|', puis des espaces, puis '|'
            print('|' + ' ' * (width - 2) + '|')

# Exemple d'utilisation avec draw_rectangle(10, 3)
draw_rectangle(10, 3)
