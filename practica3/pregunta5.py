
class Alumno:
    # inicializamos los atributos
    def inicializar(self,nombre,numero_registro):
        self.nombre=nombre
        self.numero_registro=numero_registro
    def resultado(self,nota,edad) :
        self.nota=nota
        self.edad=edad

 
    # función para imprimir los datos
    def imprimir(self):
               print("Nombre: ",self.nombre)
               print("Numero de registro: ",self.numero_registro)
               print("Nota" ,self.nota)
               print("Edad",self.edad)
    # función para obtener el resultado
    
alumno1=Alumno()
alumno1.inicializar("ivan",8)
alumno1.resultado(14,25)
alumno1.imprimir()

