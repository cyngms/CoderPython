# POO - organizar el codigo pensando en el problema como una relacion entre "cosas", es decir,
# objetos.
# objeto = carro
# Caracteristicas
# numero_ruedas
# numero_puertas
# tipo_de_combustible
# anio_creacion
# modelo

# Funcionalidades
# frenar
# avanzar
# encender_luces

# Crear una clase

class Dog:
    tipo = "mamifero"
    cantidad_ojos = 2

# Agregando atributos de instancia a la clase
    def __init__(self, raza: str, color: str) -> None:
        self.raza = raza
        self.color = color
        self.cantidad_patas = 4

    def __str__(self):
        return f"Yo soy un perro de raza{self.raza} y de color{self.color}"

    def __iter__(self):
        for ra in self.raza:
            yield ra

    def __len__(self):
        return len(self.raza)
    def ladrar(self) -> str:
        if self.raza == "doberman":
            return "ggggggggg"
        return "woff"

    def caminar(self, cantidad_pasos) -> str:
        if cantidad_pasos > 100:
            return "ha caminado mucho"
        return "ha caminado poco"

dog_1 = Dog(raza="doberman", color="negro") # Definir un objeto dentro de la clase
print(dog_1.cantidad_ojos)
print(dog_1)
print(dog_1.raza)
print(dog_1.color)
print(dog_1.ladrar())
print(dog_1.caminar(500))
print(len(dog_1))
# print("---------------------------")

# dog_2 = Dog(raza="pastor aleman", color="cafe") # Definir un objeto dentro de la clase
# print(dog_2.raza)
# print(dog_2.color)
# print(dog_2.ladrar())

