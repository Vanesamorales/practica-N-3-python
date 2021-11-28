class Circulo:
   pi = 3.14159                     # Atributo de clase
   def __init__(self, radio):
         self.radio = radio           # Atributo de instancia
   def area(self):
       return Circulo.pi * self.radio ** 2
c1=Circulo(2)


print(c1.area())
