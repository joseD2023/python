#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def numeros_impares(n): #esperamos una cantidad numerica 
  for i in range(n): #lo colocamso para recorrer el for 
   if i % 2 != 0: #si el residuo es diferente de 0 entonces es un numero impar si fuera igual a 0 seria par 
    print(f"Numero impar {i}") #imprimimos el numero par 

numero_usuario = int(input("Ingrese un numero entero: "))

for x in range(1, numero_usuario, 2): #ya no colocamos comprobacion de numeros negativos porque estamso diciendo que comienze en 1 y el numero usairo +1  o solo podemos usar numero usuario es decir que le estamos diciendo que se corra 1 osea que no inicie en 0 si no es 1 y el 2 que vaya en 2 en dos para seguir con los impares 
  print(x, end=",")
 #numeros_impares(numero_usuario)



 






