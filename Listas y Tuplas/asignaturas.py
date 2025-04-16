#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

asignaturas = []

for agregar in range(10):
 materia = input("Materias: ")
 asignaturas.append(materia)

print(asignaturas)