#Crear una Clase llamada Auto con los atributos marca modelo y encendido (inicialmente False)
#Metodos encender() Apagar() Estado()


class Auto:  #Creamos la clase Auto
 def __init__(self, marca, modelo): #Hacemos nuestro constructor en el cual solo va a tener 2 parametros 
  self.marca = marca 
  self.modelo = modelo
  self.encendido = False  #Nuestro atributo encendido esta en False porque el auto no esta encendido 

 #Vamos a Crear los metodos 
 def encender(self): #Creamos el metodo encender que hace que nuestro auto encienda 
  self.encendido = True 

 def Apagar(self): #Creamos el metodo apagar que hace que nuestro auto se apague 
  self.encendido = False

 def estado(self): #En nuestro estado colocamos un condicional para ver si mi auto esta encendido o apagado
  if self.encendido == False:
   print("Mi auto esta apagado...")
  else: 
   print("Mi auto esta encendido")


#Vamos a crear una instancia u Objeto 
mi_auto = Auto("Toyota", "XLR8")
mi_auto.encender()
mi_auto.estado()
mi_auto.Apagar()
mi_auto.estado()