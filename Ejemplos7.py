# Este es el trabajo con strings
# Hola Luis como estas
# txt = input("ingrese cualquier valor: ")

# print(f"El texto en mayuscula es: {txt.upper()}, esto es para coder")
# print(f"El texto en minuscula es: {txt.lower()}, esto es para coder")
# print(f"El texto en capitalize es: {txt.capitalize()}, esto es para coder")
# print(f"El texto en title es: {txt.title()}, esto es para coder")
# print(f"La cantidad de caracteres 'a' es: {txt.lower().count('a')}, esto es para coder")
# print(f"Indice del string es: {txt.find('Luis')}, esto es para coder")
# print(f"Indice del strinf es: {txt.rfind('a')}, esto es para coder")
# print(f"La cadena separada por espacio es: {txt.split()}")
# print(f"La cadena separada es: {txt.split('a')}")
# print(f"Eliminando los ----- laterales: {txt.strip('-')}")
# print(f"Reemplanzando valores: {txt.replace('a','A')}")

# Funciones de Listas
# lista = [1, 2, 3, 4, 5]
# print(lista)
# lista.clear() - elimina todos los elementos
# lista.insert(0,0)
# lista.insert(5,6) # agrega un item a la lista en un indice especifico
# print(lista)
# Reverse - dar la vuelta a la lista
# lista.reverse()
# print(lista)
# Sort - ordenar una lista de menor a mayor
# value = [5, 87541, 54.2, 97, -10, -128]
# value.sort()
# print(value)
# value.sort(reverse = True)
# print(value)

# Funciones de Conjuntos
# Copy - devuelve una copia del set
# set1 = {1, 2, 3, 4}
# set2 = set1.copy()
# print(set2)
# Isdisjoint - comprueba si el set es distinto
# set1 = {1,2,3}
# set2 = {3,4,5}
# set1.isdisjoint(set2)
# Issubset - comprueba si el set es subset de otro set
# set3 = {-1, 99}
# set4 = {1, 2, 3, 4, 5}
# set3.issubset(set4)
# Issuperset - comprueba si el set es contenedor de otro set
# set1 = {1,2,3}
# set2 = {1,2}
# set1.issuperset(set2)
# Union - une un set con otro y devulve el resultado en un nuevo set
# set1 = {1,2,3}
# set2 = {3,4,5}
# set1.union(set2)
# Difference - devuelve un set de items diferentes entre cada set
# set1 = {1,2,3}
# set2 = {3,4,5}
# set1.difference(set2)
# Diference_update - asigna como nuevo valor los items diferentes
# set1 = {1,2,3}
# set2 = {3,4,5}
# set1.difference_update(set2)
# print(set1)
# Ahora set1 vale {1, 2} porque es la diferencia que tenia con set2
# Intersection - devuelve un set de items iguales entre cada set
# set1 = {1,2,3}
# set2 = {3,4,5}
# set1.intersection(set2)
# Intersection_update - asigna como nuevo valor los items en comun
# set1 = {1,2,3}
# set2 = {3,4,5}
# set1.intersection_update(set2)
# print(set1)
# Ahora set1 vale los items en comun con set2 --> {3}

# Funciones de Diccionarios
# Get - busca un elemtno a partir de su key --> dict.get(key, "valor por defecto")
# colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }
# colores.get("rojo", "no hay clave rojo")
# Keys - traer todas las claves de un diccionario en caso de desconocerlas --> dict.keys
# colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }
# colores.keys()
# Values - trae todos los valores de un diccionario --> dict.value()
# colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }
# colores.values(['yellow', 'blue', 'green'])
# Items - crea una lista con valve y valor de los items de un diccionario --> dict.items()
# colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }
# colores.items()
# for clave, valor in colores.items():
#     print(clave, valor)

#Ejemplo de clase N°1

# txt = ("gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos "
#        "pies le corrigió Troop&strawberry menea la cabeza como disgustado..."
#        "-agrega el comentarista")
# lineas = txt.split("&")
# print(lineas)
# for i, linea in enumerate(lineas):
#     lineas[i] = linea.capitalize()
#     if i == 0:
#         lineas[i] = lineas[i] + "..."
#     else:
#         lineas[i] = "- " + lineas[i] + "."
# print(linea)
# for linea in lineas:
#     print(linea)

# Ejemplo de clase N°2
# A. Con esta funcion podemos ver como se unen los set y regresan un set nuevo
# my_set_1 = set([1, 2, 3])
# my_set_2 = set([3, 4, 5])
# my_new_set = my_set_1.union(my_set_2)
# print(my_new_set)
# B. Esta funcion nos devuelve un set compuesto por los elementos en comun entre ellos
# my_set_1 = set([1, 2, 3])
# my_set_2 = set([3, 4, 5])
# my_new_set = my_set_1.intersection(my_set_2)
# print(my_new_set)
# C. Devuelve un set con items diferentes entre cada set
# my_set_1 = set([1, 2, 3])
# my_set_2 = set([3, 4, 5])
# my_new_set = my_set_1.difference(my_set_2)
# print(my_new_set)

# Ejemplo de clase N°3

# monedas = {'Dolar': '$', 'Euro': '€', 'Libra': '£'}
# consult = input('Ingrese el nombre de la divisa: ')

# Ejemplo de clase N°4

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
lista_n = list(set(lista)) # --> Sin duplicados (1)
lista_n.sort(reverse=True) # --> Orden de mayor a menor (2)
copy_list = lista_n[:]
for elemento in copy_list:
    if elemento % 2 == 1:
        lista.remove(elemento)
print(lista_n) # --> lista sin numero impares (3)
print(sum(lista_n)) # --> suma de la lista (4)
lista_n.insert(0,109) # --> insertar la suma en primer lugar de la lista (5)
print(lista_n) # --> lista modificada (6)