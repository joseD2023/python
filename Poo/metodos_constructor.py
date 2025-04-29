#VAMOS A USAR METODOS DENTRO DE NUESTRAS CLASES QUE LOS METODOS MAYORMENTE SON ACCIONES QUE PUEDEN AHCER LOS  OBJETOS 

class Perro: 
 especie = "mamifero"
 def __init__(self, nombre, raza):
  self.nombre = nombre 
  self.raza = raza 

 #VAMOS A CREAR LOS METODOS PARA ESTA CLASE 

 #Un metodo que no recibe parametros en es caso ladrar
 def ladrar(self):
  print("Guau")

 #Un metodo que recibe parametros en este caso caminar, los pasos que da el perro
 def caminar(self, pasos):
  print(f"Caminando {pasos} pasos")

#Ahora creamos una instancia u Objeto 

my_dog = Perro("Firu", "Bulldog")

my_dog.ladrar() #aqui hacemos que el perro ladre en su accion segun el metodo
my_dog.caminar(10) #aqui hacemos o damos el parametro de que debe hacer 10 pasos

