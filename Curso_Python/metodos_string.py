
#METODO CAPITALIZE() DEVUELVE LA PRIMERA LETRA EN MAYUSCULA 
letra_cadena ="jose victor" #tenemos el nombre con minuscula al principio 
print(letra_cadena.capitalize()) #Nos va hacer que la primera letra salga en mayuscula

#METODO LOWER() CONVIERTE TODOS LOS CARACTERES ALFABETICOS EN MINUSCULA 
palabra_mayuscula = "JOSE VICTOR DE LA ROSA"
print(palabra_mayuscula.lower()) #Va a convertir toda la cadena en minuscula

#METODO UPPER() CONVIERTE TODOS LOS CARACTERES ALFABETICOS EN MAYUSCULAS 
palabra_mayuscula = "palabra en minuscula a mayuscula con upper"
print(palabra_mayuscula.upper()) #Me va convertir todos la cadena en mayusculas

#METODO  SWAPCASE() CONVIERTE TANTO MAYUSCULAS COMO MINUSCULAS TENEMOS UNA VARIABLE CON AMBAS PROPIEDADES MINUSCULAS Y MAYUSCULAS 
palabra_prueba = "Mi mama Me mImA"
print(palabra_prueba.swapcase())

#METODO COUNT SIRVE PARA CONTAR EL NUMERO DE VECES QEU APARECE UN TEXTO EN UNA CADENA 
palabra_nueva = "Blanca Nieves"
print(palabra_nueva.count("a")) #Nos va el numero de veces que aparece la palabra a en la cadena de texto Blanca nieves en este caso son 2 veces 

#METODO ISALNUM() VERIFICA SI EN EL TEXTO SE ENCUENTRA ALGUN CARCATER ESPECIAL COMO @ & ESTOS TIPOS DE CARACTERES 
palabra_especial = "Josevictordelarosa@gmail.com"
print(palabra_especial.isalnum()) #Me va tirar false porque contiene un @ no solo esta formado con caracteres alfanumericos(lo que hace isalnum() es comprobar si hay solo caracteres alfanumericos sin caracteres especiales)

#METODO ISAPHA() ES UN METODO DEVULVE TRUE SI TODOS LOS CARACTERES SON ALFABETICOS DELO CONTRARIO FALSE
palabra_alafabetica = "abcdef" #True
palabra_alfa_numerico = "ab123" #False
print(palabra_alafabetica.isalpha(), palabra_alfa_numerico.isalpha())

#METODO FIND() PARA ENCONTRAR UNA POSICON DE ALGUNA LETRA 
palabra_posicion = "Ingenieria in sistema"
print(palabra_posicion.find("in"))

#METODO REPLACE() INTERCAMBIA UN VALOR POR OTRO 
palabra_original = "Hola Mundo"
cambiar = "Espacio"
print(palabra_original)
print(palabra_original.replace(palabra_original, cambiar)) #Tenemos un Hola mundo y lo replazamos por espacio 

#METODO ISNUMERIC() DEVUELVE TRUE O FALSE SI LA VARIABLE TIENE TEXTO O NUMERO 
variable = "Soy texto"
print(variable.isnumeric()) #Nos va arrojar False porque es un texto y no un numero variable

#METODO SPLIT() QUE SIRVE PARA SEPARAR CADENAS 
palabra_sp = "Te amo Dios" 
palabra_sp2 = "Te-amo-Dios"
print(palabra_sp.split(" ")) #En donde encuentre une espacio en blanco lo va a separar 
print(palabra_sp.split("-")) #En donde encuentre - los va a separar


