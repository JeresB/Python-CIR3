"""Class Operateur."""


import sys


class Operateur:
    """docstring for Operateur."""

    def __init__(self):
        """Constructor."""
        self.__nom = 'Jeres'
        self.__nombre = 0
        self.__chaine = ''

    def demanderNom(self):
        """Methode Demander Nom."""
        self.__nom = input('Quel est votre nom ? ')

    def demanderNombre(self):
        """Methode Demander Nombre."""
        try:
            self.__nombre = input('De combien d’itérations voulez-vous avancer ?! ')
        except SyntaxError:
            self.__nombre = -2

    def demanderChaine(self):
        """Methode Demander Chaine."""
        while self.__chaine == '':
            self.__chaine = input('Quel est le nom du fichier à lire ? ')

    def getNom(self):
        """Getteur Nom."""
        return self.__nom

    def getNombre(self):
        """Getteur Nombre."""
        return self.__nombre

    def getFile(self):
        """Getteur File."""
        return self.__chaine
