# lista = [1, 2, 3, 4, 5]
# print(len(lista))
# print(lista.__len__())

# print(lista[2])
# print(lista.__getitem__(2))

class Alumno:
    def __int__(self, nombre: str, nota: float) -> None:
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"La nota del estudiante {self.nombre} es {self.nota}")

    def resultado(self):
        if self.nota < 3.5:
            print(f"El resultado es: perdio")
        print(f"El resultado es: gano")


alu1 = Alumno("Luis",3.2)
alu1.imprimir()
alu1.resultado()
