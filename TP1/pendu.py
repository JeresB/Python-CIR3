"""Pendu."""


# On utilise choice pour récupérer un mot aléatoire dans la liste
from random import choice
from sys import argv

essaiRestant = 7  # Erreur Maximum
compteur = 0  # Nombre d'erreur actuelle
MotDecouvert = ""  # Mot découvert -> se complète au fur et à mesure
lettreUtilise = ""

# On récupère un mot alétoire dans un fichier fournit en argument
mot = choice(open(argv[1]).readlines()).strip()

# On demande le nom de l'utilisateur
nom = input('Entrez votre nom > ')

print("")

# On remplit le mot découvert par des tirets
# Autant de tirets que des lettres dans le mot à trouver
while len(mot) > len(MotDecouvert):
    MotDecouvert += "-"

# On continue tant que le mot n'a pas été trouvé
while mot != MotDecouvert:
    # Si le nombre maximum d'erreur a été atteint, on quitte la boucle
    if compteur >= essaiRestant:
        break

    # erreur vaut 1 tant qu'on a pas trouvé de lettre
    erreur = 1

    print("Erreur", compteur, "/ 7")  # On affiche le compteur d'erreur
    print("Mot :", MotDecouvert)  # On affiche le mot découvert
    print("")

    # On affiche les lettres utilisées
    print("Lettres utilisées :", lettreUtilise)

    # On demande une lettre à l'utilisateur
    lettre = input('Entrez une lettre > ')
    lettre = lettre.upper()  # On met en majuscule la lettre Entrez
    # On ajoute la lettre aux lettres déja utilisées
    lettreUtilise = lettreUtilise + lettre

    print("")

    # Si e caractère n'est pas une lettre on affiche une erreur
    if lettre.isdigit():
        print("Lettre incorrecte !")
    else:
        # On parcourt le mot à trouver
        for i in range(len(mot)):
            # Si on trouve une lettre
            if mot[i] == lettre:
                # On ajoute cette lettre dans le mot découvert
                new = list(MotDecouvert)
                new[i] = mot[i]
                MotDecouvert = ''.join(new)
                erreur = 0  # erreur vaut 0 on a trouvé un lettre

        # Si erreur vaut 1, on incrémente le nombre d'erreur
        if erreur == 1:
            compteur = compteur + 1

# Si le mot a été découvert, on affiche BRAVO
if mot == MotDecouvert:
    print("Bravo, vous avez gagné", nom)

# Si le nombre d'erreur est trop grand, on affiche PERDU
elif compteur >= 7:
    print("Vous avez perdu", nom)
    print("Le mot était", mot)
