#Cadenas de Caracteres:Asignación, Concatenación, Búsqueda, Extracción, Comparación.

#Asignacion:
mensaje="Hola"
mensaje+=" "
mensaje+="Sofia, tú puedes!"
print (mensaje)

#Concatenación:
mensaje="Sigue"
espacio=" "
nombre="Sofy"
print (mensaje+espacio+nombre)
#Concatenación Numérica:
num1=5
num2=12
resultado=num1+num2
#debemos transformarla a string, this only concatenate str to str,
#no puede concatenar valor de cadena de caracteres con  valor de cadena numérica int.
resultado=str(resultado)
print("El resultado de la suma es : " + resultado)

#Búsqueda:
mensaje= "Hola Sofia"
busqueda_subcadena=mensaje.find("Sofia")
print(busqueda_subcadena)

#Extracción:
mensaje="Buen trabajo chica!"
extraer_subcadena=mensaje[5:12]
print(extraer_subcadena)

#Comparación (True):
mensaje1="Saludos"
mensaje2="Saludos"
print(mensaje1==mensaje2)

#Comparación (False):
mensaje1="Saludos"
mensaje2="Terrícolas"
print(mensaje1==mensaje2)
















