
# EJEMPLO DE HERENCIA EN PROGRAMACIÓN ORIENTADA A OBJETOS


class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)


# HERENCIA:
# Las clases Guerrero y Mago heredan los atributos y métodos de Personaje.

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro


# Ejemplo de uso
g = Guerrero("Guts", 20, 10, 4, 100, 4)
m = Mago("Vanessa", 5, 15, 4, 100, 3)

g.atributos()
m.atributos()
