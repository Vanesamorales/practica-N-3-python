class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
c1=Rectangulo(4,3)
print(c1.area())