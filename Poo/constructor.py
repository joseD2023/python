#vamos a usar constructores para que nos ayuden en el flujo de neustro codigo 

class Perro:
 #ATRIBUTO QUE PERTENECE A LA CLASE Y NO AL CONSTRUCTOR ES DECIR ES CCOMO SI ESE ATRIBUTO NO NECESARIAMENTE ES DEL  METODO EN ESTE CASO CONSTRUCTOR 
 especie = "mamifero"
 def __init__(self, nombre, raza): #El constructor es el def __init__ y es necesario que siempre tenga un self adentro 
   # Vamos a crear los atributos para nuestra clase
   self.nombre = nombre 
   self.raza = raza

#CREAMOS EL OBJETO O INSTANCIA PARA VER COMO FUNCIONA 

mi_perro1 = Perro("Firulais", "Pitubbull")

#PARA ACCEDER ALGUN DE SUS DATOS PODEMOS IMPRIMIRLOS EN PANTALLA 

print(mi_perro1.nombre) #Aqui estamos diciendo que solo quiero saber el nombre de mi perro 1 (resultado: Firulais)

print(mi_perro1.especie) #aqui accedemos al atributo de la clase y el es mamifero y puedo usarlo para todas las instancia ya que esta generada para la clase perro y no solo para el constructor


