#VAMOS A RECREAR EL JUEGO DEL AHORCADO 
import random

letras_usadas = []
lista_palabras = ["camisa", "pelota", "alaba", "Dios", "corazon"]
palabra_aleatoria = random.choice(lista_palabras)
intentos = 0
letras_correctas = []
aux_lista = ["_" for i in palabra_aleatoria]  # Lista auxiliar para mostrar el progreso


def dibujo_palabra():
    global aux_lista
    for i in range(len(aux_lista)):
        aux_lista[i] = "_"
    print(aux_lista)


def encontrar_palabra():
    global intentos, palabra_aleatoria, letras_correctas, aux_lista

    # 🔁 Reiniciamos variables para cada nuevo juego
    letras_correctas.clear()
    letras_usadas.clear()
    palabra_aleatoria = random.choice(lista_palabras)
    intentos = 0
    aux_lista = ["_" for _ in palabra_aleatoria]

    print("+-------- Bienvenidos Al jugos --------+")
    print(f"La letra a encontrar tiene {len(palabra_aleatoria)} Letras, y usted tiene {intentos} Intentos")
    print("Comenzemoossss")
    print(aux_lista)

    while intentos < 5:
        print(f"Intentos por el momento {intentos}: ")
        letra = input("Ingrese una Letra: ").lower()
        print()

        if letra in palabra_aleatoria:
            if letras_correctas.count(letra) < palabra_aleatoria.count(letra):
                letras_correctas.append(letra)
                print("Letra encontrada")

                for j in range(len(palabra_aleatoria)):
                    if palabra_aleatoria[j] == letra:
                        aux_lista[j] = letra

                print(aux_lista)

                if "_" not in aux_lista: #Si ya no encontramos mas "_" entonces significa que ya ganamos eso signfiica este parte 
                    print("Felicidades has encontrado la palabra")
                    break
                else:
                    continue #Si todavia hay solo continuamos
            else:
                print("La letra ya no puede ser agregada más") #aqui nos va a tirar un error de que ya no podemos ingresar las letras que ya estan ahi agreados y se repiten
                letras_usadas.append(letra)
                intentos += 1
        else:
            intentos += 1
            letras_usadas.append(letra)
            print("Letra incorrecta")
            print(aux_lista)  # 🔄 Mostrar sin reiniciar

        if intentos == 4:
            print("Te queda solo un intento brou")
        elif intentos == 5:
            print(f"Brou Has perdido tus intentos son ahora {intentos} Perdiste brouuu")

        print()
        print(f"Letras usadas por el momento: {letras_usadas}")
        print("Palabras encontradas: ", letras_correctas)
        print()


# Bucle principal del juego
while True:
    print("+--- JUEGO DEL AHORCADO ---+")
    print("+--------- Jugar si/no ------------+")
    opc = input("De su respuesta: ")
    if opc.lower() == "si":
        encontrar_palabra()
    else:
        print("Gracias por jugar")
        break
