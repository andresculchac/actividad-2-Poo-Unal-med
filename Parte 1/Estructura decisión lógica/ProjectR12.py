class Trabajador:
    def __init__(self):
        self.nombres = input("Ingrese los nombres del trabajador: ")
        self.horas_trabajadas = float(input("Ingrese el número de horas trabajadas en la semana: "))
        self.valor_hora = float(input("Ingrese el valor recibido por una hora normal de trabajo: "))

    def calcular_salario(self):
        if self.horas_trabajadas <= 40:
            salario = self.horas_trabajadas * self.valor_hora
        elif self.horas_trabajadas > 40 and self.horas_trabajadas <= 48:
            horas_normales = 40
            horas_extra = self.horas_trabajadas - horas_normales
            salario = (horas_normales * self.valor_hora) + (horas_extra * self.valor_hora * 1.25)
        else:
            horas_normales = 40
            horas_extra = 8
            horas_dobles = self.horas_trabajadas - 48
            salario = (horas_normales * self.valor_hora) + (horas_extra * self.valor_hora * 1.25) + (horas_dobles * self.valor_hora * 1.5)
        return salario

    def mostrar_informacion(self):
        salario = self.calcular_salario()
        print("Nombres del trabajador:", self.nombres)
        print("Salario semanal: $", round(salario, 2))

# Crear una instancia de Trabajador y mostrar la información
trabajador = Trabajador()
trabajador.mostrar_informacion()
