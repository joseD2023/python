#Crea una clase Estudiante con un atributo de clase total_estudiantes. Cada vez que crees un estudiante, aumenta ese número. Luego, haz un método de clase que imprima cuántos hay.

class Estudiante:
 total_estudiantes = 0 #atributo de clase no es un atributo de instancia 

 @classmethod #decorador para indicar que es un metodo de la clase
 def sumar_estudiantes(cls):
  cls.total_estudiantes += 1 #incrementamso el atributo de la clase
  print(f"se ha integrado un nuevo alumno ahora hay {cls.total_estudiantes} estudiantes en total")

 #Agrega un método de clase que reinicie el contador a 0, como si comenzara un nuevo ciclo escolar.

 @classmethod 
 def reiniciar_contador(cls):
  cls.total_estudiantes = 0
  print(f"Nuevo año escolar, contador de alumnos reiniciado a {cls.total_estudiantes}")

 @classmethod
 def cantidad_faltantes(cls): 
  faltan = 100 - cls.total_estudiantes
  print(f"faltan {faltan} estudiantes para llegar a los 100 estudiantes")


#Estructura para llamar 
#Clase_metodo

Estudiante.sumar_estudiantes()#se ha integrado un nuevo alumno 

#supongamos que vamos agregar 10 alumnos 

for i in range(10):
 Estudiante.sumar_estudiantes()

#Vamos a probar el metodo de la clase de cuantos estudiantes falta hasta el momento aqui tenemos 10 nos faltaria 90 
 Estudiante.cantidad_faltantes()


#ahora reiniciamos 

Estudiante.reiniciar_contador()
Estudiante.sumar_estudiantes()
