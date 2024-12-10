class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.salario_hora = float(input("Ingrese el salario básico por hora del empleado: "))
        self.horas_trabajadas = int(input("Ingrese el número de horas trabajadas en el mes: "))

    def calcular_salario_mensual(self):
        salario_mensual = self.salario_hora * self.horas_trabajadas
        return salario_mensual

    def mostrar_resultado(self):
        salario_mensual = self.calcular_salario_mensual()
        if salario_mensual > 450000:
            print(f"Nombre del empleado: {self.nombre}")
            print(f"Salario mensual: ${salario_mensual:.2f}")
        else:
            print(f"Nombre del empleado: {self.nombre}")
            print("El salario mensual es menor o igual a $450,000.")


# Crear instancia de Empleado y mostrar el resultado
empleado = Empleado()
empleado.mostrar_resultado()
