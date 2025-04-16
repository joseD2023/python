#LAS TUPLAS NO SON INMUTABLES COMO LAS LISTAS ES DECIR NO ES TAN FACIL MODIFICARLAS ES ALGO MAS CONCRETO PERMITE ALMACENAR DISTINTOS TIPOS DE DATOS (INMUTABLES:NO CAMBIAN UNA VEZ INICAL )

tupla = (1,2,3,4,5,6,7,8,9) #Tenemos nuestra tupla tipo entero
print(tupla)
tupla_datos_variados = (1,"jose", True, 6.7, False, "Te amos Dios") #Tenemos neustra tupla con varios tipos de datos
print(tupla_datos_variados)

#VAMOS ACCEDER A UNA POSICION EN TUPLAS 

print(tupla_datos_variados[1]) #accedemos la posicion 1 en esta caso Jose

#MODIFICAR UN DATO EN LA TUPLA 
#tupla_datos_variados[1] = "DE JOSE A HECTOR" NO SE VA A PODER VA A TIRAR UN ERROR PORQUE UNA TUPLA NO SE PUEDE MODIFICAR 

print(tupla[-1]) #Vamos acceder al ultimo elemento de la tupla 
print(tupla[-2]) #ahora fuera como si estuvieramos de reversa 

#AHORA PARA UN RANGO EN LA TUPLA PODEMOS HACER ESTO
print(tupla_datos_variados[0:4]) #aqui decimos que inicie en la posicion 0 y llegue a la 4

#PODEMOS HACER EN UNA SOLA LINEA DE CODIGO UNA VARIABLE PARA CADA POSICION PARA LA TUPLA 
tupla_ejemplo = (1,2,3) 
a, b, c = tupla_ejemplo #a b c van a tomar las primera posicones es decir a = 1 b = 2 y asi sucecisvametne 
#LAS VARIABLES DE LAS TUPLAS TIENE QUE SER EL TOTAL DE VALORES QUE TIENE LA TUPLA PARA FUNCIONAR
print(a)
print(b)
print(c)

#PODEMOS UNIR LAS TUPLAS CONCATENANDO 

tupla1 = (1,3,4,5,6)
tupla2 = (7,8,9)
tupla_final = tupla1 + tupla2
print(tupla_final) #Va unir las tuplas 

x


