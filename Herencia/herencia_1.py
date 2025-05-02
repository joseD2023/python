#vamos a ver una herenica simple en python 

class Animal: 
 def __init__(self, nombre):
  self.nombre = nombre 

 def hablar(self):
  return f"{self.nombre} hace un sonido." #metodo self dentro de la clase animal ahora vamos a heredar este metodo

#clase que hereda animal 
class Perro(Animal): 
 def hablar(self): 
  return f"{self.nombre} dice Guauuuuuuu!" #metodo que sobreescribe el metodo de la clase padre 

class Gato(Animal):
 def hablar(self):
  return f"{self.nombre} dice Miau!!"


mi_perro = Perro("Firulais")
mi_gato = Gato("Mishi")


print(mi_perro.hablar())
print(mi_gato.hablar())


