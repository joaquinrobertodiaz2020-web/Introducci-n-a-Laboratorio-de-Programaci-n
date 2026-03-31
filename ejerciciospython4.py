def agregar_tarea(tareas, tarea, fecha_limite, prioridad, completada=False):  # actividad 1
    nueva_tarea = {
        "Tarea": tarea,
        "Fecha limite": fecha_limite,
        "Prioridad": prioridad,
        "Completada": completada  # actividad 1
    }
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")

# actividad 3
def mostrar_tareas(tareas, completadas=None):  # actividad 3
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        contador = 0  # actividad 3

        for i, tarea in enumerate(tareas, 1):
            # actividad 3
            if completadas is True and not tarea["Completada"]:
                continue
            if completadas is False and tarea["Completada"]:
                continue

            print(f"\nTarea {i}:")
            for clave, valor in tarea.items():
                print(f"{clave}: {valor}")
            contador += 1  # actividad 3

        if contador == 0:  # actividad 3
            print("No hay tareas para mostrar según el filtro.")

# actividad 2
def marcar_completada(tareas):
    if not tareas:  # actividad 2
        print("No hay tareas para marcar.")  # actividad 2
        return  # actividad 2

    try:
        indice = int(input("Ingrese el número de la tarea a completar: ")) - 1  # actividad 2

        if 0 <= indice < len(tareas):  # actividad 2
            tareas[indice]["Completada"] = True  # actividad 2
            print("Tarea marcada como completada.")  # actividad 2
        else:
            print("Índice inválido.")  # actividad 2

    except ValueError:  # actividad 2
        print("Debe ingresar un número válido.")  # actividad 2


if __name__ == "__main__":
    lista_tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar todas las tareas")  # actividad 3
        print("3. Marcar tarea como completada")  # actividad 4
        print("4. Mostrar tareas completadas")  # actividad 3
        print("5. Mostrar tareas pendientes")  # actividad 3
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea_nueva = input("Ingrese la descripción de la tarea: ")
            fecha_limite_nueva = input("Ingrese la fecha límite (formato: dd/mm/yyyy): ")
            prioridad_nueva = input("Ingrese la prioridad: ")

            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, prioridad_nueva)  # actividad 1

        elif opcion == "2":
            mostrar_tareas(lista_tareas)  # actividad 3

        elif opcion == "3":  # actividad 4
            marcar_completada(lista_tareas)  # actividad 4

        elif opcion == "4":  # actividad 3
            mostrar_tareas(lista_tareas, True)  # actividad 3

        elif opcion == "5":  # actividad 3
            mostrar_tareas(lista_tareas, False)  # actividad 3

        elif opcion == "6":
            break

        else:
            print("Opción no válida. Intente nuevamente.")


# actividad 5:
# probé todas las funcionalidades del programa:
#  agregar tareas
#  mostrar tareas
#  marcar tareas como completadas
#  filtrar tareas completadas y pendientes
# 
# detecté problemas al ingresar datos incorrectos (como letras en vez de números),
# los cuales solucioné utilizando manejo de excepciones (try/except)
# también se validaron los índices para evitar errores al seleccionar tareas inexistentes

# actividad 6:
# el programa fue ejecutado y probado correctamente
# todas las funcionalidades funcionan según lo solicitado
# no detecté errores luego de la depuración