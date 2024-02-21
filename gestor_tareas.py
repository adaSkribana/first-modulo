def agregar_tareas():
    with open("tareas.txt", "a") as file:
        title_tarea = input("Ingresa un titulo para tu tarea pendiente: \n")
        tarea = input("Ingresa tu tarea pendiente: \n")
        file.write(title_tarea + ": " + tarea + "\n")

def mostrar_tareas():
    with open("tareas.txt", "r") as file:
        print(file.read())

def completar_tarea():
    titulo = input("Ingresa el título de la tarea que quieres marcar como completada: ")
    with open("tareas.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if titulo in line:
                line = line.strip() + " -completada\n"  # Agrega "-completada" al final de la línea
            file.write(line)
        file.truncate()
    print(f"Tarea '{titulo}' marcada como completada.")


def guardar_tareas():
    print("Tareas guardadas exitosamente en 'tareas.txt'")

def menu_tareas():
    while True:
        try:
            print('')
            print("Selecciona una opción: ")
            print("1 - Agregar Tarea")
            print("2 - Mostrar Tareas")
            print("3 - Completar Tarea")
            print("4 - Guardar Tareas")
            print("5 - Salir")
            opcion = int(input("Ingresa una opcion entre las dadas: "))
            if opcion == 1:
                agregar_tareas()
            elif opcion == 2:
                mostrar_tareas()
            elif opcion == 3:
                completar_tarea()
            elif opcion == 4:
                guardar_tareas()
            else:
                print("Gracias por usar nuestro gestor de tareas. El programa ha terminado.")
                break
        except Exception:
                print("ingrese una opción valida")

def gestor_tareas():
    menu_tareas()

if __name__ == "__main__":
    gestor_tareas()