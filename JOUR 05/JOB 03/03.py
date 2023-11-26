def draw_triangle(height):
    if height < 1:
        print("La hauteur doit être supérieure à zéro.")
        return

    for i in range(height):
        if i == height - 1:
            # Dernière ligne : afficher '_'
            print('_' * (2 * height - 1))
        else:
            # Lignes intérieures : afficher '\', puis des espaces, puis '/'
            espaces = ' ' * (height - i - 1)
            if i == 0:
                print(espaces + '\\')
            else:
                print(espaces + '\\' + ' ' * (2 * i - 1) + '/')

# Exemple d'utilisation avec draw_triangle(5)
draw_triangle(5)
