# Errores sintacticos - relacionados con la escritura
# print("Hola"
# Errores semanticos - ligados al funcionamiento  y dependen de la situacion
# lista = []
# lista.pop() -> no se puede sacar un elemento de una lista vacia

# Errores semanticos
# n = input("Ingresar n:\n")
# m = 4
# print(f"---> {n}/{m} = {n/m}")

# Version correcta
# n = float(input("Introduce un numero:"))
# m = 4
# print("{}/{} = {}".format(n,m,n/m))

# Ejemplo
# def div(a: int, b: int) -> float:
#     return a / b
#
# n1 = int(input("Ingrese un numero: "))
# n2 = int(input("Ingrese otro numero: "))
#
# while n2 == 0:
#     print("Este valor debe ser diferente de 0")
#     n2 = int(input("Ingrese nuevamente el valor: "))
#
# print(div(n1, n2))

# def div(a: int, b: int) -> float:
#     if b == 0:
#         return
#     return a/b
# div(1,0)

# Excepciones - errores destacados durante la ejecucion
# Try-Except -> nos permite controlar situaciones excepsionales que generalmente darian error
# n1 = input("Ingrese el primer valor: ")
# n2 = int(input("Ingrese el siguiente valor: "))

# while True:
#     n1 = input("numero 1: ")
#     n2 = input("numero 2: ")
#     try:
#         n1 = int(n1)
#         n2 = int(n2)
#         div = n1 / n2
#         div_0 = div/0
#         break
#
#     except ValueError:
#         print("Ingrese un numero valido ")
#     except ZeroDivisionError:
#         print("Por favor ingrese un numero distinto de cero")

# Ejercicio
# def div(a: int,b: int) -> float:
#     try:
#         div = a/b
#         return div
#     except ZeroDivisionError as err:
#         return ("Cannot divide using 0")
#
# num1 = 5
# num2 = 0
# print(div(num1,num2))


