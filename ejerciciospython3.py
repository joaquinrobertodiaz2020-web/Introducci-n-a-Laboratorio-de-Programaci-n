#1. Define una lista de diccionarios que represente información personal.nombre,edad. Luego, accede a elementos específicos de la lista, como el primer diccionario, el nombre de la primera persona y la edad de la segunda persona, para finalmente imprimir los resultados en la consola.
#personas = [
#    {"nombre": "Juan", "edad": 20},
#    {"nombre": "Maria", "edad": 25},
#    {"nombre": "Pedro", "edad": 30}
#]

#print("primer diccionario:", personas[0])

#print("nombre de la primera persona:", personas[0]["nombre"])

#print("edad de la segunda persona:", personas[1]["edad"])

#1.2. Del punto 1, recorrer y mostrar k,v

#personas = [
#    {"nombre": "Juan", "edad": 20},
#    {"nombre": "Maria", "edad": 25},
#    {"nombre": "Pedro", "edad": 30}
#]

#for persona in personas:
#    print("persona:")
    
#    for k, v in persona.items():
#        print(k, ":", v)
    
#    print()

# Funciones:
#2. Definir función, parámetros, retorno, capturar un valor o varios

#def calcular_suma_y_promedio(a, b):
#    suma = a + b
#    promedio = suma / 2
#    return suma, promedio 

#resultado_suma, resultado_promedio = calcular_suma_y_promedio(10, 20)

#print("suma:", resultado_suma)
#print("promedio:", resultado_promedio)

#3. Contar palabras

#def contar_palabras(texto):
#    palabras = texto.split()
#    return len(palabras)

#frase = input("ingrese una frase: ")

#cantidad = contar_palabras(frase)

#print("cantidad de palabras:", cantidad)

#4. Verificación de Palíndromos

#def es_palindromo(texto):
#    texto = texto.lower().replace(" ", "")
#    return texto == texto[::-1]

#frase = input("ingrese una palabra o frase: ")

#if es_palindromo(frase):
#    print("es palindromo")
#else:
#    print("no es palindromo")

#5. Lambda para sumar, potencia

#sumar = lambda a, b: a + b

#potencia = lambda base, exp: base ** exp

#print("suma:", sumar(5, 3))
#print("potencia:", potencia(2, 4))

#6. map() con lambda

#numeros = [1, 2, 3, 4, 5]

#resultado = list(map(lambda x: x * 2, numeros))

#print("lista original:", numeros)
#print("lista multiplicada:", resultado)

#7. Integrador: Crear programa que permita al usuario agregar tareas con descripción, fecha límite y prioridad, así como mostrar la lista de tareas. Este menú se repite hasta que el usuario elige salir."
#def agregar_tarea(tareas):
#    descripcion = input("ingrese la descripcion de la tarea: ")
#    fecha = input("ingrese la fecha limite: ")
#    prioridad = input("ingrese la prioridad (alta, media, baja): ")
    
#    tarea = {
#        "descripcion": descripcion,
#        "fecha": fecha,
#        "prioridad": prioridad
#    }
    
#    tareas.append(tarea)
#    print("tarea agregada correctamente")


#def mostrar_tareas(tareas):
#    if len(tareas) == 0:
#        print("no hay tareas cargadas")
#    else:
#        print("lista de tareas:")
#        for i, tarea in enumerate(tareas, start=1):
#            print("tarea", i)
#            for k, v in tarea.items():
#                print(k, ":", v)


#def menu():
#    tareas = []  
#    while True:
#        print("1. agregar tarea")
#        print("2. mostrar tareas")
#        print("3. salir")
        
#        opcion = input("elija una opcion: ")
        
#        if opcion == "1":
#            agregar_tarea(tareas)
#        elif opcion == "2":
#            mostrar_tareas(tareas)
#        elif opcion == "3":
#            print("saliendo del programa")
#            break
#        else:
#            print("opcion invalida")


#menu()