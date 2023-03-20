
import numpy as np
from sympy import sympify, latex

class Funcion:
    def __init__(self) -> None:
        self._funcion = ""
        self._funcion_latex = ""


    @property
    def get_funcion(self) -> str:
        return self._funcion


    @get_funcion.setter
    def set_funcion(self, funcion: str) -> None:

        equivalencias: dict = {
            "sin": "np.sin",
            "sinh": "np.sinh",
            "cos": "np.cos",
            "cosh": "np.cosh",
            "tan": "np.tan",
            "tanh": "np.tanh",
            "exp": "np.exp",
            "euler": "np.exp",
            "e": "np.exp",
            "log": "np.log",
            "log10": "np.log10",
            "sqrt": "np.sqrt",
            "cbrt": "np.cbrt",
            "^": "**"
        }

        for org, sust in equivalencias.items():
            funcion = funcion.replace(org, sust)

        self._funcion = funcion


    @property
    def get_funcion_latex(self) -> str:
        return self._funcion_latex


    @get_funcion_latex.setter
    def set_funcion_latex(self, funcion: str) -> None:

        equivalencias: dict = {
            "e": "E",
            "exp": "E",
            "euler": "E",
            "pi": "1*pi",
            "3.14": "1*pi",
            "3.1416": "1*pi",
        }

        for org, sust in equivalencias.items():
            funcion = funcion.replace(org, sust)

        self._funcion_latex = funcion


    def evaluar_funcion(self, x: float):
        return eval(self._funcion)


    def formatear(self) -> None:
        self._funcion_latex = latex(sympify(self._funcion_latex))


# Casos de prueba
""" funcion: Funcion = Funcion()
funcion.set_funcion = "x**2 + 3"
funcion.set_funcion_latex = "x**2 + 3"
funcion.formatear()
print(funcion.get_funcion)
print(funcion.get_funcion_latex)

funcion.set_funcion = "5*e**(x + y)"
funcion.set_funcion_latex = "5*e**(x + y)"
funcion.formatear()
print(funcion.get_funcion)
print(funcion.get_funcion_latex)

funcion.set_funcion = "sin(x+pi/5) - sqrt(y + z)"
funcion.set_funcion_latex = "sin(x+pi/5) - sqrt(y + z)"
funcion.formatear()
print(funcion.get_funcion)
print(funcion.get_funcion_latex) """
