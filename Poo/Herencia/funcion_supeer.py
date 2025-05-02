#VAMOS A USAR LA FUNCION SUPER PARA HEREDAR EN OTRA CLASE LA CLASE HIJA 

#En pocas palabras, la función super() nos permite acceder a los métodos de la clase padre desde una de sus hijas. Volvamos al ejemplo de Animal y Perro.

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad        
    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)

class Perro(Animal):
 def __init__(self, especie, edad, dueño):
  self.especie = especie 
  self.edad = edad 
  self.dueño = dueño

 #alternativa dos usando la funcion Super herencia super()

 super().__init__(especie, edad):
 self.dueño = dueño 

mi_perro = Perro("mamifero", 5, "hector")




