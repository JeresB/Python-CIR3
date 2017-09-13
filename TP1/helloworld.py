"""Hello Wolrd."""


# Mon premier programme
import random
from random import randint
# from monfichier import * # Importe les fonctions de monfichier.py.


def plusMoins(v1, v2):
    """Fonction pour additionner et soustraire."""
    plus = v1 + v2
    moins = v1 - v2
    return plus, moins


print('Hello World!')
variable = 8
print(variable)
variable = 4.5
print(variable)
variable = 'h'
print(variable)
variable = 'bonjour'
print(variable)
entier = int('23')  # Conversion vers un entier.
chaine = str(45)  # Conversion vers une chaine.
chaine = '512'
print(chaine.isdigit())  # Affiche True.
print(chaine.isalpha())  # Affiche False.
valeur = 23
if valeur >= 100:
    print('La valeur vaut plus de 99')
else:
    print('La valeur vaut moins de 100')
valeur = '112'
if not valeur.isdigit() or int(valeur) <= 100:
    print('Ce n\'est pas un entier supérieur à 100')
compteur = 5
while compteur > 0:
    print(compteur)
    compteur -= 1  # Affiche les entiers de 5 à 1.
for index in range(0, 5):
    print(index)  # Affiche les entiers de 0 à 4.

v1 = input('Entrez un premier entier > ')
v2 = input('Entrez un second entier > ')
print('La somme {0} + {1} = {2}'.format(v1, v2, int(v1) + int(v2)))
# Programme principal.
res1, res2 = plusMoins(8, 5)

chaine = 'Bonjour?'
print(chaine.lower())  # Minuscules.
print(chaine.upper())  # Majuscules.
print(chaine.replace('?', '!'))  # Change le ? par un !.
print(len(chaine))  # Donne la taille de la chaine (8).
# Parcours de la chaine.
for letter in chaine:
    print('-> ' + letter)

chaine = 'Bonjour?'
print(chaine[2])  # Affiche : n.
print(chaine[2:4])  # Affiche : nj.
print(chaine[:3])  # Affiche : Bon.
print(chaine[3:])  # Affiche : jour?.
print(chaine[::2])  # Affiche : Bnor (un sur deux).

# Liste ------------------------------------------------------------------
l1 = list()
l1.append('3')
l2 = ['1', 2, 'test']
print(l2[1])  # Affiche : 2.
l2.remove('test')
print(len(l1))  # Affiche : 1.
# Affiche les elements de la liste l2.
for element in l2:
    print(element)
# ------------------------------------------------------------------------


# Dictionnaire -----------------------------------------------------------
d = {}
d['1'] = 'bonjour'
d['test'] = 'salut'
print(d)  # Affiche : {1: 'bonjour', 'test': 'salut'}.
print(d['1'])  # Affiche : 'bonjour'.
del d['test']
print(d.keys())
# ------------------------------------------------------------------------

# Set --------------------------------------------------------------------
s1 = {'apple', 'orange', 'apple', 'pear'}
s2 = {'orange', 'pear', 'cherry'}
print(s1)  # Affiche : {'apple', 'orange', 'pear'}.
s1 - s2  # Elements dans s1 mais pas dans s2.
s1 | s2  # Elements dans s1 ou s2.
s1 & s2  # Elements dans s1 et s2.
s1.add('banana')
s2.remove('pear')
# ------------------------------------------------------------------------

# Fichier ----------------------------------------------------------------
fileRead = open('data.txt', 'r')
lines = fileRead.readlines()
print(lines)
fileRead.close()

fileRead = open('data2.txt')
line = fileRead.readline()
print(line)
fileRead.close()

with open('data.txt') as fileRead:
    lines = fileRead.readlines()

fileWrite = open('data.txt', 'w')
fileWrite.write('v0')
l = ['v1', 'v2', 'v3']
fileWrite.writelines(l)
fileWrite.close()
# ------------------------------------------------------------------------

# Importation de module --------------------------------------------------
print(random.randint(0, 10))  # Affiche un nombre aleatoire entre 0 et 10.

print(randint(0, 10))  # Affiche un nombre aleatoire entre 0 et 10.
# ------------------------------------------------------------------------
