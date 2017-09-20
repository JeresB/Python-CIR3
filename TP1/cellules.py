"""Class Cellules."""


class Cellule(object):
    """docstring for Cellule."""

    def __init__(self, arg):
        """Constructor."""
        super(Cellule, self).__init__()
        self.__estVivante = arg

    def affiche(self):
        """Methode Affiche."""
        if self.__estVivante == 1:
            print("@ ")
        else:
            print("- ")

    def estVivante(self):
        """Getter estVivante."""
        return self.__estVivante
