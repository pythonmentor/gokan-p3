import directions


class Labyrinthe:
    def __init__(self):
        self.chemins = []
        self.murs = []
        self.depart = None

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


class Hero:
    def __init__(self, labyrinthe):
        self.labyrinthe = labyrinthe
        self.position = self.labyrinthe.depart
        self.compteur_objets = 0

    def move(self, direction):
        position = direction(position=self.position)
        if position in self.labyrinthe.chemins:
            self.position = position
        if position in self.random_num:
            self.compteurs_objects =+ 1
            # si la nouvelle position est celle d'un objet:
            #    ramasser l'objet

    def objets(self):
        self.random_num = random.sample(self.chemins, k=5)
        print(self.random_num)

class Affichage:
    def __init__(self, labyrinthe, hero):
        self.labyrinthe = labyrinthe
        self.hero = hero

    def afficher(self):
        for y in range(15):
            for x in range(15):
                if (x, y) == self.hero.position:
                    print("H", end="")
                elif (x, y) in self.labyrinthe.chemins:
                    print(" ", end="")
                if (x, y) in self.labyrinthe.murs:
                    print("*", end="")
            print()
        print()


def test():
    labyrinthe = Labyrinthe()
    labyrinthe.charger_structure()
    hero = Hero(labyrinthe)
    affichage = Affichage(labyrinthe, hero)

    while True:
        affichage.afficher()
        choix = input("Ou voulez-vous aller? ")
        if choix in ("haut", "bas", "gauche", "droite"):
            hero.move(getattr(directions, choix))
        elif choix == "quitter":
            break


if __name__ == "__main__":
    test()
