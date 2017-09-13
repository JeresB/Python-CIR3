"""Pendu."""


from random import choice
from sys import argv

mot = choice(open(argv[1]).readlines()).strip()
print(mot)
