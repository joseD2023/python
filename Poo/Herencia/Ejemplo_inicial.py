#Vamos a crear un ejemplo de una clase con herencia simple.

#creamos una clase padre 
class Animal: 
 pass 

#creamos una clase hija 
class Perro(Animal):
 pass 

#De hecho podemos ver como efectivamente la clase Perro es la hija de Animal usando __bases__

print(Perro.__bases__) #<class ´__main__.Animal´>
