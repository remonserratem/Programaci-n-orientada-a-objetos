# Clase Habitacion
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def ocupar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True


# Clase Cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula


# Clase Reserva
class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def confirmar_reserva(self):
        if self.habitacion.disponible:
            self.habitacion.ocupar()
            total = self.habitacion.precio * self.dias
            print("Reserva confirmada")
            print("Cliente:", self.cliente.nombre)
            print("Habitación:", self.habitacion.numero)
            print("Total a pagar:", total)
        else:
            print("La habitación no está disponible")


# ----- Uso del sistema -----

# Crear objetos
habitacion1 = Habitacion(101, "Simple", 30)
cliente1 = Cliente("Ana Pérez", "0102030405")

# Crear reserva
reserva1 = Reserva(cliente1, habitacion1, 3)
reserva1.confirmar_reserva()
