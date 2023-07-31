def agregar_tarea(tareas, usuario, titulo):
    if usuario not in tareas:
        tareas[usuario] = []
    tareas[usuario].append({"titulo": titulo, "completada": False})
    print(f"Tarea '{titulo}' agregada para el usuario {usuario}.")

def mostrar_tareas_pendientes(tareas, usuario):
    if usuario in tareas:
        tareas_pendientes = [tarea["titulo"] for tarea in tareas[usuario] if not tarea["completada"]]
        if tareas_pendientes:
            print(f"Tareas pendientes para el usuario {usuario}:")
            for tarea in tareas_pendientes:
                print(f" - {tarea}")
        else:
            print(f"No hay tareas pendientes para el usuario {usuario}.")
    else:
        print(f"No se encontraron tareas para el usuario {usuario}.")

def mostrar_tareas_completadas(tareas, usuario):
    if usuario in tareas:
        tareas_completadas = [tarea["titulo"] for tarea in tareas[usuario] if tarea["completada"]]
        if tareas_completadas:
            print(f"Tareas completadas para el usuario {usuario}:")
            for tarea in tareas_completadas:
                print(f" - {tarea}")
        else:
            print(f"No hay tareas completadas para el usuario {usuario}.")
    else:
        print(f"No se encontraron tareas para el usuario {usuario}.")

def marcar_tarea_completada(tareas, usuario, titulo):
    if usuario in tareas:
        for tarea in tareas[usuario]:
            if tarea["titulo"] == titulo:
                tarea["completada"] = True
                print(f"Tarea '{titulo}' marcada como completada para el usuario {usuario}.")
                return
        print(f"No se encontró la tarea '{titulo}' para el usuario {usuario}.")
    else:
        print(f"No se encontraron tareas para el usuario {usuario}.")

if __name__ == "__main__":
    tareas_usuarios = {}

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar tareas pendientes de un usuario")
        print("4. Mostrar tareas completadas de un usuario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = input("Ingrese el nombre del usuario: ")
            titulo = input("Ingrese el título de la tarea: ")
            agregar_tarea(tareas_usuarios, usuario, titulo)
        elif opcion == "2":
            usuario = input("Ingrese el nombre del usuario: ")
            titulo = input("Ingrese el título de la tarea completada: ")
            marcar_tarea_completada(tareas_usuarios, usuario, titulo)
        elif opcion == "3":
            usuario = input("Ingrese el nombre del usuario: ")
            mostrar_tareas_pendientes(tareas_usuarios, usuario)
        elif opcion == "4":
            usuario = input("Ingrese el nombre del usuario: ")
            mostrar_tareas_completadas(tareas_usuarios, usuario)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
