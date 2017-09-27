"""Classe Case."""


class Case:
    """Gère une case de la grille."""

    def __init__(self, x, y, tresorX, tresorY):
        """Constructeur."""
        self.__estVisitee = False
        self.__x = x
        self.__y = y
        self.__tresorX = tresorX
        self.__tresorY = tresorY

    def afficher(self):
        """Methode Afficher."""
        if self.__estVisitee:
            print("  ")
        else:
            print("X ")

    def visite(self):
        """Methode Visite."""
        self.__estVisitee = True
        if self.__x == self.__tresorX and self.__y == self.__tresorY:
            return True
        else:
            return False

    def estVisitee(self):
        """Getteur estVisitee."""
        return self.__estVisitee
