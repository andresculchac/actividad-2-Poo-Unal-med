class Esferas:
    def __init__(self):
        self.peso_esfera_a = float(input("A continuación suministre el diferente peso para 3 esferas, Ingrese el peso de la esfera A: "))
        self.peso_esfera_b = float(input("Ingrese el peso de la esfera B: "))
        self.peso_esfera_c = float(input("Ingrese el peso de la esfera C: "))

    def determinar_esfera_mayor(self):
        if self.peso_esfera_a > self.peso_esfera_b and self.peso_esfera_a > self.peso_esfera_c:
            return "A"
        elif self.peso_esfera_b > self.peso_esfera_a and self.peso_esfera_b > self.peso_esfera_c:
            return "B"
        elif self.peso_esfera_c > self.peso_esfera_a and self.peso_esfera_c > self.peso_esfera_b:
            return "C"
        else:
            return "No se puede determinar"

    def mostrar_esfera_mayor(self):
        esfera_mayor = self.determinar_esfera_mayor()
        print(f"La esfera de mayor peso es la {esfera_mayor}")

esferas = Esferas()
esferas.mostrar_esfera_mayor()
