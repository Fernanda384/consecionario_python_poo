from automovil import Automovil
from moto import Moto


def main():
    a1 = Automovil("Toyota", "Corolla", 20000, 0)
    print(a1)
    print(f"Impuesto: {a1.impuesto():.2f}")

    a2 = Automovil("Ford", "Fiesta", 18000, 5)
    print(a2)
    print(f"Impuesto: {a2.impuesto():.2f}")

    m1 = Moto("Honda", "CB125", 1500, 0)
    print(m1)
    print(f"Impuesto: {m1.impuesto():.2f}")

    m2 = Moto("Yamaha", "R3", 7000, 321)
    print(m2)
    print(f"Impuesto: {m2.impuesto():.2f}")


main()
