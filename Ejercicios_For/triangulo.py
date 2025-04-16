#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

numero_entero = int(input("Ingrese un numero entero: "))

for r in range(numero_entero): #inicio final paso
 print("*"*r) #mutilplicamos r por cada pasada, es decir lo que hacemos es que r valga 1 2 3 4 y ocasionando que se multiplique por la forma
