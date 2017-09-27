"""Class Cellules."""


class Cellule:
    """docstring for Cellule."""

    def __init__(self, estVivante):
        """Constructor."""
        super(Cellule, self).__init__()
        self.__estVivante = estVivante

    def affiche(self):
        """Methode Affiche."""
        if self.__estVivante == 1:
            print("@ ", end='')
        else:
            print("- ", end='')

    def getEstVivante(self):
        """Getter estVivante."""
        return self.__estVivante
