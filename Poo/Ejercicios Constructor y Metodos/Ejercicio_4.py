#Crea una Clase Estudiante con nombre, lista de notas vaciasy metodos de agregar notas, promedio y aprobo 

class Estudiante:
 def __init__(self, nombre):
  self.nombre = nombre 
  self.lista_nota = []
  self.promedio = 0

 def agregar_notas(self, n):
  if n >= 0: 
   self.lista_nota.append(n)
   print("Nota agregada")
  else:
   print(f"Las notas debe ser mayor a cero y no {n}")


 def promedio_notas(self):
  if len(self.lista_nota) > 0: #La cantidad de notas debe ser mayor a 0 para que no tengamos problemas 
   print(sum(self.lista_nota) / len(self.lista_nota))
   self.promedio = sum(self.lista_nota) / len(self.lista_nota)
  else:
   print("Usted Ya perdio mejor dejelo Asi JAJAJAJA ")


 def curso_completo(self):
  if self.promedio == 100:
   print(f"Felicidades {self.nombre} por su promedio de {self.promedio}!!")
  elif self.promedio >= 61:
   print(f"Usted gano el año con un promedio de {self.promedio} ")
  else:
   print(f"Usted acaba de Perder el Año con un promedio de {self.promedio}")


#Vamos a crear una instancia u Objeto 

estudiante1 = Estudiante("Jose De La Rosa")
estudiante1.agregar_notas(100)
estudiante1.agregar_notas(90)
estudiante1.agregar_notas(80)
estudiante1.agregar_notas(95)
#Podemos ver las notas que estan agregadas 
print(estudiante1.lista_nota)

#VAMOS SI NOS HACE EL PROMEDIO 
estudiante1.promedio_notas()
#VAMOS A VER SI GANE EL AÑO SI O NO NELSON
estudiante1.curso_completo()