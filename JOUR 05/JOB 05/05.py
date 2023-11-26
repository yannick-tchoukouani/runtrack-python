def chiffrement_cesar(message, decalage):
    message_chiffre = ""

    for caractere in message:
        if 'a' <= caractere <= 'z':
            nouveau_caractere = chr((ord(caractere) - ord('a') + decalage) % 26 + ord('a'))
        elif 'A' <= caractere <= 'Z':
            nouveau_caractere = chr((ord(caractere) - ord('A') + decalage) % 26 + ord('A'))
        else:
            nouveau_caractere = caractere

        message_chiffre += nouveau_caractere

    return message_chiffre

# Exemple d'utilisation
message_original = "Bonjour, Cesar!"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)

print(f"Message original : {message_original}")
print(f"Message chiffré : {message_chiffre}")
