#Crea una clase Persona con atributos nombre y edad. Crea un método que diga "Hola, me llamo <nombre> y tengo <edad> años".

class Persona:
 def __init__(self, nombre, edad):
  self.nombre = nombre 
  self.edad = edad 

 def saludar(self):
  print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

 #Agrega un método que diga si la persona es mayor de edad o no.
 def es_mayor_de_edad(self):
  if self.edad >= 18: 
   print(f"{self.nombre} es mayor de edad. ")
  else: 
   print("Es menor de edad aun")
 def cumplir_anios(self): 
  self.edad +=1 
  print(f"{self.nombre} ha cumplido años y ahora tiene  {self.edad} años")


persona1 = Persona("Jose", 20) #creacion de instancia
persona2 = Persona("Daniel", 17)

persona1.saludar()

persona1.es_mayor_de_edad()
persona2.es_mayor_de_edad()

for i in range(3):
 persona1.cumplir_anios()