# 1.- Abrir el archivo (Obligatorio)
#   a. Ruta del archivo
#   b. Permisos que se van a brindar al archivo
#       a --> adicion al archivo
#       w --> sobreescritura
#       r --> lectura
# 2.- Escribir el archivo
# 3.- Cerrar el archivo (Obligatorio)

# fil = open("usuario.csv", "a")
# fil.write("Cynthia4, Guadalupe4, Munoz4, Solis4, 224\n")
# fil.close()

# Lectura
#     read --> Lectura completa
#     readline --> solo una linea
#     readlines --> iterable con la lectura de todas las lienas
# with open("usuario.csv") as f:
#     # print(f.read())
#     # print(f.readline())
#     i = 0
#     for line in f.readlines():
#         print(line)
#         i += 1
#         if i == 2:
#             print('se encuentra en la linea 2')


# JSON en escritura
import json
# user_dic = {
#     "estudiantes": [
#         {
#             'Nombre': 'Cynthia',
#             'Edad': 22
#         },
#         {
#             'Nombre': 'Diego',
#             'Edad': 25
#         },
#         {
#             'Nombre': 'Daniela',
#             'Edad': 22
#         }
#     ]
# }
# user_str = json.dumps(user_dic, indent=2) --> de dict a str
# with open("estudiantes.txt", "w") as fil:
#     fil.write(user_str)

# JSON en lectura
# with open("estudiantes.txt", "r") as fil:
#     estudiantes_str = fil.read()
#
# estudiantes_dict = json.loads(estudiantes_str) # --> de str a dict
# print(estudiantes_dict['estudiantes'][0]['Nombre'])