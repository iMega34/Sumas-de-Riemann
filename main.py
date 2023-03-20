
from funcion import Funcion
from metodos import Metodos

import flet as ft
from flet.matplotlib_chart import MatplotlibChart


def main(page: ft.Page):

    def proc_input() -> tuple[Funcion, float, float, int]:
        """
        Toma los valores de los cuadros de texto y los devuelve como una tupla.
        :return: Una tupla de la función, el límite inferior, el límite superior y el delta t.
        """
        funcion: Funcion = Funcion()
        funcion.set_funcion = txt_funcion.value
        lim_inf: float = float(txt_lim_inf.value)
        lim_sup: float = float(txt_lim_sup.value)
        del_t: int = int(txt_del_t.value)

        return funcion, lim_inf, lim_sup, del_t


    def calc_punto_izq(func) -> None:
        """
        Llama a la función de aproximación por punto izquierdo de la clase Metodos, y
        devuelve dos valores: un área y un gráfico. Luego, la función muestra el área y el gráfico en la
        GUI
        """
        funcion, lim_inf, lim_sup, del_t = proc_input()
        area, grafica = Metodos.punto_izquierdo(funcion, lim_inf, lim_sup, del_t)
        area_gui.value = f"El área aproximada bajo de la curva es {area:.6f} u2"
        grafica_gui.content = MatplotlibChart(grafica, original_size = True, expand = True, scale = 1.2)
        page.update()


    def calc_punto_der(func) -> None:
        """
        Llama a la función de aproximación por punto derecho de la clase Metodos, y
        devuelve dos valores: un área y un gráfico. Luego, la función muestra el área y el gráfico en la
        GUI
        """
        funcion, lim_inf, lim_sup, del_t = proc_input()
        area, grafica = Metodos.punto_derecho(funcion, lim_inf, lim_sup, del_t)
        area_gui.value = f"El área aproximada bajo de la curva es {area:.6f} u2"
        grafica_gui.content = MatplotlibChart(grafica, original_size = True, expand = True, scale = 1.2)
        page.update()


    def calc_punto_medio(func) -> None:
        """
        Llama a la función de aproximación por punto medio de la clase Metodos, y
        devuelve dos valores: un área y un gráfico. Luego, la función muestra el área y el gráfico en la
        GUI
        """
        funcion, lim_inf, lim_sup, del_t = proc_input()
        area, grafica = Metodos.punto_medio(funcion, lim_inf, lim_sup, del_t)
        area_gui.value = f"El área aproximada bajo de la curva es {area:.6f} u2"
        grafica_gui.content = MatplotlibChart(grafica, original_size = True, expand = True, scale = 1.2)
        page.update()


    def calc_trapecios(func) -> None:
        """
        Llama a la función de aproximación por trapecios de la clase Metodos, y
        devuelve dos valores: un área y un gráfico. Luego, la función muestra el área y el gráfico en la
        GUI
        """
        funcion, lim_inf, lim_sup, del_t = proc_input()
        area, grafica = Metodos.trapecio(funcion, lim_inf, lim_sup, del_t)
        area_gui.value = f"El área aproximada bajo de la curva es {area:.6f} u2"
        grafica_gui.content = MatplotlibChart(grafica, original_size = True, expand = True, scale = 1.2)
        page.update()

    # Propiedades de la ventana de la GUI
    page.title = "Sumas de Riemann"
    page.window_maximizable = False
    page.window_resizable = False
    page.window_width = 990
    page.window_height = 565
    page.padding = 35

    # Cuadros de texto y sus propiedades
    txt_funcion = ft.TextField(label = "Función", helper_text = "Ej. x^2 + 1", height = 75)
    txt_lim_inf = ft.TextField(label = "Límite inferior", height = 50)
    txt_lim_sup = ft.TextField(label = "Límite superior", height = 50)
    txt_del_t = ft.TextField(label = "Número de particiones", helper_text = "¡Solo números enteros!", height = 75)

    # Botones de métodos de integración y sus propiedades
    boton_suma_izq = ft.ElevatedButton(text = "Punto izquierdo", on_click = calc_punto_izq, width = 150)
    boton_suma_der = ft.ElevatedButton(text = "Punto derecho", on_click = calc_punto_der, width = 150)
    boton_suma_medio = ft.ElevatedButton(text = "Punto medio", on_click = calc_punto_medio, width = 150)
    boton_suma_trap = ft.ElevatedButton(text = "Trapecios", on_click = calc_trapecios, width = 150)

    # Función de ejemplo para la GUI
    funcion: Funcion = Funcion()
    funcion.set_funcion = "x**2 + 1"
    area, grafica = Metodos.punto_izquierdo(funcion, -2, 5, 6)

    # Cuadro modificable para la gráfica en la GUI
    grafica_gui: ft.Container = ft.Container(
                    content = MatplotlibChart(grafica, original_size = True, expand = True, scale = 1.2),
                    padding = 46,
                )

    # Cuadro modificable para el área en la GUI
    area_gui: ft.Text = ft.Text(
        f"El área aproximada bajo de la curva es {area:.6f} u2",
        font_family = "Verdana",
        color = ft.colors.AMBER_300,
        weight = ft.FontWeight.NORMAL,
        text_align = ft.TextAlign.CENTER,
        width = 560
    )

    page.add(
        ft.Row(
            [
                # Panel principal (cuadros de texto y botones) (495h x 315w) + 12w
                ft.Column(
                    [
                        # Texto de introducción (¿?h x 315w)
                        ft.Row(
                            controls = [
                                ft.Text(
                                    "Sumas de Riemann",
                                    size = 26,
                                    font_family = "Verdana",
                                    color = ft.colors.LIGHT_BLUE_200,
                                    weight = ft.FontWeight.BOLD,
                                    text_align = ft.TextAlign.CENTER,
                                    width = 315,
                                ),
                            ],
                        ),

                        # Cuadro de texto de funciones (75h x 315w)
                        ft.Row(
                            controls = [
                                ft.Column(
                                    controls = [
                                        txt_funcion
                                    ],
                                    width = 315
                                )
                            ],
                            height = 75
                        ),

                        # Cuadro de texto de delta t (75h x 315w)
                        ft.Row(
                            controls = [
                                ft.Column(
                                    controls = [
                                        txt_del_t
                                    ],
                                    width = 315
                                )
                            ],
                            height = 75
                        ),

                        # Cuadros de texto de limites de integración [(50h x 150w) * 2] + 15w
                        ft.Row(
                            controls = [
                                ft.Column(
                                    controls = [
                                        txt_lim_inf
                                    ],
                                    width = 150
                                ),
                                ft.Column(
                                    controls = [
                                        txt_lim_sup
                                    ],
                                    width = 150
                                )
                            ],
                            spacing = 15,
                            height = 50
                        ),

                        # Línea divisora (10h x 1w)
                        ft.Divider(
                            color = ft.colors.WHITE70,
                            height = 4,
                        ),

                        # Texto de métodos de integración (¿?h x 315w)
                        ft.Row(
                            controls = [
                                ft.Text(
                                    "Métodos de aproximación",
                                    font_family = "Verdana",
                                    color = ft.colors.LIGHT_BLUE_200,
                                    weight = ft.FontWeight.NORMAL,
                                    text_align = ft.TextAlign.CENTER,
                                    width = 315,
                                ),
                            ],
                        ),

                        # Línea divisora (10h x 1w)
                        ft.Divider(
                            color = ft.colors.WHITE70,
                            height = 4,
                        ),

                        # Botones de gráficas I [(¿?h x 150w) * 2] + 15w
                        ft.Row(
                            controls = [
                                ft.Column(
                                    controls = [
                                        boton_suma_izq
                                    ],
                                    width = 150
                                ),
                                ft.Column(
                                    controls = [
                                        boton_suma_der
                                    ],
                                    width = 150
                                )
                            ],
                            spacing = 15,
                        ),

                        # Botones de gráficas II [(¿?h x 150w) * 2] + 15w
                        ft.Row(
                            controls = [
                                ft.Column(
                                    controls = [
                                        boton_suma_medio
                                    ],
                                    width = 150
                                ),
                                ft.Column(
                                    controls = [
                                        boton_suma_trap
                                    ],
                                    width = 150
                                )
                            ],
                            spacing = 15,
                        )
                    ],
                    width = 315,
                    height = 495,
                    spacing = 10,
                    alignment = ft.MainAxisAlignment.CENTER,
                ),

                # Línea divisora
                ft.VerticalDivider(
                    color = ft.colors.RED
                ),

                # Gráfica y área aproximada bajo la curva
                ft.Column(
                    [
                        grafica_gui,
                        area_gui
                    ]
                )
            ],
            spacing = 10,
            expand = True
        )
    )

ft.app(target = main)