#vamos a usar metodos genericos en herencias 

class Animal:
 def __init__(self, especie, edad):
  self.especie = especie 
  self.edad = edad 

  #Metodo generico pero con implementacion particular 

 def hablar(self):
  pass 
 def moverese(self):
  pass 
 def describeme(self):
  print(f"soy un animal tipo", type(self).__name__)


perro1 = Animal("Mamifero", 5)

perro1.describeme() #soy un animal tipo y el type (osea a qeu parte de la clase pertenezco)
 