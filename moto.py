from vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, precio_base: float, cc: int):
        super().__init__(marca, modelo, precio_base)
        if cc <= 0:
            self.cc = 125
            print("El cilindraje no puede ser menor o igual a 0, se asigno un valor de 125")
        else:
            self.cc = cc

    def get_cc(self) -> int:
        return self.cc

    def impuesto(self) -> float:
        impuesto = self.get_precio_base()
        if self.cc <= 250:
            impuesto = impuesto * 0.05
        else:
            impuesto = impuesto * 0.09
        return impuesto

    def __str__(self) -> str:
        return f"{super().__str__()}, Cilindraje: {self.cc}"
