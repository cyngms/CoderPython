#Metodos de coleccion
#Strings
#Upper - mayusculas
phase = "Hola Mundo"
phase.upper()
print(phase)
#Lower - minusculas
lock = "HOLA AMIGO"
lock.lower()
print(lock)
#Capitalize - Primer mayuscula
flower = "hola mundo"
flower.capitalize()
print(flower)
#Title - Mayuscula en cada palabra
gloss = "HOla munDO"
gloss.title()
print(gloss)
#Count - cuantas veces aparece un caracter
phil = "Hola Mundo esta cadena tiene muchas a"
phil.count("a")
print(phil)
#Find - en que lugar de la cadena aparece
hell = "Hola mundo esta cadena tiene muchas a"
hell.find("esta")
print(hell)
#Rfind - indica la ultima vez que aparece en la cadena
treat = "Hola amigo como estas amigo!"
treat.rfind("amigo")
print(treat)
#en caso de que no lo encuentre en la cadena, indica un -1
#Split - devuelve una lista con la cadena separada
cadena = "Hola amigo como estas el dia de hoy"
cadena.split()
print(cadena)
#Join - separa los caracteres
tooth = "Hola mundo"
" ".join(tooth)
print(tooth)
#Strip - borra los caracteres delante y detras de la cadena
red = "---------- Hola mundo ----------"
red.strip("-")
print(red)
#Replace - reemplaza caracteres indicados de la cadena
gray = "Hola mundo, como anda todo"
gray.replace("o","e",2)
print(gray)