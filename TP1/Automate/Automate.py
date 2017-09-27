"""Class Automate."""


from Operateur import Operateur
from CelluleVivante import CelluleVivante
from CelluleMorte import CelluleMorte
import sys


class Automate:
    """docstring for Automate."""

    def __init__(self):
        """Constructor."""
        self.__operateur = Operateur()
        self.__iterations = 0
        self.__grille = [[0]*17 for i in range(0, 17)]

    def __creerCellule(self, x, y, vie):
        """Methode Créer cellule."""
        if vie:
            self.__grille[x][y] = CelluleVivante()
        else:
            self.__grille[x][y] = CelluleMorte()

    def __initialiser(self, pathFile):
        """Methode Initialiser."""
        with open(pathFile, 'r') as file:
            for x in range(0, 17):
                for y in range(0, 17):
                    value = file.read(2).strip()
                    if value == '1':
                        self.__creerCellule(x, y, True)
                    else:
                        self.__creerCellule(x, y, False)

    def __afficher(self):
        """Methode Afficher."""
        nom = self.__operateur.getNom()
        ite = self.__operateur.getNombre()
        print(nom, " - Itération numéro :", ite)
        for x in range(0, 17):
            for y in range(0, 17):
                self.__grille[x][y].affiche()
            print('')

    def __itererCellule(self, x, y):
        """Calcul des voisins."""
        nb = 0
        if x > 0 and y > 0:
            if self.__grille[x-1][y-1].getEstVivante():
                nb += 1
        if y > 0:
            if self.__grille[x][y-1].getEstVivante():
                nb += 1
        if y > 0 and x < 16:
            if self.__grille[x+1][y-1].getEstVivante():
                nb += 1
        if x > 0:
            if self.__grille[x-1][y].getEstVivante():
                nb += 1
        if x < 16:
            if self.__grille[x+1][y].getEstVivante():
                nb += 1
        if x > 0 and y < 16:
            if self.__grille[x-1][y+1].getEstVivante():
                nb += 1
        if y < 16:
            if self.__grille[x][y+1].getEstVivante():
                nb += 1
        if x < 16 and y < 16:
            if self.__grille[x+1][y+1].getEstVivante():
                nb += 1

        if nb == 3:
            return True
        if nb < 2 or nb > 3:
            return False
        if nb == 2:
            return self.__grille[x][y].getEstVivante()

    def __iterer(self, iteration):
        """Calcul d'iteration."""
        tab = [[0]*17 for i in range(0, 17)]

        while self.__iterations < int(iteration):
            for x in range(0, 17):
                for y in range(0, 17):
                    tab[x][y] = self.__itererCellule(x, y)
            for x in range(0, 17):
                for y in range(0, 17):
                    if tab[x][y]:
                        self.__creerCellule(x, y, True)
                    else:
                        self.__creerCellule(x, y, False)

            self.__iterations += 1
        self.__iterations = 0

    def lancer(self):
        """Lancement de l'automate."""
        self.__operateur.demanderNom()
        self.__operateur.demanderChaine()
        self.__initialiser(self.__operateur.getFile())

        while int(self.__operateur.getNombre()) != int(-1):
            self.__afficher()
            self.__operateur.demanderNombre()
            if int(self.__operateur.getNombre()) == int(-1):
                print("Arret")
                sys.exit()
            self.__iterer(self.__operateur.getNombre())
