#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

usuario_numer = int(input("Ingrese Un numero: "))

for i in range(usuario_numer, 0, -1):
 print(i, end=",")
 pass