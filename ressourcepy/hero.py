class Hero:
    def __init__(self, labyrinthe):
        self.labyrinthe = labyrinthe
        self.position = self.labyrinthe.depart
        self.compteur_objets = []
        self.quete = None

    def move(self, direction):
        position = direction(position=self.position)
        if position in self.labyrinthe.chemins:
            self.position = position
        if position in self.labyrinthe.objets_positions:
            self.ramasser_objets()
        if position == self.labyrinth.arriver.position:
            self.objectif()

     def ramasser_objets(self):
        # ramasser objets et bouger ca position
        self.ramasser_objets.append(self.position)
        compteur_objets = self.labyrinthe.objets_positions.index(self.position)
        self.labyrinthe.objets[compteur_objets].position = (self.labyrinthe.chemins, compteur_objets)

    def objectif(self):
        if len(self.compteur_objets) == "3":
            self.quete = "GAGNER"
        else :
            self.quete = "PERDU"
