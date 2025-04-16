#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

numero_trinagulo = int(input("Ingrese un numero:"))

for i in range(1, numero_trinagulo+1, 2): #En este apartado lo que hace es que los numero sean impares osea si colocamos 5 seria 1 3 5 hasta ahi llegaria el for
 for j in range(i, 0, -2):#ahora lo que hace esto es hacer que el numero osea i vaya en retroceso es decir si i vales 3 entonces va a retroceder descendentemente hacia abajo por eso del -2 porque va en 2 en 2 retrocediendo hasta llegar a 0
  print(j, end=" ")
 print("")

