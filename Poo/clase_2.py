#Clases y Objeto II

class Persona: 
 doctor = "Victor"
#print(Persona.doctor) #Accedemos a la clase y al atributo

#AHORA SI QUEREMOS CREAR UN ATRIBUTO PARA UNA CLASE QUE NO LO TENGA LA SINTAXIS ES 
#objeto.atributo = valor 

class Nombre: #La clase nombre no tiene ningun atributo pero 
 pass 
#AQUI CREAMOS MAS OBJETOS PARA LA PERSON_1 LO QUE QUERAMOS INCLUSO SI NO LO TENEMOS DENTRO DE LA CLASE

person_1 = Nombre()
person_1.nombre = "Jose"
person_1.edad= 20
persona_estudio = "Ingeniereia en Sistemas"
person_1.sexo = "Guatemala"
person_1.genero = "masculino"
print(person_1.nombre)

#PODEMOS CREAR OTRO OBJETO Y HACER NUEVOS ATRIBUTOS CON ELLOS 

person_2 = Nombre()
person_2.estado = "Soltera"
person_2.estudia = True 

print(person_2.estudia)
