#Crea un clase Cuenta Bancaria con atributos titular saldo y metodos depositar, retirar, mostrar saldo, Asegúrate de que no se permita retirar más de lo disponible.

class Cuenta_bancaria:
 def __init__(self, titular): #titular el nombre de la persona 
  self.titular = titular 
  self.saldo = 0

 def depositar(self, monto):
  if monto >= 0:
   self.saldo += monto
  else:
   print(f"El Monto no es valido {monto}")
   
  
 def retirar(self, dinero):
  if self.saldo >= dinero:
   self.saldo -= dinero
   print(f"Monto de Retiro {dinero}")
  else:
   print(f"No puede retirar mas de lo que no tiene :( saldo total {self.saldo} ")

 def mostrar_saldo(self):
  print(f"Saldo de la cuenta de la persona {self.titular} es: {self.saldo}")


#Creamos una instancia u Objeto 

while True: 
 print("1. Crear Cliente    ")
 print("2. Depositar        ")
 print("3. Retirar          ")
 print("4. Estado de Cuenta ")
 print("5. Salir            ")

 opc = int(input("Ingrese Opc: "))

 if opc == 1: 
  nombre_clinete = input("Nombre del cliente: ")
  cliente = Cuenta_bancaria(Cuenta_bancaria)
 elif opc ==2: 
  deposito = int(input("Cuanto desea depositar: "))
  cliente.depositar(deposito)

 elif opc == 3: 
  retiro = int(input("Cuanto desea retirar: "))
  cliente.retirar(retiro)
 elif opc == 4: 
  cliente.mostrar_saldo()
 elif opc == 5: 
  break
 else: 
  print("OPcion invalida")