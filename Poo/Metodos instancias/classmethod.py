#Ahora veremos otro metodo que podemo susar dentro de las clases que es el metodo CLASSMETHOD. 
#A diferencia de los métodos de instancia, los métodos de clase reciben como argumento cls, que hace referencia a la clase. Por lo tanto, pueden acceder a la clase pero no a la instancia.

#Ojito dice que podemos acceder a la clase pero no a la instancia, es decir, no podemos acceder a los atributos de la instancia, pero si a los atributos de la clase. 

class Panaderia: 
 panes_horneados = 0 #ATRIBUTO DE CLASE (este atributo pertenece a la clase mas no a la instancia es decir no podemos acceder a el desde la instancia), no es creado en base a un constructor. 

 
 @classmethod #decorador para indicar que es un metodo de la clase
 def hornear_pan(cls):
  cls.panes_horneados += 1 
  print(f"se horneo un pan. total {cls.panes_horneados} panes horneados")

#vamos a hornear 3 panes 

Panaderia.hornear_pan() #se horneo un pan total 1 
Panaderia.hornear_pan() #se horneo un pan total 2
Panaderia.hornear_pan() #se horneo un pan total 3

#No necesitamos un constructor para acceder a los atributos de la clase, ya que no es necesario crear una instancia para acceder a los atributos de la clase. 

#en terminos generales no es necesario crear un objeto para acceder a los atributos de la clase con el hecho de crear una metodo y colocarle cls ya podemos acceder a los atributos.
