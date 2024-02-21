import math

def sumar(*args):
    resultado = 0
    for n in args:
        resultado += n
    return resultado

def restar(*args):
    if len(args) < 2:
        return "Se requieren al menos dos números para realizar una resta."
    resultado = args[0]
    for num in args[1:]:
        resultado -= num
    return f"El resultado de la resta es: {resultado}"

def multiplicar(*args):
    if len(args) < 2:
        return "Se requieren al menos 2 datos para multiplicar"
    resultado = 1
    for num in args:
        resultado *= num
    return f"El resultado de la multiplicación es {resultado}"

def dividir(*args):
    if len(args) < 2:
        return "Se requieren al menos dos números para dividir"
    resultado = args[0]
    for num in args[1:]:
        resultado /= num
    return resultado

def modulo(*args):
    if len(args) < 2:
        return "Se requieren al menos dos números para obtener su módulo"
    resultado = args[0]
    for num in args[1:]:
        resultado %= num
    return resultado

def division_entera(*args):
    if len(args) < 2:
        return "Se requieren al menos dos números para la división entera"
    resultado = args[0]
    for num in args[1:]:
        resultado //= num
    return resultado

def potencia(*args):
    if len(args) < 2:
        return "Se requieren al menos dos argumentos: base y exponente"
    base, exponente = args
    resultado = base ** exponente
    return f"El resultado de {base} elevado a la potencia {exponente} es: {resultado}"

def raiz_cuadrada(*args):
    if len(args) != 1:
        return "Se requiere exactamente un argumento para calcular la raíz cuadrada."
    numero = args[0]
    if numero < 0:
        return "No se puede calcular la raíz cuadrada de un número negativo."
    resultado = math.sqrt(numero)
    return f"La raíz cuadrada de {numero} es aproximadamente {resultado:.2f}"
def calculadora():
    while True:
        print("\nCALCULADORA")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Módulo")
        print("6. División Entera")
        print("7. Potencia")
        print("8. Raíz Cuadrada")
        print("9. Salir")

        opcion = input("\nSeleccione una opción (1-9): ")

        if opcion == "9":
            print("Saliendo de la calculadora.")
            break

        elif opcion in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            try:
                nums = [float(num) for num in input("Ingrese los números separados por un guion - : ").split("-")]
            except ValueError:
                print("Error: Ingrese números válidos.")
                continue

            if opcion == "1":
                print(f"Usted escogio SUMAR {nums} ")
                print("Resultado:", sumar(*nums))
            elif opcion == "2":
                print(f"Usted escogio RESTAR {nums} ")
                print("Resultado:", restar(*nums))
            elif opcion == "3":
                print(f"Usted escogio MULTIPLICAR {nums} ")
                print("Resultado:", multiplicar(*nums))
            elif opcion == "4":
                print(f"Usted escogio DIVIDIR {nums} ")
                print("Resultado:", dividir(*nums))
            elif opcion == "5": 
                print(f"Usted escogio MODULO {nums} ")
                print("Resultado:", modulo(*nums))
            elif opcion == "6":
                print(f"Usted escogio DIVISION ENTERA {nums} ")
                print("Resultado:", division_entera(*nums))
            elif opcion == "7":
                print(f"Usted escogio PONTENCIACION {nums} ")
                print("Resultado:", potencia(*nums))
            elif opcion == "8":
                print(f"Usted escogio RAIZ CUADRADA {nums} ")
                print("Resultado:", raiz_cuadrada(*nums))

        else:
            print("Opción no válida. Por favor, seleccione una opción válida (1-9).")

if __name__ == "__main__":
    calculadora()