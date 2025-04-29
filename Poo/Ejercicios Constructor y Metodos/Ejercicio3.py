#Crea una clase Rectangulo que tenga atributos base, altura y metodos area y perimetro 

class Rectangulo: 
 def __init__(self, base, altura):
  self.base = base 
  self.altura = altura 

 def calcular_area(self):
  return self.base * self.altura
  pass 
 def calcular_perimetro(self):
  return 2*(self.base + self.altura)


#Creamos la instancia u Objeto 

rectangulo = Rectangulo(2,2)

print(f"El area del Rectangulo es: {rectangulo.calcular_area()}")
print(f"El perimetro del Rectangulo es: {rectangulo.calcular_perimetro()}")

