#Vamos a ver las funcionalidades de una cadena en python 

#1. Como saber el tipo de dato de una variable podemos usar type(Nombre_variable) o el tipo de dato Ejemplo:

print(type(3)) #Valor Entero
print(type("Hola mundo")) #valor string
print(type(5.3)) #valor Float
print(type(True)) #valor booleano


#VAMOS A CONVERTIR EN MINUSCULA TODA UNA CADENA
cadena_lower = "HOLA MUNDO"
print(cadena_lower.lower()) #Lo que hace Lower es hacer todo en minuscula la cadena de texto 

#COMO MULTIPLICAR UN STRING POR UN INT PARA NO USAR FOR 
s = "Hola mundo"
print(s*3, end=" ") #Lo que va hacer es repetir 3 veces el Hola mundo 
#end="" Lo que vamos hacer es que vamos a dejar un espacio en blanco en cada hola mundo
print()
#COMO VERIFICAR SI ALGUNA ESTA DENTRO DE OTRA 
palabra = "Dios es amor"
encontrar_palabra = "Dios"
print(encontrar_palabra in palabra) #Lo que estamos diciendo es que python verifica si la palabra se encuentra en la otra!! a lo que nos Dara True si es cierto y un False si es falso

#COMO CONVERTIR DE UN TIPO DE VALOR A OTRO 
numero = 5
texto_numero = str(numero) #Solo convierte de un entero a un string el valor y asi sucesivamente 
texto = "10"
numero_texto = int(texto)#Aqui el texto lo convertimos en numero

#COMO ACCEDER A UNA POSICON DE UN STRING COMO SI FUERA UNA MATRIZ 
matriz_palabra = "abcde"
print(matriz_palabra[0]) #recordamos que python comienza en una posicion 0, aqui accedemos a la primera posicon que seria (a)
print(matriz_palabra[1]) #Accedemos a (b)
print(matriz_palabra[-1]) #Accedemos pero desde el ultima posicion (e)
print("--------------------------------------------------------------------------------------------------------") 

#tambien jugar con las posicones 
print(matriz_palabra[0:5:2]) #Accedemos a tres posicones diferentes (ace) aqui lo que se hizo 
#EL inicio seria el 0 y el 5 son la cantidad de letras que hay en la cadena y el 2 en porque vamos a ir de 2 en dos 
print("--------------------------------------------------------------------------------------------------------") 

ejemplo_numero = "123456789"
print(ejemplo_numero[0:len(ejemplo_numero):2]) #Empezaria (1,3,5,7,9)

