class MayorNumero:
    def __init__(self):
        self.num1 = int(input("Ingrese el primer número entero: "))
        self.num2 = int(input("Ingrese el segundo número entero: "))
        self.num3 = int(input("Ingrese el tercer número entero: "))

    def encontrar_mayor(self):
        if self.num1 > self.num2 and self.num1 > self.num3:
            return self.num1
        elif self.num2 > self.num1 and self.num2 > self.num3:
            return self.num2
        else:
            return self.num3

    def mostrar_resultado(self):
        mayor = self.encontrar_mayor()
        print("El mayor número es:", mayor)

mayor_numero = MayorNumero()
mayor_numero.mostrar_resultado()
