def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

def main():
    print("=" * 30)
    print("   CALCULADORA PYTHON")
    print("=" * 30)

    print(f"10 + 5 = {sumar(10, 5)}")
    print(f"10 - 5 = {restar(10, 5)}")
    print(f"10 x 5 = {multiplicar(10, 5)}")
    print(f"10 / 5 = {dividir(10, 5)}")
    print(f"10 / 0 = {dividir(10, 0)}")

    print("=" * 30)
    print("Calculadora ejecutada correctamente")
    print("=" * 30)

if __name__ == "__main__":
    main()