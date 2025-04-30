#Los metodos de instancias son aquellos que usamos dentro de las clases normalmente recibiendo como parametro 
#self que hace referencia a la instancia de la clase que se esta creando. 
#EJEMPLO 

class Persona: 
 def __init__(self, nombre, edad):
  self.nombre = nombre 
  self.edad = edad 

 def saludar(self): #Esta es la instancia de la clase usando self 
  print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")



persona1 = Persona("Juan", 30) #creamos la instancia 

persona1.saludar() #llamamos al metodo de la instancia


#Los metodos de instancia normal 
#pueden acceder a otros metodos 
#Pueden acceder y modificar los atributos del objeto.
#