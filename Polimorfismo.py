
# EJEMPLO DE POLIMORFISMO


class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def daño(self, enemigo):
        # Método base
        return self.fuerza - enemigo.defensa


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    # POLIMORFISMO: sobrescritura del método daño()
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    # POLIMORFISMO: sobrescritura del método daño()
    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa


# Ejemplo práctico
g = Guerrero("Guts", 20, 10, 4, 100, 4)
m = Mago("Vanessa", 5, 15, 4, 100, 3)

print("Daño de Guts:", g.daño(m))
print("Daño de Vanessa:", m.daño(g))
