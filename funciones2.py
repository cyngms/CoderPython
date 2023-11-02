# def suma(num1: int, num2: int) -> int:
#     total = num1 + num2
#     return total
#
# print(f"El total de la suma es {suma(2,5)}")
#
# def resta(num1: int, num2: int) -> int:
#     total = num1 - num2
#     return total
#
# print(f"El total de la resta es {resta(2,5)}")

# Dentro de las llaves del print, se pude colocar el orden de los numeros como sea necesario

# def suma(num1: int, num2: int) -> int:
#     total = num1 + num2
#     return total
#
# print(f"El total de la suma es {suma(num2=5,num1=7)}")
#
# def resta(num1: int, num2: int) -> int:
#     total = num1 - num2
#     return total
#
# print(f"El total de la resta es {resta(num2=2,num1=5)}")

# def resta_defecto(num1: int = 2, num2: int = 0) -> int:
#     total = num1 - num2
#     return total
#
# print(f"El total de la resta es {resta_defecto(num1=5, num2=2)}")
# print(f"El total de la resta es {resta_defecto(num1=5)}")
# print(f"El total de la resta es {resta_defecto()}")
#
# def modify(value):
#     value = value * 2
#     return value
#
# value_start = ['Luis', 'Carlos']
# value_modify = modify(value_start)
# print(value_start)
# print(value_modify)

# Modificar los valores de una lista
# def doblar(numeros):
#     for i, n in enumerate(numeros): # enumerate sirve para traer los indices de una lista
#         numeros[i] *= 2
#
# lis_n = [10, 50, 100]
# doblar(lis_n)
# print(lis_n)

# def modify(value):
#     print(id(value))
#     value = value * 2
#     return value
#
# value_start = 2
# value_modify = modify(value_start)
# print(id(value_start))

# *args lista, **kargs diccionario
# def suma(*args, **kwargs) -> int:
#     print(args)
#     print(kwargs)
#     total = 0
#     for key, num in kwargs.items():
#         print(f"sumando la referencia {key}")
#         total += num
#     return total
#
# print(f"El total de la suma es {suma(1,3, ['deas', 'dedfs'], num1=2, num2= 5, num3=2, num4=45)}")

# def suma(*args):
#     mm = args[0] / 1000
#     cm = args[1] / 100
#     m = args[2]
#     total = mm + cm + m
#     return total
#
#
# conversion = suma(*[1, 3, 5])
# print(conversion)

# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num - 1)
#
# print(factorial(3))

# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)
#
# print(fibo(10))