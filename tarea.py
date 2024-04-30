#En esta actividad, ampliarás el programa de gestión de tareas proporcionado para incluir la capacidad de marcar una tarea como completada. Esto te permitirá practicar la modificación de funciones existentes y la adición de nuevas funcionalidades a un programa en Python.
#Instrucciones:
#Modificar la Función agregar_tarea:
#Añadir un nuevo parámetro opcional llamado completada a la función agregar_tarea.
#Por defecto, establecer el valor de completada en False para indicar que la tarea no está completada inicialmente.
#Agregar la Función marcar_completada:
#Crear una nueva función llamada marcar_completada que acepte la lista de tareas como argumento.
#Solicitar al usuario que ingrese el número de índice de la tarea que desea marcar como completada.
#Si el índice es válido, cambiar el valor del campo completada de la tarea correspondiente a True.
#Imprimir un mensaje indicando que la tarea ha sido marcada como completada.
#Si el índice es inválido, imprimir un mensaje de error.
#Modificar la Función mostrar_tareas:
#Añadir un nuevo parámetro opcional llamado completadas a la función mostrar_tareas.
#Si completadas es True, mostrar solo las tareas completadas.
#Si completadas es False, mostrar solo las tareas no completadas.
#Si completadas no se proporciona o es None, mostrar todas las tareas como se hacía anteriormente.
#Actualizar el Menú Principal:
#Agregar una nueva opción en el menú principal para "Marcar tarea como completada".
#Asociar esta opción con la llamada a la función marcar_completada.
#Probar y Depurar:
#Ejecutar el programa y probar todas las funcionalidades nuevas y existentes.
#Depurar cualquier error o comportamiento inesperado que encuentres.
#Entrega:
#Cuando hayas completado la implementación y depuración, ejecuta el programa y asegúrate de que todas las funcionalidades funcionen correctamente.
#Adjunta el archivo Python con tu implementación y una breve descripción de cualquier problema que hayas encontrado y cómo lo solucionaste.
#CONSEJO: como sugerencia antes de realizar esta actividad prueben la resolución que les envió para que puedan ver como funciona y se pueda entender la lógica del código.


def agregar_tarea(tareas, descripcion, completada=False):
    tarea = {"descripcion": descripcion, "completada": completada}
    tareas.append(tarea)
    print("Tarea agregada correctamente.")

def marcar_completada(tareas):
    indice = int(input("Ingrese el número de índice de la tarea que desea marcar como completada: "))
    if indice >= 0 and indice < len(tareas):
        tareas[indice]["completada"] = True
        print("La tarea ha sido marcada como completada.")
    else:
        print("Error: Índice inválido.")

def mostrar_tareas(tareas, completadas=None):
    if completadas is None:
        print("Todas las tareas:")
        for i, tarea in enumerate(tareas):
            print(f"{i}. [{ 'x' if tarea['completada'] else ' ' }] {tarea['descripcion']}")
    else:
        print("Tareas completadas:" if completadas else "Tareas pendientes:")
        for i, tarea in enumerate(tareas):
            if tarea["completada"] == completadas:
                print(f"{i}. {tarea['descripcion']}")

def menu():
    tareas = []
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Mostrar tareas completadas")
        print("5. Mostrar tareas pendientes")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            agregar_tarea(tareas, descripcion)
        elif opcion == "2":
            marcar_completada(tareas)
        elif opcion == "3":
            mostrar_tareas(tareas)
        elif opcion == "4":
            mostrar_tareas(tareas, completadas=True)
        elif opcion == "5":
            mostrar_tareas(tareas, completadas=False)
        elif opcion == "6":
            print("¡Buena suerte con proximas tareas!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida del menú.")

menu()
