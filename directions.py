def haut(position):
    x, y = position
    return (x, y-1)

def bas(position):
    x, y = position
    return (x, y+1)
    
def droite(position):
    x, y = position
    return (x+1, y)

def gauche(position):
    x, y = position
    return (x-1, y)