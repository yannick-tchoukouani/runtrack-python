def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60

        if heures == 0:
            if minutes_restantes == 1:
                print(f"{minutes_restantes} minute")
            else:
                print(f"{minutes_restantes} minutes")
        elif heures == 1:
            if minutes_restantes == 0:
                print(f"{heures} heure")
            elif minutes_restantes == 1:
                print(f"{heures} heure et {minutes_restantes} minute")
            else:
                print(f"{heures} heure et {minutes_restantes} minutes")
        else:
            if minutes_restantes == 0:
                print(f"{heures} heures")
            elif minutes_restantes == 1:
                print(f"{heures} heures et {minutes_restantes} minute")
            else:
                print(f"{heures} heures et {minutes_restantes} minutes")
    else:
        print("Veuillez entrer un nombre entier positif.")

# Appels de la fonction avec différents paramètres
time_to_text(120)
time_to_text(75)
time_to_text(30)
time_to_text(-5)
time_to_text("Bonjour")
