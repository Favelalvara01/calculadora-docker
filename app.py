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

def mostrar_menu():
    print("=" * 30)
    print("   CALCULADORA PYTHON")
    print("=" * 30)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("=" * 30)

def main():
    print("Bienvenido a la Calculadora")

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion (1-5): ")

        if opcion == "5":
            print("Saliendo... Hasta luego!")
            break

        if opcion not in ["1", "2", "3", "4"]:
            print("Opcion invalida. Intenta de nuevo.")
            continue

        try:
            a = float(input("Ingresa el primer numero: "))
            b = float(input("Ingresa el segundo numero: "))
        except ValueError:
            print("Por favor ingresa un numero valido.")
            continue

        if opcion == "1":
            print(f"Resultado: {a} + {b} = {sumar(a, b)}")
        elif opcion == "2":
            print(f"Resultado: {a} - {b} = {restar(a, b)}")
        elif opcion == "3":
            print(f"Resultado: {a} x {b} = {multiplicar(a, b)}")
        elif opcion == "4":
            print(f"Resultado: {a} / {b} = {dividir(a, b)}")

if __name__ == "__main__":
    main()