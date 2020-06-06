from ressourcepy import hero
from ressourcepy import gardien
from ressourcepy import objets
from ressourcepy import directions
from ressourcepy import affichage

class Labyrinthe:
    def __init__(self):
        self.chemins = []
        self.murs = []
        self.depart = None
        self.arriver = None
        self.gardien = None
        self.hero = None

    def charger_structure(self):
        with open('exo3.txt', 'r') as fichier:
            ligne_n = 0
            for ligne in fichier:
                colon_n = 0
                for character in ligne:
                    if character == ".":
                        self.chemins.append((colon_n, ligne_n))
                    elif character == "#":
                        self.murs.append((colon_n, ligne_n))
                    elif character == "D":
                        self.depart = (colon_n, ligne_n)
                        self.chemins.append((colon_n, ligne_n))
                    colon_n = colon_n + 1
                ligne_n = ligne_n + 1


        self.objets_positions = random.sample(
        set(self.paths)  {self.depart.position, self.arriver.position},
        objets = 3
        nom = ['seringue', 'aiguille', 'tube']
