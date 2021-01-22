class pokemon:
    vida = 100
    def __init__(self, nombre, ataque):
        self.nombre = nombre
        self.ataque = ataque

    def win(self):
        print("Ha ganado ", self.nombre.upper())
    def lost(self):
        print("Ha perdido ", self.nombre.upper())
    def life(self):
        print(self.nombre," tiene una vida de ", self.vida)