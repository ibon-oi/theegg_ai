class Cow:
    #clase de la vaca
    def __init__(self, id, weight, milk):
        self.id = id
        self.weight = weight
        self.milk = milk

    def print(self):
        print("Vaca %d de %d kilos que produce %d litros" %
              (self.id, self.weight, self.milk))