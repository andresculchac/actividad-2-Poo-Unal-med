class Estudiante:
    def __init__(self):
        self.numero_inscripcion = input("Ingrese el número de inscripción del estudiante: ")
        self.nombres = input("Ingrese los nombres del estudiante: ")
        self.patrimonio = float(input("Ingrese el patrimonio del estudiante: "))
        self.estrato_social = int(input("Ingrese el estrato social del estudiante: "))

    def calcular_pago_matricula(self):
        pago_base = 50000
        if self.patrimonio > 2000000 and self.estrato_social > 3:
            aumento = self.patrimonio * 0.03
            return pago_base + aumento
        else:
            return pago_base

    def mostrar_informacion(self):
        pago_matricula = self.calcular_pago_matricula()
        print("Número de inscripción:", self.numero_inscripcion)
        print("Nombres:", self.nombres)
        print("Pago de matrícula: $", pago_matricula)

estudiante = Estudiante()
estudiante.mostrar_informacion()
