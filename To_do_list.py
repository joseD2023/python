# Gestor de Tareas (To-Do List)


tarea = [] #creamos una lista para que guarde todo los dicicionarios


def agregar_tareas():
 global tarea
 #vamos agregar tareas pendientes 
 nombre = input("Nombre de la tareas: ")
 estado = input("Pendiente/completado: ")
 diccionario = {}

 diccionario["nombre"] = nombre
 diccionario["estado"] = estado
 tarea.append(diccionario)


def eliminar_tareas():
 global tarea 
 #Vamos a eliminar las tareas 
 print("+--- LISTADO DE TAREA ---+")
 ver_tareas()
 print("+--- Elimine el numero de tarea: ---+")
 buscar = int(input("Ingrese el nombre de la tarea: "))


 if buscar < 0:
  print("Ingresa un valor mayor a 0")
 else:
  for i in range(len(tarea)):
   if i == buscar:
     tarea.pop(buscar)
   else: 
    print("No encontramos el indice")

 ver_tareas()



def tareas_completas():
 pass 

def guardar_tareas_txt():
 pass 

def ver_tareas():
 for i, j in enumerate(tarea):
  print(f"{i} - {j["nombre"]} [{j["estado"]}]")

while True:
 print("+---- Gestor de Tareas ----+")
 print("1. Ver todas las Tareas  ")
 print("2. Agregar Tarea         ")
 print("3. Eliminar Tarea        ")
 print("4. Marcar Tarea completa ")
 print("5. salir                 ")

 

 try: 
  opc = int(input("Ingrese una Opcion: "))
  if opc == 1: 
   print("Ver Todas las tareas")
   ver_tareas()
  
   

  elif opc == 2:
   print("Agregar una Tarea")
   agregar_tareas()
   ver_tareas()

  elif opc == 3: 
   print("Eliminar una tarea")
   eliminar_tareas()

  elif opc == 4:
   print("Marcar tarea Completa")
 
  elif opc == 5:
   print("Gracias por usar el gestor de tareas. ¡Hasta luego!")
   break
  else: 
   print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")
 except ValueError as e:
  print(f"¡Error! Debe ingresar un número válido. {e}")
