class Almacen:
    def __init__(self):
        self.valor_compra = float(input("Ingrese el valor de la compra: "))
        self.color_bolita = input("Ingrese el color de la bolita (blanca, verde, amarilla, azul, roja): ").lower()

    def calcular_descuento(self):
        if self.color_bolita == "blanca":
            descuento = 0
        elif self.color_bolita == "verde":
            descuento = 0.1
        elif self.color_bolita == "amarilla":
            descuento = 0.25
        elif self.color_bolita == "azul":
            descuento = 0.5
        elif self.color_bolita == "roja":
            descuento = 1
        else:
            print("Color de bolita no válido.")
            descuento = 0
        return descuento

    def calcular_valor_final(self):
        descuento = self.calcular_descuento()
        valor_final = self.valor_compra * (1 - descuento)
        return valor_final

    def mostrar_valor_final(self):
        valor_final = self.calcular_valor_final()
        print("Valor a pagar teniendo en cuenta los posibles descuentos: $", round(valor_final, 2))

almacen = Almacen()
almacen.mostrar_valor_final()
