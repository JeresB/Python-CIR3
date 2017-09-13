"""Min et Max."""


def minMaxBoucle(liste):
    """Fonction pour trouver le min et le max d'une liste avec une boucle."""
    minimum = 99999999
    maximum = -9999999

    for index in range(0, 5):
        liste[index] = int(liste[index])
        if liste[index] > maximum:
            maximum = liste[index]
        if liste[index] < minimum:
            minimum = liste[index]
    return minimum, maximum


def minMaxFonc(liste):
    """Fonction min max d'une liste avec les fonctions min() et max()."""

    return min(liste), max(liste)


taille = 5
liste = list()
compteur = 0
while compteur < taille:
    nombre = input('Entrez un nombre > ')
    try:
        var = int(nombre)
        liste.append(var)
        compteur += 1
    except ValueError:
        print("Nombre incorrect !")

minimum, maximum = minMaxBoucle(liste)

chaine = "".join(str(liste))
print("Le min et le max de", chaine, "sont", minimum, "et", maximum)

minimum, maximum = minMaxFonc(liste)
print("Le min et le max de", chaine, "sont", minimum, "et", maximum)
