"""Jeu du plus ou moins."""


from random import randint
import sys
alea = randint(0, 20)  # Affiche un nombre aleatoire entre 0 et 20.
essaiRestant = 6
compteur = 0
nom = input('Entrez votre nom > ')


while compteur < essaiRestant:
    print("Essai", compteur + 1, "/ 6")
    nombre = input('Entrez un nombre entre 0 et 20 > ')
    if nombre.isdigit():
        compteur += 1
        nombre = int(nombre)
        if nombre == alea:
            print("Bravo vous avez gagné", nom)
            sys.exit()
        if nombre < alea:
            print("Le nombre est plus grand")
        if nombre > alea:
            print("Le nombre est plus petit")
    else:
        print("Nombre incorrect !")

print("Vous avez perdu !")
