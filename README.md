
# Sumas de Riemman

## Descripción

Programa con interfaz sencilla para realizar sumas de Riemann. Permite ingresar una función como texto,
los límites de integración y el número de particiones. La interfaz trabaja con matplotlib, haciendo 
posible visualizar la función ingresada con los datos ingresados y el área aproximada bajo la curva.

## Previw de la aplicación

![Preview](/assets/preview1.png "Ventana principal")

## Requisitos

  - Usar Python 3.10 o superior
  - Matplotlib v3.6.0 o superior
  - Sympy v1.11.1 o superior
  - Numpy v1.22.1 o superior
  - Flet v0.4.0 o superior

## Para convertir en un archivo ejecutable (.exe)

  --- IMPORTANTE ---
  El archivo en formato .exe tiene un peso de aproximadamente 69.1 MB

  - Requiere pyinstaller v5.7.0 o superior
  - Abrir la terminal e ingresar el comando:
    "flet pack main.py"

## Changelog

--- v1.0 ---
  - Primera versión del programa
  - Interfaz gráfica de usuario (GUI) hecha en Python usando la librería Flet
  - Graficador de funciones usando Matplotlib
  - Cálculos usando Numpy

--- v1.1 ---

  - Se añadió un parser de LaTeX, el cual permite ver cómo es la función que se va a graficar
  - Las entradas de texto reconocen pi y e como constantes
  - Se cambiaron de ubicación algunos elementos para optimizar el espacio usado
  - Se mejoraron algunos elementos visuales del graficador para armonizar la paleta de colores
  - Se mejoró la experiencia visual en general

