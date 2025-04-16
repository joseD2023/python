#VAMOS A RECREAR EL JUEGO DEL AHORCADO 
import random

letras_usadas = []
lista_palabras = ["camisa", "pelota", "alaba", "Dios", "corazon"]
palabra_aleatoria = random.choice(lista_palabras)
intentos = 0
letras_correctas = []
aux_lista = ["_" for i in palabra_aleatoria] #Vamos a usar una lista nueva auxiliar que nos ayude mejor a la comparacion en nuestro 

def dibujo_palabra():
 global aux_lista
 for i in range(len(aux_lista)):
  aux_lista[i] = "_"
 print(aux_lista)


def encontrar_palabra():
 global intentos, palabra_aleatoria, letras_correctas
 print("+-------- Bienvenidos Al jugos --------+")
 print(f"La letra a encontrar tiene {len(palabra_aleatoria)} Letras, y usted tiene {intentos} Intentos")
 print("Comenzemoossss")
 dibujo_palabra()


 while (intentos < 5):
  print(f"Intentos por el momento{intentos}: ")
  letra = input("Ingrese una Letra: ").lower()
  print()
  if letra in palabra_aleatoria:
   if letras_correctas.count(letra) <= palabra_aleatoria.count(letra) : #Comparamos para que no se utilice tantas veces la letras cuando ya se llego a su limite es decir si en la palabra original hay 2 "a" no puede ingresar 3 el usuario y decir que esta bien entonces esto hara que no pase eso que tome la 3 "a" como buena
    letras_correctas.append(letra)
    print("Letra encontrada")

    for j in range(len(palabra_aleatoria)):
     if palabra_aleatoria[j] == letra:
      aux_lista[j] = letra
    
    print(aux_lista)


    if len(letras_correctas) == len(aux_lista):
     print("Felicidades has encontrado la palabra")
     letras_correctas.clear()
     letras_usadas.clear()
     break
    else: 
     continue
   else:
    print("La letra ya no puede ser agregada mas")
    letras_usadas.append(letra)
    intentos += 1
  else: 
   intentos += 1 
   letras_usadas.append(letra)
   print("Letra incorrecta")
   dibujo_palabra()

  if intentos == 4:
   print("Te queda solo un intento brou")
  elif intentos == 5: 
   print(f"Brou Has perdido tus intentos son ahora {intentos} Perdiste brouuu")
   letras_correctas.clear()
   letras_usadas.clear()


  print()
  print(f"Letras usadas por el momento", letras_usadas)
  print("Palabras encontradas: ", letras_correctas)
  print()


while True:
 print("+--- JUEGO DEL AHORCADO ---+")
 print("+--------- Jugar si/no ------------+")
 opc = input("De su respuesta: ")
 if opc.lower() == "si":
  encontrar_palabra()

 else: 
  print("Gracias por jugar")
  break




