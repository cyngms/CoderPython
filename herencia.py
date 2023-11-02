# La herencia es un proceso mediatne el cual se puede crear una clase hija que
# hereda de una clase padre, compartiendo sus metodos y atributos.
#  Clase hija -- sobreescrbir  los metos o atributos, y definir unos nuevos

# Clase padre
# class Animal:
#     pass

# Clase hija que hereda de la Clase padre
# class Perro(Animal):
#     pass

# Una clase hija hereda los atributos y metodos de la padre, es util cuando se tienen clases
# que se parecen entre si, pero tienen ciertas peculiaridades

# Don't repeat yourself -- DRY -> Las clases y las herencias ayudan a no repetir
# codigo de manera innecesaria

class Animal:  # Clase padre
    adn = True

    def __init__(self, cantidad_ojos: int, tipo_piel: str) -> None:
        self.cantidad_ojos = cantidad_ojos
        self.tipo_piel = tipo_piel

    def breath(self) -> int:
        """
        Cantidad de veces que respira por minuto
        :return: int
        """
        return 30

    def run(self) -> str:
        """Me dice de que forma corre
        :return: str"""


class Mamifero:  # Sobreescritura del codigo, debido a la funcion dentro de la clase padre
    def breath(self):
        return "Estamos respirando por la nariz"


# Constructor
class Gato(Animal, Mamifero):  # Clase hija que hereda los atributos y modificaciones de la clase padre
    def __init__(self, cantidad_ojos: int, tipo_piel: str, color: str, raza: str):
        super().__init__(cantidad_ojos, tipo_piel=tipo_piel)  # super hace referencia a la clase padre
        self.color = color
        self.raza = raza

    def run(self) -> str:
        return "Corre normal"

    def breath(self) -> str:
        return Mamifero.breath(self)


# gato = Gato(cantidad_ojos=2, tipo_piel="aspera", color="rojo", raza="egipcio")
# print(gato.breath())
# print(gato.color)
# print(gato.raza)
# print(gato.cantidad_ojos)
# print(gato.tipo_piel)
# print(gato.run())


# Sobreescritura el metodo a correr, dentro de esta sobreescritura se elimina
# de la clase padre la funcion, para tomar la nueva
class Ballena(Animal):
    def run(self) -> str:
        return "Este animal no corre"

    def swim(self) -> str:
        return "Este animal nada lento"


#
#
# print("-----------")
# ballena = Ballena(cantidad_ojos=2, tipo_piel="escamosa")
# print(ballena.run())
# print(ballena.swim())


# Herencia multiple - una clase puede heredad de varias clases padre en lugar de una sola,
# Method Order Resolution - Nos devuelve una tupla con el orden de busqueda de los metodos
# Empieza en la propia clase y se va subiendo hasta la clase padre de izquierda a derecha.

# print(Animal.__mro__)
# print(Gato.__mro__)

# Multiherencia
# class Clase1:
#     pass
# class Clase2:
#     pass
# class Clase3(Clase1, Clase2):
#     pass

# Multiherencia, donde se elige de que clase se quiere heredar
# class Clase1:
#     pass
# class Clase2(Clase1):
#     pass
# class Clase3(Clase2):
#     pass

# Duck typing - tipado de los datos dentro de Python

def run(x: Gato | Ballena):
    return x.run()


print(run(Gato(cantidad_ojos=2, tipo_piel="aspera", color="rojo", raza="egipcio")))
print(run(Ballena(cantidad_ojos=2, tipo_piel="escamosa")))
