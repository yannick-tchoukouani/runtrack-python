def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  # Vérification pour éviter une division par zéro
            return num1 / num2
        else:
            return "Erreur: Division par zéro"
    elif operator == '%':
        if num2 != 0:  # Vérification pour éviter un modulo par zéro
            return num1 % num2
        else:
            return "Erreur: Modulo par zéro"
    else:
        return "Opérateur non valide"

# Exemples d'appels de la fonction
result1 = calcule(5, '+', 3)
result2 = calcule(10, '*', 2)
result3 = calcule(8, '/', 2)

# Affichage des résultats
print(result1)
print(result2)
print(result3)
