class AbstractAuto:
    def andar(self):
        raise NotImplementedError

    def frenar(self):
        raise NotImplementedError


class Bus(AbstractAuto):
    def andar(self):
        return "estoy andando"

    def frenar(self):
        return "estoy frenando"

# Crear una base de codigo que obligatoriamente se tiene que hacer, en caso de que no se implemente,
# se va a generar error
