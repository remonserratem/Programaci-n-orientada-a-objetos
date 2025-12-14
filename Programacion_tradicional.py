
# Programación Tradicional
# Ejemplo: Registro de temperaturas semanales


# Variable global para almacenar las temperaturas
temperaturas = []

# Función para ingresar la temperatura diaria
def ingresar_temperatura(temp):
    """
    Agrega una temperatura diaria a la lista.
    """
    temperaturas.append(temp)

# Función para calcular el promedio semanal
def calcular_promedio_semanal():
    """
    Calcula y retorna el promedio de las temperaturas registradas.
    """
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)

# Uso de las funciones (programación tradicional)
ingresar_temperatura(28)
ingresar_temperatura(30)
ingresar_temperatura(29)
ingresar_temperatura(31)
ingresar_temperatura(27)
ingresar_temperatura(26)
ingresar_temperatura(28)

# Calcular y mostrar el promedio
promedio = calcular_promedio_semanal()
print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")
