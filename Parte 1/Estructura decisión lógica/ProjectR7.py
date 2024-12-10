class Comparador:
    def __init__(self):
        self.valor_a = float(input("Ingrese el valor de A: "))
        self.valor_b = float(input("Ingrese el valor de B: "))

    def comparar_valores(self):
        if self.valor_a > self.valor_b:
            return "A es mayor que B."
        elif self.valor_a < self.valor_b:
            return "A es menor que B."
        else:
            return "A es igual a B."

    def mostrar_resultado(self):
        resultado = self.comparar_valores()
        print(resultado)

comparador = Comparador()
comparador.mostrar_resultado()
