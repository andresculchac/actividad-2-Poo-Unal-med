class Esferas:
    def __init__(self):
        self.peso_esfera_a = float(input("Ingrese el peso de la esfera A: "))
        self.peso_esfera_b = float(input("Ingrese el peso de la esfera B: "))
        self.peso_esfera_c = float(input("Ingrese el peso de la esfera C: "))
        self.peso_esfera_d = float(input("Ingrese el peso de la esfera D: "))

    def determinar_esfera_diferente(self):
        pesos = [self.peso_esfera_a, self.peso_esfera_b, self.peso_esfera_c, self.peso_esfera_d]
        pesos_unicos = set(pesos)
        for peso in pesos_unicos:
            if pesos.count(peso) == 1:
                esfera_diferente = peso
                break
        else:
            esfera_diferente = None  # Si no se encuentra una esfera diferente
        return esfera_diferente

    def comparar_peso_esfera_diferente(self, esfera_diferente):
        if esfera_diferente is None:
            return "No se encontró una esfera diferente."

        if esfera_diferente == self.peso_esfera_a:
            mensaje = "La esfera diferente es la A y es de menor peso que las otras tres."
        elif esfera_diferente == self.peso_esfera_b:
            mensaje = "La esfera diferente es la B y es de menor peso que las otras tres."
        elif esfera_diferente == self.peso_esfera_c:
            mensaje = "La esfera diferente es la C y es de menor peso que las otras tres."
        elif esfera_diferente == self.peso_esfera_d:
            mensaje = "La esfera diferente es la D y es de menor peso que las otras tres."
        else:
            mensaje = "No se encontró una esfera diferente."
        return mensaje


# Crear una instancia de Esferas y determinar la esfera diferente
esferas = Esferas()
esfera_diferente = esferas.determinar_esfera_diferente()
mensaje = esferas.comparar_peso_esfera_diferente(esfera_diferente)
print(mensaje)
