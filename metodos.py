
from funcion import Funcion

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("svg")

class Metodos:
    @staticmethod
    def graficar_funcion_punto_izquierdo(funcion: Funcion, lim_inf: float, lim_sup: float, particiones: int, paso: float):
        x_func = np.linspace(lim_inf, lim_sup, 1000)
        y_func = funcion.evaluar_funcion(x_func)

        x_rect = np.linspace(lim_inf, lim_sup, particiones + 1)
        y_rect = funcion.evaluar_funcion(x_rect)

        x_rect = x_rect[:-1]; y_rect = y_rect[:-1]

        grafica = plt.figure()
        plt.plot(x_func, y_func)
        plt.plot(x_rect, y_rect, 'r.', markersize = 10) 
        plt.bar(x_rect, y_rect, width = paso, align = 'edge', alpha = 0.2, edgecolor = 'b')
        plt.title(f"Punto izquierdo y {particiones} particiones")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)

        return grafica


    @staticmethod
    def graficar_funcion_punto_derecho(funcion: Funcion, lim_inf: float, lim_sup: float, particiones: int, paso: float):
        x_func = np.linspace(lim_inf, lim_sup, 1000)
        y_func = funcion.evaluar_funcion(x_func)

        x_rect = np.linspace(lim_inf, lim_sup, particiones + 1)
        y_rect = funcion.evaluar_funcion(x_rect)

        x_rect = x_rect[1:]; y_rect = y_rect[1:]

        grafica = plt.figure()
        plt.plot(x_func, y_func)
        plt.plot(x_rect, y_rect, 'r.', markersize = 10)
        plt.bar(x_rect, y_rect, width = -paso, align = 'edge', alpha = 0.2, edgecolor = 'b')
        plt.title(f"Punto derecho y {particiones} particiones")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)

        return grafica


    @staticmethod
    def graficar_funcion_punto_medio(funcion: Funcion, lim_inf: float, lim_sup: float, particiones: int, paso: float):
        x_func = np.linspace(lim_inf, lim_sup, 1000)
        y_func = funcion.evaluar_funcion(x_func)

        x_rect = np.linspace(lim_inf, lim_sup, particiones + 1)
        y_rect = funcion.evaluar_funcion(x_rect)

        x_rect = (x_rect[:-1] + x_rect[1:]) / 2
        y_rect = funcion.evaluar_funcion(x_rect)

        grafica = plt.figure()
        plt.plot(x_func, y_func)
        plt.plot(x_rect, y_rect, 'r.', markersize = 10)
        plt.bar(x_rect, y_rect, width = paso, alpha = 0.2, edgecolor = 'b')
        plt.title(f"Punto medio y {particiones} particiones")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        
        return grafica


    @staticmethod
    def graficar_trapecio(funcion: Funcion, lim_inf: float, lim_sup: float, particiones: int):
        x_func = np.linspace(lim_inf, lim_sup, 1000)
        y_func = funcion.evaluar_funcion(x_func)

        x_trap = np.linspace(lim_inf, lim_sup, particiones + 1)
        y_trap = funcion.evaluar_funcion(x_trap)

        grafica = plt.figure()
        for x in range(particiones):
            abcisas_trap = [x_trap[x], x_trap[x], x_trap[x + 1], x_trap[x + 1]]
            ordenadas_trap = [0, funcion.evaluar_funcion(x_trap[x]), funcion.evaluar_funcion(x_trap[x + 1]), 0]
            plt.fill(abcisas_trap, ordenadas_trap, 'C0', edgecolor = 'b', alpha = 0.2)

        plt.plot(x_func, y_func)
        plt.plot(x_trap, y_trap, 'r.', markersize = 10)
        plt.title(f"Trapecios y {particiones} particiones")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)

        return grafica


    @staticmethod
    def punto_izquierdo(funcion: Funcion, lim_inf: float, lim_sup: float, particiones: int):
        paso = (lim_sup - lim_inf) / particiones
        subintervalos = np.arange(lim_inf, lim_sup, paso)
        area = 0
        for x in subintervalos:
            area += np.abs(funcion.evaluar_funcion(x) * paso)

        grafica = Metodos.graficar_funcion_punto_izquierdo(funcion, lim_inf, lim_sup, particiones, paso)

        return area, grafica


    @staticmethod
    def punto_derecho(funcion: Funcion, lim_inf: float, lim_sup: float, particiones: int) -> float:
        paso = (lim_sup - lim_inf) / particiones
        subintervalos = np.arange(lim_inf, lim_sup, paso) + paso
        area = 0
        for x in subintervalos:
            area += np.abs(funcion.evaluar_funcion(x) * paso)

        grafica = Metodos.graficar_funcion_punto_derecho(funcion, lim_inf, lim_sup, particiones, paso)

        return area, grafica


    @staticmethod
    def punto_medio(funcion: Funcion, lim_inf: float, lim_sup: float, particiones: int) -> float:
        paso = (lim_sup - lim_inf) / (particiones)
        subintervalos = np.arange(lim_inf, lim_sup, paso) + (paso/2)
        area = 0
        for x in subintervalos:
            area += np.abs(funcion.evaluar_funcion(x) * paso)

        grafica = Metodos.graficar_funcion_punto_medio(funcion, lim_inf, lim_sup, particiones, paso)

        return area, grafica


    @staticmethod
    def trapecio(funcion: Funcion, lim_inf: float, lim_sup: float, particiones: int) -> float:
        paso = (lim_sup - lim_inf) / particiones
        subintervalos = np.arange(lim_inf, lim_sup, paso)
        area = 0
        for x in subintervalos:
            area += np.abs((funcion.evaluar_funcion(x) + funcion.evaluar_funcion(x + paso)) * (paso/2))

        grafica = Metodos.graficar_trapecio(funcion, lim_inf, lim_sup, particiones)

        return area, grafica


    @staticmethod
    def grafica_ejemplo():
        funcion: Funcion = Funcion()
        funcion.set_funcion = "x**2 + 1"
        lim_inf: float = -2
        lim_sup: float = 5
        particiones: int = 6

        Metodos.punto_izquierdo(funcion, lim_inf, lim_sup, particiones)


# Caso de prueba
""" funcion: Funcion = Funcion()
funcion.set_funcion = "x**3"
lim_inf = 0; lim_sup = 1
particiones = 4
print(Metodos.punto_izquierdo(funcion, lim_inf, lim_sup, particiones))
print(Metodos.punto_derecho(funcion, lim_inf, lim_sup, particiones, True))
print(Metodos.punto_medio(funcion, lim_inf, lim_sup, particiones, True))
print(Metodos.trapecio(funcion, lim_inf, lim_sup, particiones, True)) """
