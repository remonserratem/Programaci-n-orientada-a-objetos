
# EJEMPLO DE ENCAPSULACIÓN


class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        # ENCAPSULACIÓN: atributos dentro de la clase
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    # Métodos para manejar los atributos
    def recibir_daño(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    def mostrar_vida(self):
        print(f"{self.nombre} tiene {self.vida} de vida.")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa


# Ejemplo de encapsulación
p1 = Personaje("Artorias", 30, 5, 10, 100)
p2 = Personaje("Juanito", 25, 8, 12, 100)

daño = p1.daño(p2)
p2.recibir_daño(daño)

p2.mostrar_vida()
