from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, precio_base: float, puertas: int):
        super().__init__(marca, modelo, precio_base)
        if puertas <= 0:
            self.puertas = 4
            print("El numero de puertas no puede ser menor o igual a 0, se asigno un valor de 4")
        else:
            self.puertas = puertas

    def get_puertas(self) -> int:
        return self.puertas
    
    def impuesto(self) -> float:
        impuesto = self.get_precio_base() * 0.08
        if self.puertas == 5:
            impuesto = impuesto - (self.get_precio_base() * 0.01)
        return impuesto

    def __str__(self) -> str:
        return f"{super().__str__()}, Puertas: {self.puertas}"
