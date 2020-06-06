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
