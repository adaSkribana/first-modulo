def evaluacion_rendimiento(): 
# Solicitar el nombre del alumno
    nombre = input("Ingrese el nombre del Alumno: ").capitalize()

# Solicitar la cantidad de asignaturas
    num_asignaturas = int(input("¿Cuántas asignaturas desea registrar? "))

# Crear un diccionario para almacenar las calificaciones
    calificaciones = {}

# Registrar nombres de asignaturas y calificaciones
    for i in range(num_asignaturas):
        asignatura = input(f"Ingrese el nombre de la asignatura {i + 1}: ").capitalize()
        calificaciones[asignatura] = []

        num_notas = int(input(f"Cuantas notas desea ingresar para {asignatura}: "))
        for j in range(num_notas):
            nota = float(input(f"Ingrese la calificación número {j + 1} para {asignatura}: "))
            calificaciones[asignatura].append(nota)

# Imprimir el diccionario de calificaciones
    print("\nCalificaciones:")
    for asignatura, notas in calificaciones.items():
        promedio = sum(notas) / len(notas)
        print(f"{asignatura}: {notas} (Promedio: {promedio:.2f})")

    if promedio < 4.0:
        print(f"El alumno {nombre} necesita subir tus calificaciones!")
    elif promedio >= 4.0 and promedio <= 5.5:
        print(f"El alumno {nombre} Tiene un desempeño aceptable")
    elif promedio >= 5.5 and promedio <= 6.5:
        print(f"El alumno {nombre} tiene un desempeño muy bueno!")
    else:
        print(f"Felicidades! {nombre}, tu desempeño es excelente!")
if __name__ == "__main__":
    evaluacion_rendimiento()
