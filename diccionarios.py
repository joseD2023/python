
tareas = []



def agre():
 global tareas, diccionario
 for i in range(2):
  nombre = input("Nombre de la tareas: ")
  estado = input("Pendiente/completado: ")
  diccionario = {}

  diccionario["nombre"] = nombre
  diccionario["Estado"] = estado
  tareas.append(diccionario)
 print(tareas)

def elimi():
 global tareas 
 buscar = input("Ingrese el nombre: ")




agre()

for i in tareas:
 for clave, valor in i.items():
  if valor == "python":
   print("Has encontrado el valor")
   break
  print(f"clave {clave}: valor {valor} ")




