def registrar_entrenamiento():
    # Solicita al usuario los detalles del entrenamiento
    ejercicio = input("Nombre del ejercicio: ")
    peso = float(input("Peso utilizado (kg): "))
    series = int(input("Número de series: "))
    repeticiones = int(input("Repeticiones por serie: "))

    # Devuelve los datos para utilizarlos en otras funciones
    return ejercicio, peso, series, repeticiones


def calcular_volumen(peso, series, repeticiones):
    # Calcula el volumen total del entrenamiento
    volumen = peso * series * repeticiones

    # Devuelve el volumen calculado
    return volumen


def mostrar_resultados(ejercicio, peso, series, repeticiones):
    # Calcula el volumen total y el promedio por serie
    volumen = calcular_volumen(peso, series, repeticiones)
    promedio_por_serie = volumen / series

    # Muestra los resultados del entrenamiento
    print("\n===== Resultados del Entrenamiento =====")
    print(f"Ejercicio: {ejercicio}")
    print(f"Peso utilizado: {peso} kg")
    print(f"Número de series: {series}")
    print(f"Repeticiones por serie: {repeticiones}")
    print(f"Volumen total del entrenamiento: {volumen} kg")
    print(f"Volumen promedio por serie: {promedio_por_serie:.2f} kg")


def main():
    # Muestra el nombre del programa
    print("==============================")
    print("          GainTrack          ")
    print("==============================")

    # Muestra las opciones disponibles en el menú
    print("\n¿Qué deseas hacer?")
    print("1. Registrar entrenamiento")
    print("2. Calcular volumen de entrenamiento")
    print("3. Salir")

    # Guarda la opción seleccionada por el usuario
    opcion = int(input("Selecciona una opción: "))

    # Si el usuario selecciona 1, registra un entrenamiento
    if opcion == 1:
        ejercicio, peso, series, repeticiones = registrar_entrenamiento()
        mostrar_resultados(ejercicio, peso, series, repeticiones)

        # Indica que el programa debe continuar
        return True

    # Si el usuario selecciona 2, calcula el volumen directamente
    elif opcion == 2:
        # Solicita los datos necesarios para calcular el volumen
        peso = float(input("Peso utilizado (kg): "))
        series = int(input("Número de series realizadas: "))
        repeticiones = int(input("Repeticiones por serie: "))

        # Calcula el volumen y guarda el resultado
        volumen = calcular_volumen(peso, series, repeticiones)

        # Muestra el volumen calculado
        print(f"\nEl volumen de tu entrenamiento es: {volumen} kg")

        # Indica que el programa debe continuar
        return True

    # Si el usuario selecciona 3, termina el programa
    elif opcion == 3:
        print("\nGracias por usar GainTrack")

        # Indica que el programa debe detenerse
        return False

    # Si el usuario selecciona una opción diferente a 1, 2 o 3
    else:
        print("\nOpción no válida")

        # Permite volver al menú principal
        return True


# Repite el menú para que el usuario pueda realizar varias acciones
# hasta que seleccione la opción de salir
while True:
    continuar = main()

    # Si main() devuelve False, termina el ciclo
    if not continuar:
        break
    
