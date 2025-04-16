#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Frase Usuario: ")
letra = input("Letra a Buscar: ")
cont = 0

for x in frase:
 if x == letra:
  cont += 1 #Va sumando la cantidad de veces que la letra va apareciendo
 print(x, end="")

print(f"La cantidad de veces que aparece la letra {letra} = {cont}")

