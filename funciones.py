# Agrupaciones optimas del codigo - Funciones
# len('Hola') # --> Longitud
# def --> crear funciones definidas

# def sin return
# def saludar_estudiante(nombre):
#     print(f"Hola como estas {nombre}?")
#
# saludar_estudiante("Carlos Vega")

# def con return
# def saludar_estudiante(nombre):
#     mensaje = f"Hola como estas {nombre}?"
#     return mensaje
#
# print(saludar_estudiante("Barbabra Lopez"))

# def con input y sin return
# nombre = str(input("Ingrese su nombre:"))
# def saludar_estudiante(nombre):
#     print(f"Hola, como va tu dia {nombre}?")
#
# saludar_estudiante(nombre)

# var_test = 10
# def test():
#     print(var_test)
#
# test()
# print(var_test)

# def con dos o mas parametros
# def suma(n1, n2):
#     total = n1 + n2
#     mensaje = f"El resultado es el siguiente: {total}"
#     return mensaje
# num1 = int(input('Ingrese la cantidad: '))
# num2 = int(input("Ingrese la siguiente cantidad: "))
# print(suma(num1,num2))

# Ejercicio 1
# def bienvenida(city):
#     mensaje = f"¡Hola bienvenido a {city}"
#     return mensaje
# bienvenida('Ciudad de Mexico')
# print(bienvenida("Ciudad de Mexico"))

# Ejercicio 2
# def calificar(promedio):
#     lista = [7, 8, 9, 7, 5, 10, 4, 6, 10]
#     return sum(lista)/len(lista)
#
# print(calificar("promedio"))

# Ejercico 3
def es_multiplo(n1,n2):
    if n1 % n2 == 0:
        return True
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
if es_multiplo(num1,num2):
    print(num1, "es multiplo de", num2)
else:
    print(num1, "no es multiplo de", num2)
