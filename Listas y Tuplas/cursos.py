#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

cursos = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

for ver in range(len(cursos)): #len para ver la cantidad o longitud de la lista en este caso 5 cursos 
 print(f"yo estudio {cursos[ver]}") #recordemos que podemos acceder a la lista nombre de la valirable y la posicion en los corchetes

