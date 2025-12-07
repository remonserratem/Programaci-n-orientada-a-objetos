
# EJEMPLO DE ABSTRACCIÓN EN POO


class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    # ABSTRACCIÓN: el usuario usa este método sin saber cómo funciona internamente
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(f"{self.nombre} atacó a {enemigo.nombre} causando {daño} de daño.")

    def esta_vivo(self):
        return self.vida > 0

    # Método que será diferente en cada clase hija
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa


# Ejemplo usando abstracción
g1 = Guerrero("Guts", 20, 10, 4, 100, 4)
g2 = Guerrero("Griffith", 15, 20, 5, 100, 3)

g1.atacar(g2)
print("¿Griffith sigue vivo?:", g2.esta_vivo())
