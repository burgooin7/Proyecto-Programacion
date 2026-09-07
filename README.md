# Proyecto-Programaci-n-1
Semestre Agosto - Diciembre 2026 
, por: Alejandro Burgoin A01714726

# GainTrack

## Descripción

**GainTrack** es un programa desarrollado en Python que permite a los usuarios registrar, consultar y analizar sus entrenamientos para llevar un seguimiento de su rendimiento físico y observar su progreso a través del tiempo.

El proyecto está pensado como una herramienta sencilla que transforma los datos de los entrenamientos en información útil para que el usuario pueda conocer mejor su desempeño y darle seguimiento a sus objetivos.

----------

## Contexto

Actualmente, muchas personas realizan ejercicio de manera constante, pero no siempre llevan un registro organizado de sus entrenamientos. Datos como el peso utilizado, las series, las repeticiones o la frecuencia de entrenamiento pueden perderse o simplemente no utilizarse para conocer el progreso.

A partir de esta situación surge **GainTrack**, una propuesta que busca facilitar el registro de los entrenamientos y utilizar la información recopilada para obtener datos que ayuden al usuario a conocer su rendimiento.

El proyecto comenzará como un programa sencillo que funciona desde la terminal y que irá creciendo conforme se incorporen nuevos conocimientos de programación durante el semestre.

----------

## Objetivo

Desarrollar una herramienta sencilla en Python que permita a los usuarios registrar sus entrenamientos y utilizar sus propios datos para consultar su rendimiento, identificar su progreso y, posteriormente, establecer metas de entrenamiento.

----------

## Alcance inicial

La primera versión de **GainTrack** contará con las siguientes funciones:

-   Registrar un entrenamiento.
    
-   Ingresar el nombre del ejercicio.
    
-   Registrar el peso utilizado.
    
-   Registrar el número de series.
    
-   Registrar el número de repeticiones.
    
-   Consultar los entrenamientos registrados.
    
-   Calcular el volumen de entrenamiento.
    
-   Mostrar un menú para navegar por las diferentes opciones.
    
-   Validar datos y opciones ingresadas por el usuario.
    

El cálculo inicial del volumen de entrenamiento será:

**Volumen = peso × series × repeticiones**

----------

## Funcionamiento general

El funcionamiento principal del programa seguirá el siguiente proceso:

```text
Inicio
  ↓
Mostrar menú principal
  ↓
Seleccionar una opción
  ↓
┌─────────────────────────────┐
│ Registrar entrenamiento     │
│ Consultar entrenamiento     │
│ Calcular volumen            │
│ Salir                       │
└─────────────────────────────┘
  ↓
Procesar la opción seleccionada
  ↓
Mostrar resultado
  ↓
Regresar al menú
  ↓
¿Salir?
  ├── No → Continuar
  └── Sí → Fin

```

----------

## Algoritmo

ENTRADAS:
- Nombre del ejercicio.
- Peso utilizado en kilogramos.
- Número de series.
- Número de repeticiones.
- Opción seleccionada en el menú.

1. INICIO

2. Mostrar el nombre del programa GainTrack.

3. Mostrar un menú con las opciones:
   2.1. Registrar entrenamiento.
   2.2. Consultar entrenamiento.
   2.3. Calcular volumen de entrenamiento.
   2.4. Salir.

4. Pedir al usuario que seleccione una opción.

5. Si selecciona Registrar entrenamiento:
   4.1. Pedir el nombre del ejercicio.
   4.2. Pedir el peso utilizado.
   4.3. Pedir el número de series.
   4.4. Pedir el número de repeticiones.
   4.5. Guardar los datos del entrenamiento.

6. Si selecciona Consultar entrenamiento:
   5.1. Mostrar los entrenamientos registrados.

7. Si selecciona Calcular volumen:
   6.1. Obtener el peso, número de series y número de repeticiones.
   6.2. Calcular el volumen de entrenamiento.
   6.3. Mostrar el resultado.

8. Si selecciona Salir:
   7.1. Terminar el programa.

9. Si selecciona una opción incorrecta:
   8.1. Mostrar un mensaje indicando que la opción no es válida.
   8.2. Regresar al menú principal.

10. Volver al paso 2.
11. FIN

SALIDAS:
- Datos del entrenamiento registrado.
- Entrenamientos registrados.
- Volumen de entrenamiento calculado.
- Mensaje de opción no válida.
- Mensaje de salida del programa.

----------

## Escalabilidad

Una de las características principales de **GainTrack** será que el proyecto podrá crecer conforme se adquieran nuevos conocimientos de programación.

Algunas funcionalidades que podrían incorporarse posteriormente son:

-   Historial completo de entrenamientos.
    
-   Búsqueda de ejercicios.
    
-   Estadísticas de rendimiento.
    
-   Comparación del progreso entre diferentes fechas.
    
-   Registro de diferentes tipos de entrenamiento.
    
-   Establecimiento de metas.
    
-   Recomendaciones basadas en los datos registrados.
    
-   Almacenamiento permanente de la información.
    
-   Análisis más avanzado del rendimiento.
    

Estas funcionalidades permitirán que el proyecto evolucione de un programa básico de registro a una herramienta más completa para el seguimiento del rendimiento físico.

----------

## Estructura del proyecto

```text
GainTrack/
│
├── README.md
│
└── gaintrack.py
```

### `README.md`
Contiene la documentación y descripción general del proyecto.

### `gaintrack.py`
 será donde posteriormente hagamos el programa.

## Tecnologías

-   **Python 3.13**
-   **GitHub**
    

----------

##  Proyección del proyecto

La intención de **GainTrack** es comenzar con funcionalidades básicas y aumentar progresivamente su capacidad conforme se aprendan nuevos conceptos de programación.

El proyecto seguirá una idea principal:

> **Registrar → Organizar → Analizar → Comprender el progreso**

De esta manera, cada nueva funcionalidad podrá aportar mayor utilidad al usuario sin perder la idea original del proyecto.
