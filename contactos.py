"""
diccionario[clave]=valor
los [corchetes] se utilizan para acceder a un elemento dentro del diccionario. 
La clave es la parte que se encuentra dentro de los corchetes. 
En un diccionario, las claves son únicas y se utilizan para identificar los valores asociados.
=: El signo igual se utiliza para asignar un valor a una clave en el diccionario. 
En este caso, estamos asignando el valor de valor a la clave.
valor: Esto es lo que queremos almacenar en el diccionario. 
Puede ser cualquier tipo de dato: 
una cadena de texto, un número, una lista, otro diccionario, etc.

ERRORES
al comienzo, mi codigo tenia las variables iniciadas fuera de las funciones 
y solo deberia a ver iniciado el diccionario de esta manera para pasarselo de argumento
a mis funciones
y tenia las funciones mal definidas en cuanto a la sintaxis original de las intrucciones
del user
vista= contacto[user]
en mostrar contactos también estaba mal utilizando el metodo
 .items al llamarlo sin un ciclo for que iterara el diccionario me retornaba un print de mi llamada


"""
contactos={}

def agregar_contacto(contactos):
    nombre = input("Ingrese el nombre para su nuevo contacto: ")
    numero = int(input(f"Ingrese el número para {nombre}: "))
    contactos[nombre] = numero

def eliminar_contacto(contactos):
    print("**Esta acción es irreversible**")
    user = input("Ingrese el nombre del contacto que desea eliminar: ")
    if user in contactos: 
        del contactos[user]
    else:
        print(f"No se encontró el contacto {user}.")

def mostrar_contactos(contactos):
    print("Sus contactos son:")
    for nombre, numero in contactos.items():
        print(f"{nombre}: {numero}")
def gestor_contactos():
    while True:
        print("Contactos en Python")
        print("Ingrese entre las siguientes opciones:")
        print("1- Añadir contacto")
        print("2- Eliminar contacto")
        print("3- Mostrar contactos")
        print("4- Salir")

        try:
            option = int(input("Ingrese su elección: "))

            if option == 1:
                print("Opción 1 seleccionada: Añadir contacto")
                agregar_contacto(contactos)
            # ...
            elif option == 2:
                print("Opción 2 seleccionada: Eliminar contacto")
                eliminar_contacto(contactos)
                print("Contacto eliminado exitosamente")
            
            # ...
            
            elif option == 3:
                print("Opción 3 seleccionada: Mostrar contactos")
                mostrar_contactos(contactos)
            elif option == 4:
                print("Gracias por usar nuestro gestor de contactos. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
        except ValueError:
            print("Error: Ingrese un número válido.")
if __name__ == "__main__":
    gestor_contactos()