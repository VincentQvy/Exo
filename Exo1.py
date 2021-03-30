import math


# Cours 1 exo 1
temps = 6.892
distance = 19.7
vitesse = distance / temps
vitesse = vitesse*10
vitesse = math.ceil(vitesse)
vitesse = vitesse/10
print(vitesse)

# Cours 1 exo 2
nom = input("Votre nom ? ")
age = input("Votre age ? ")
print("Vous vous appellez " + nom + " et vous avez" + age)