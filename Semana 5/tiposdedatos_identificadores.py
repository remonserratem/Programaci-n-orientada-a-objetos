"""
Programa: Conversor de Temperatura (POO)
Descripción: Programa orientado a objetos que convierte temperaturas
entre Celsius y Fahrenheit.
Autor: ROXANA ESTEFANIA MONSERRATE MIÑO
"""

class ConversorTemperatura:
    """
    Clase que representa un conversor de temperaturas.
    """

    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte grados Celsius a Fahrenheit.
        """
        return (celsius * 9 / 5) + 32

    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Convierte grados Fahrenheit a Celsius.
        """
        return (fahrenheit - 32) * 5 / 9


class Aplicacion:
    """
    Clase principal que controla la ejecución del programa.
    """

    def __init__(self):
        self.conversor = ConversorTemperatura()
        self.continuar_programa = True  # Boolean

    def mostrar_menu(self):
        print("\nConversor de Temperatura")
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")

    def ejecutar(self):
        while self.continuar_programa:
            self.mostrar_menu()

            opcion = input("Elige una opción (1 o 2): ")  # String

            if opcion == "1":
                temperatura_celsius = float(input("Ingresa la temperatura en Celsius: "))  # Float
                resultado = self.conversor.celsius_a_fahrenheit(temperatura_celsius)
                print(f"{temperatura_celsius} °C equivale a {resultado:.2f} °F")

            elif opcion == "2":
                temperatura_fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
                resultado = self.conversor.fahrenheit_a_celsius(temperatura_fahrenheit)
                print(f"{temperatura_fahrenheit} °F equivale a {resultado:.2f} °C")

            else:
                print("Opción no válida.")

            respuesta = input("¿Deseas realizar otra conversión? (si/no): ").lower()
            if respuesta != "si":
                self.continuar_programa = False


# Punto de entrada del programa
if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()
