# Guarda los entrenamientos registrados durante la ejecucion
entrenamientos = []

# Archivo donde se guardan los entrenamientos
nombre_archivo = "entrenamientos.txt"


def registrar_entrenamiento():
    # Solicita al usuario los detalles del entrenamiento
    ejercicio = input("Nombre del ejercicio: ")
    peso = float(input("Peso utilizado (kg): "))
    series = int(input("Numero de series: "))
    repeticiones = int(input("Repeticiones por serie: "))

    # Guarda los datos del entrenamiento en una lista
    entrenamiento = [ejercicio, peso, series, repeticiones]

    # Agrega la lista del entrenamiento a la lista principal
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
        # Permite elegir como mostrar los nombres de los ejercicios
        print("\nComo deseas mostrar los nombres?")
        print("1. Texto original")
        print("2. Mayusculas")
        print("3. Minusculas")

        formato = int(input("Selecciona una opcion: "))

        # Comprueba que la opcion sea valida
        if formato == 1 or formato == 2 or formato == 3:
            # Muestra el historial de entrenamientos
            print("\n===== Historial de Entrenamientos =====")

            # Recorre las filas de la lista principal
            for i in range(len(entrenamientos)):
                # Obtiene la lista correspondiente a cada entrenamiento
                entrenamiento = entrenamientos[i]

                # Accede a los datos mediante sus posiciones
                ejercicio = entrenamiento[0]
                peso = entrenamiento[1]
                series = entrenamiento[2]
                repeticiones = entrenamiento[3]

                # Cambia el formato del nombre del ejercicio
                if formato == 2:
                    ejercicio = ejercicio.upper()
                elif formato == 3:
                    ejercicio = ejercicio.lower()

                # Calcula el volumen del entrenamiento actual
                volumen = calcular_volumen(peso, series, repeticiones)

                # Muestra los datos de cada entrenamiento
                print(f"\nEntrenamiento {i + 1}")
                print(f"Ejercicio: {ejercicio}")
                print(f"Peso utilizado: {peso} kg")
                print(f"Numero de series: {series}")
                print(f"Repeticiones por serie: {repeticiones}")
                print(f"Volumen total: {volumen} kg")
        else:
            print("\nOpcion no valida.")


def guardar_entrenamientos():
    # Guarda todos los entrenamientos en el archivo de texto,
    # uno por linea: ejercicio,peso,series,repeticiones
    archivo = open(nombre_archivo, "w")

    for i in range(len(entrenamientos)):
        entrenamiento = entrenamientos[i]
        ejercicio = entrenamiento[0]
        peso = entrenamiento[1]
        series = entrenamiento[2]
        repeticiones = entrenamiento[3]
        archivo.write(f"{ejercicio},{peso},{series},{repeticiones}\n")

    archivo.close()
    print(f"\nSe guardaron {len(entrenamientos)} entrenamientos en {nombre_archivo}.")


def cargar_entrenamientos():
    # Lee los entrenamientos guardados y los agrega a la lista
    archivo = open(nombre_archivo, "r")
    cargados = 0

    for linea in archivo:
        linea = linea.strip()
        if linea == "":
            continue
        partes = linea.split(",")
        ejercicio = partes[0]
        peso = float(partes[1])
        series = int(partes[2])
        repeticiones = int(partes[3])
        entrenamiento = [ejercicio, peso, series, repeticiones]
        entrenamientos.append(entrenamiento)
        cargados = cargados + 1

    archivo.close()
    if cargados > 0:
        print(f"\nSe cargaron {cargados} entrenamientos desde el archivo.")


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
    print("4. Guardar entrenamientos en archivo")
    print("5. Salir")

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

    # Si el usuario selecciona 4, guarda los entrenamientos en el archivo
    elif opcion == 4:
        guardar_entrenamientos()

        # Indica que el programa debe continuar
        return True

    # Si el usuario selecciona 5, termina el programa
    elif opcion == 5:
        print("\nGracias por usar GainTrack!")

        # Indica que el programa debe detenerse
        return False

    # Si el usuario selecciona una opcion diferente a las disponibles
    else:
        print("\nOpcion no valida")

        # Permite regresar al menu principal
        return True


# Carga los entrenamientos guardados antes de mostrar el menu
cargar_entrenamientos()

# Repite el menu hasta que el usuario decida salir
while True:
    continuar = main()

    # Termina el ciclo cuando main() devuelve False
    if not continuar:
        break
