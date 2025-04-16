#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


for x in range(1,11): #Esta parte es la cantidad de tablas es decir que va hacer 10 veces el recorrido es decir que va hacer 10 interaccioens asi como 1 2 3 4 5 6 7 8 9 10 a la cual va a pasar por el otro for
 for i in range(1,11): #en este for lo que va a suceder es que va hacer lo mismo que el anterior pero se va a repetir las cantidades del anterior for
  print(f"{x} x {i} = {(x*i)}", end="\n")
  pass 

