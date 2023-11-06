# Se crea la clase "Clientes"
class Clientes:
    def __init__(self, nombre: str, apellido: str, correo: str, telefono: str):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def obtener_info(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nCorreo: {self.correo}\nTeléfono: {self.telefono}"

    def realizar_compra(self):
        pass


# Utilizar la clase cliente
cliente1 = Clientes("Juan", "Perez", "juan@gmail.com", "575-4879-936")
cliente2 = Clientes("Maria", "Lopez", "marilop@gmail.com", "524-8967-325")

print("Cliente 1: ", cliente1)
print("Cliente 2: ", cliente2)

print("\nInformacion del Cliente 1: ")
print(cliente1.obtener_info())

print("\nInformacion del Cliente 2: ")
print(cliente2.obtener_info())


def ClientesVIP(Clientes) -> None:
    def __init(self, nombre: str, apellido: str, correo: str, telefono: int, descuento: float):
        Clientes.__init__(nombre, apellido, correo, telefono)
        self.descuento = descuento

    def __str__(self):
        return f"Cliente VIP: {self.nombre} {self.apellido}"
