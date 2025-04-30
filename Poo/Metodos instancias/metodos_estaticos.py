#AHORA VAMOS A VER METODOS ESTATICOS SE PUEDE DEFINIR CON EL DECORADOR @staticmethod y no aceptan como parametro ni la instancia ni la clase.Es por ello por lo que no pueden modificar el estado ni la clase ni de la instancia  pero por supuesto pueden aceptar parametros de entrada.abs

#EJEMPLO 

class Calculadora: 

 @staticmethod
 def sumar(a, b):
  return a + b 

 @staticmethod 
 def restar(a, b):
  return a - b 

#No necesitamos crear una instancia u objeto usamos la clase directamente. 

print(Calculadora.sumar(5,4)) #9
print(Calculadora.restar(5,4)) #1 

#En este caso no es necesario crear una instancia para acceder a los metodos estaticos, ya que no dependen de la instancia ni de la clase. 

#En pocas palabras es como si tuvieramos metodos normales pero dentro de una clase pero que no depende de la clase por eso le colcoamso el decorador staticmethod para decir hey mira aqui pongo un metodo dentro de la clase que lo puede usar pero no necesitas ni crerar un constructor ni nada. solo usalo y ya 