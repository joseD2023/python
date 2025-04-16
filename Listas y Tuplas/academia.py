#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

asignatura_cursos = ["matematicas", "fisica", "Quimica", "Historia", "Lengua"]

for i in range(len(asignatura_cursos)):
 print(asignatura_cursos[i])
 nota_curso = int(input("Nota del usuario: "))
 print(f"Nota del curso {asignatura_cursos[i]} = {nota_curso}")
