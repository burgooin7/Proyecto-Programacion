def registrar_entrenamiento():
    # Solicita al usuario que ingrese los detalles del entrenamiento
    ejercicio = input("nombre del ejercicio: ")
    peso = float(input("peso utilizado (kg): "))
    series = int(input("numero de series: "))
    repeticiones = int(input("repeticiones por serie: "))

    # Devuelve los datos para que puedan ser utilizados en otras funciones
    return ejercicio, peso, series, repeticiones

def calcular_volumen(peso, series, repeticiones):
    # Calcula el volumen total del entrenamiento
    volumen = peso * series * repeticiones

    # Devuelve el volumen calculado
    return volumen

def mostrar_resultados(ejercicio, peso, series, repeticiones):
    # Calcula el volumen del entrenamiento
    volumen = calcular_volumen(peso, series, repeticiones)
    # Calcula el volumen promedio realizado en cada serie
    promedio_por_serie = volumen / series

    # Muestra los resultados del entrenamiento
    print("\n===== Resultados del Entrenamiento =====")
    print(f"Ejercicio: {ejercicio}")
    print(f"Peso utilizado: {peso} kg")
    print(f"Numero de series: {series}")
    print(f"Repeticiones por serie: {repeticiones}")
    print(f"Volumen total del entrenamiento: {volumen} kg")
    print(f"Volumen promedio por serie: {promedio_por_serie:.2f} kg")

def main():
    # Ejecuta el programa principal
    print("==============================")
    print("          GainTrack          ")
    print("==============================")
    # Muestra las opciones disponibles para el usuario
    print("\n¿Que deseas hacer?")
    print("1. Registrar Entrenamiento")
    print("2. Calcular Volumen de Entrenamiento")
    print("3. Salir")

    # Guarda la opción que seleccionó el usuario
    opcion = int(input("Salecciona una opcion: "))

    # Si el usuario selecciona 1, registra un nuevo entrenamiento
    if opcion == 1:
        ejercicio, peso, series, repeticiones = registrar_entrenamiento()
        mostrar_resultados(ejercicio, peso, series, repeticiones)

        return True

    # Si el usuario selecciona 2, calcula el volumen directamente
    elif opcion == 2:
        peso = float(input("Peso utilizado (kg): "))
        series = int(input("Numero de series realizadas: "))
        repeticiones = int(input("Repeticiones por serie: "))
        calcular_volumen(peso, series, repeticiones)
        volumen = calcular_volumen(peso, series, repeticiones)
        print(f"\nEl volumen de tu entreno es:{volumen} kg ")

        return True

    # Si el usuario selecciona 3, termina el programa
    elif opcion == 3:
        print("\nGracias por usar GainTrack")

        return False
        
    # Si el usuario escribe una opción diferente a 1, 2 o 3
    else: 
        print("\nopcion no valida")

        return True
    
# Repite el menu para que el usuario pueda realizar varias acciones
# hasta que seleccione la opcion de salir
while True : 

    # Si el usuario selecciona salir, termina el ciclo
    continuar = main()
    if not continuar:
        break
