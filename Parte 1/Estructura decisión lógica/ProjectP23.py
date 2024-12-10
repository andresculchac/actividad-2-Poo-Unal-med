import math

class EcuacionSegundoGrado:
    def __init__(self):
        self.a = float(input("Ingrese el coeficiente 'A': "))
        self.b = float(input("Ingrese el coeficiente 'B': "))
        self.c = float(input("Ingrese el coeficiente 'C': "))

    def calcular_soluciones(self):
        discriminante = self.b**2 - 4 * self.a * self.c
        if discriminante > 0:
            raiz_discriminante = math.sqrt(discriminante)
            solucion1 = (-self.b + raiz_discriminante) / (2 * self.a)
            solucion2 = (-self.b - raiz_discriminante) / (2 * self.a)
            return solucion1, solucion2
        elif discriminante == 0:
            solucion_unica = -self.b / (2 * self.a)
            return solucion_unica,
        else:
            return "No tiene soluciones reales."

    def mostrar_soluciones(self):
        soluciones = self.calcular_soluciones()
        print("Soluciones de la ecuación de segundo grado:")
        if isinstance(soluciones, str):  # Si es un mensaje
            print(soluciones)
        else:  # Si es una lista o tupla de soluciones
            for solucion in soluciones:
                print(solucion)

ecuacion = EcuacionSegundoGrado()
ecuacion.mostrar_soluciones()
