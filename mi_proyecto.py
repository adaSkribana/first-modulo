import gestor_tareas 
import evaluacion_rendimiento
import calculadora_avannzada_interactiva
import contactos

print("Bienvenido")

while True:
    try:
        print("Escoja entre las siguientes opciones:")
        print("1 - Organizar tareas")
        print("2 - Evaluar rendimiento")
        print("3 - Calculadora")
        print("4 - Contactos")
        print("5 - Salir")
        user = int(input("Ingrese el número correspondiente a su opción: "))

        if user <= 0 or user >= 6:
            print("Ingrese una opción válida")
            continue
        elif user == 5:
            print("Hasta pronto.")
            break
        elif user == 1:
            gestor_tareas.gestor_tareas()  # Llamar a la función principal de gestor_tareas
        elif user == 2:
            evaluacion_rendimiento.evaluacion_rendimiento()  # Llamar a la función principal de evaluacion_rendimiento
        elif user == 3:
            calculadora_avannzada_interactiva.calculadora()  # Llamar a la función principal de calculadora_avannzada_interactiva
        elif user == 4:
            contactos.contactos()  # Llamar a la función principal de contactos

    except ValueError:
        print("Ingrese un número válido como opción.")
