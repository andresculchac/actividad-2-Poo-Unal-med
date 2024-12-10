class Trabajador:
    def __init__(self):
        self.nombres = input("Ingrese los nombres del trabajador: ")
        self.horas_trabajadas = float(input("Ingrese el número de horas trabajadas en la semana: "))
        self.valor_hora = float(input("Ingrese el valor recibido por una hora normal de trabajo:"))

    def calcular_salario(self):
        horas_normales = 40
        if self.horas_trabajadas <= horas_normales:
            salario = self.horas_trabajadas * self.valor_hora
        elif self.horas_trabajadas <= 48:
            horas_extra = self.horas_trabajadas - horas_normales
            salario = (horas_normales * self.valor_hora) + (horas_extra * self.valor_hora * 1.25)
        else:
            horas_extra_doble = 8
            horas_extra_triple = self.horas_trabajadas - 48
            salario = (
                (horas_normales * self.valor_hora) +
                (horas_extra_doble * self.valor_hora * 2) +
                (horas_extra_triple * self.valor_hora * 3)
            )
        return salario

    def mostrar_informacion(self):
        salario_devengado = self.calcular_salario()
        print("Nombre del trabajador:", self.nombres)
        print("Salario: $", round(salario_devengado, 2))

trabajador = Trabajador()
trabajador.mostrar_informacion()
