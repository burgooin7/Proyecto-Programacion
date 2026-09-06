def registrar_entrenamiento():
    # Solicita al usuario que ingrese los detalles del entrenamiento
    ejercicio = input("nombre del ejercicio: ")
    peso = float(input("peso utilizado (kg): "))
    series = int(input("numero de series: "))
    respeticiones = int(input("repeticiones por serie: "))
    return ejercicio, peso, series, respeticiones

def calcular_volumen(peso, series, respeticiones):
    # Calcula el volumen total del entrenamiento
    volumen = peso * series * respeticiones
    return volumen

def mostrar_resultados(ejercicio, peso, series, respeticiones):
    # Muestra los resultados del entrenamiento
    volumen = calcular_volumen(peso, series, respeticiones)
    total_repeticiones = series * respeticiones
    promedio_por_serie = volumen / series

    print("\n===== Resultados del Entrenamiento =====")
    print(f"Ejercicio: {ejercicio}")
    print(f"Peso utilizado: {peso} kg")
    print(f"Numero de series: {series}")
    print(f"Repeticiones por serie: {respeticiones}")
    print(f"Volumen total del entrenamiento: {volumen} kg")
    print(f"Volumen promedio por serie: {promedio_por_serie:.2f} kg")

def main():
    # Ejecuta el programa principal
    print("==============================")
    print("          GainTrack          ")
    print("==============================")
    ejercicio, peso, series, respeticiones = registrar_entrenamiento()
    mostrar_resultados(ejercicio, peso, series, respeticiones)

main()