class Empresa:
    def __init__(self):
        self.ventas_departamento1 = float(input("Ingrese el importe de ventas del departamento 1: "))
        self.ventas_departamento2 = float(input("Ingrese el importe de ventas del departamento 2: "))
        self.ventas_departamento3 = float(input("Ingrese el importe de ventas del departamento 3: "))
        self.salario_vendedores = float(input("Ingrese el salario de los vendedores de cada departamento: "))

    def calcular_incentivos(self):
        ventas_totales = self.ventas_departamento1 + self.ventas_departamento2 + self.ventas_departamento3
        incentivos_dep1 = 0
        incentivos_dep2 = 0
        incentivos_dep3 = 0

        if self.ventas_departamento1 > 0.33 * ventas_totales:
            incentivos_dep1 = 0.2 * self.salario_vendedores
        if self.ventas_departamento2 > 0.33 * ventas_totales:
            incentivos_dep2 = 0.2 * self.salario_vendedores
        if self.ventas_departamento3 > 0.33 * ventas_totales:
            incentivos_dep3 = 0.2 * self.salario_vendedores

        return incentivos_dep1, incentivos_dep2, incentivos_dep3

    def calcular_pago_final(self):
        incentivos_dep1, incentivos_dep2, incentivos_dep3 = self.calcular_incentivos()
        salario_final_dep1 = self.salario_vendedores + incentivos_dep1
        salario_final_dep2 = self.salario_vendedores + incentivos_dep2
        salario_final_dep3 = self.salario_vendedores + incentivos_dep3
        return salario_final_dep1, salario_final_dep2, salario_final_dep3

    def mostrar_salario_final(self):
        salario_final_dep1, salario_final_dep2, salario_final_dep3 = self.calcular_pago_final()
        print("Valor recibido por salario en el departamento 1: $", round(salario_final_dep1, 2))
        print("Valor recibido por salario en el departamento 2: $", round(salario_final_dep2, 2))
        print("Valor recibido por salario en el departamento 3: $", round(salario_final_dep3, 2))
empresa = Empresa()
empresa.mostrar_salario_final()
