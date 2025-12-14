
# Programación Orientada a Objetos (POO)
# Ejemplo: Registro de temperaturas semanales


class ClimaSemanal:
    """
    Clase que representa la información climática semanal.
    """

    def __init__(self):
        # Atributo privado (encapsulamiento)
        self.__temperaturas = []

    def ingresar_temperatura(self, temp):
        """
        Metodo para ingresar una temperatura diaria.
        """
        self.__temperaturas.append(temp)

    def calcular_promedio_semanal(self):
        """
        Método para calcular el promedio semanal de temperaturas.
        """
        if len(self.__temperaturas) == 0:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)

# Uso de la clase
clima = ClimaSemanal()

clima.ingresar_temperatura(28)
clima.ingresar_temperatura(30)
clima.ingresar_temperatura(29)
clima.ingresar_temperatura(31)
clima.ingresar_temperatura(27)
clima.ingresar_temperatura(26)
clima.ingresar_temperatura(28)

# Calcular y mostrar el promedio
promedio = clima.calcular_promedio_semanal()
print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")
