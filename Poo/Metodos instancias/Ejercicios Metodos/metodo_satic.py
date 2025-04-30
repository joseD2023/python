#

class Matemticas: 

 @staticmethod 
 def raiz_cuadrada(numero): #metodo que no depende de las instancia ni de las clases esta dentro una clase mas no funciona como una es un metodo normal pero dentro de una clase y ya.
  return numero ** 0.5

 @staticmethod 
 def par_impar(n):
  if n % 2 == 0: 
   print(f"{n} es par")
  else: 
   print(f"{n} es impar")

 @staticmethod 
 def numeros_grande(n,n1,n2):
   if n > n1 and n > n2: 
    print(f"El numero {n} es el mayor")
   elif n1 > n and n1 > n2:
    print(f"El numero {n1} es el mayor")
   else:
    print(f"El numero {n2} es el mayor")


#No es necesario crear una instancia ni nada solo usar Clase_nombre_metodo 

print(Matemticas.raiz_cuadrada(25)) #5
print(Matemticas.par_impar(10)) #10 par
print(Matemticas.numeros_grande(10,20,30)) #30 el mas grande

    
