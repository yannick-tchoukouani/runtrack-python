def afficher_alphabet_envers():
    for lettre in range(ord('Z'), ord('A')-1, -1):
        print(chr(lettre), end=' ')


afficher_alphabet_envers()