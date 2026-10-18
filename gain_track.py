# Guarda los entrenamientos registrados durante la ejecucion
entrenamientos = []


def registrar_entrenamiento():
    # Solicita al usuario los detalles del entrenamiento
    ejercicio = input("Nombre del ejercicio: ")
    peso = float(input("Peso utilizado (kg): "))
    series = int(input("Numero de series: "))
    repeticiones = int(input("Repeticiones por serie: "))

    # Guarda los datos del entrenamiento en una lista
    entrenamiento = [ejercicio, peso, series, repeticiones]

    # Agrega el entrenamiento al historial
    entrenamientos.append(entrenamiento)

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
    print(f"Numero de series: {series}")
    print(f"Repeticiones por serie: {repeticiones}")
    print(f"Volumen total del entrenamiento: {volumen} kg")
    print(f"Volumen promedio por serie: {promedio_por_serie:.2f} kg")


def consultar_entrenamientos():
    # Comprueba si existen entrenamientos registrados
    if len(entrenamientos) == 0:
        print("\nTodavia no hay entrenamientos registrados.")

    else:
        # Recorre la lista para mostrar cada entrenamiento
        print("\n===== Historial de Entrenamientos =====")

        for i in range(len(entrenamientos)):
            # Obtiene los datos del entrenamiento actual
            entrenamiento = entrenamientos[i]

            ejercicio = entrenamiento[0]
            peso = entrenamiento[1]
            series = entrenamiento[2]
            repeticiones = entrenamiento[3]

            # Calcula el volumen del entrenamiento actual
            volumen = calcular_volumen(peso, series, repeticiones)

            # Muestra los datos del entrenamiento
            print(f"\nEntrenamiento {i + 1}")
            print(f"Ejercicio: {ejercicio}")
            print(f"Peso utilizado: {peso} kg")
            print(f"Numero de series: {series}")
            print(f"Repeticiones por serie: {repeticiones}")
            print(f"Volumen total: {volumen} kg")


def main():
    # Muestra el nombre del programa
    print("\n==============================")
    print("          GainTrack")
    print("==============================")

    # Muestra las opciones disponibles en el menu
    print("\nQue deseas hacer?")
    print("1. Registrar entrenamiento")
    print("2. Calcular volumen de entrenamiento")
    print("3. Consultar entrenamientos")
    print("4. Salir")

    # Guarda la opcion seleccionada por el usuario
    opcion = int(input("Selecciona una opcion: "))

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
        series = int(input("Numero de series realizadas: "))
        repeticiones = int(input("Repeticiones por serie: "))

        # Calcula y muestra el volumen
        volumen = calcular_volumen(peso, series, repeticiones)
        print(f"\nEl volumen de tu entrenamiento es: {volumen} kg")

        # Indica que el programa debe continuar
        return True

    # Si el usuario selecciona 3, muestra el historial
    elif opcion == 3:
        consultar_entrenamientos()

        # Indica que el programa debe continuar
        return True

    # Si el usuario selecciona 4, termina el programa
    elif opcion == 4:
        print("\n¡Gracias por usar GainTrack!")

        # Indica que el programa debe detenerse
        return False

    # Si el usuario selecciona una opcion diferente a las disponibles
    else:
        print("\nOpcion no valida")

        # Permite regresar al menu principal
        return True


# Repite el menu hasta que el usuario decida salir
while True:
    continuar = main()

    # Termina el ciclo cuando main() devuelve False
    if not continuar:
        break

    # Si main() devuelve False, termina el ciclo
    if not continuar:
        break
    
