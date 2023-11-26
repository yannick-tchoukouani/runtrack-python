def distance_totale_parcourue(marches, hauteur_marche):
    # Nombre de montées et descentes par jour
    montees_descentes_par_jour = 2
    # Nombre de jours dans une semaine
    jours_par_semaine = 7

    # Calcul de la distance totale parcourue par semaine
    distance_semaine = marches * hauteur_marche * montees_descentes_par_jour * jours_par_semaine / 100

    return distance_semaine

# Exemple d'utilisation
nombre_marches = 10
hauteur_marche = 20

distance_parcourue = distance_totale_parcourue(nombre_marches, hauteur_marche)

# Afficher le résultat
print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_parcourue:.2f} m par semaine.")
