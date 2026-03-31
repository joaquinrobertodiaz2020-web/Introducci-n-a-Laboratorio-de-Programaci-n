#1- Calculadora de índice de masa corporal (IMC):
#- Solicita al usuario que ingrese su peso en kg y su altura en metros.
#- Calcula el IMC utilizando la fórmula: IMC = peso / (altura * altura).
#- Muestra el IMC calculado y una categoría de peso según el IMC (talla s, talla m, talla l, talla xl).

#peso = float(input("ingresa tu peso en kg: "))
#altura = float(input("ingresa tu altura en metros: "))

#imc = peso / (altura * altura)

#if imc < 18.5:
#    categoria = "talla s"
#elif imc < 25:
#    categoria = "talla m"
#elif imc < 30:
#    categoria = "talla l"
#else:
#    categoria = "talla xl"

#print("tu imc es:", imc)
#print("categoria:", categoria)

#2- Conversor de temperaturas:
#Pide al usuario que ingrese una temperatura en grados Celsius.
#Convierte la temperatura a grados Fahrenheit utilizando la fórmula: Fahrenheit = (Celsius * 9/5) + 32.
#Imprime la temperatura en grados Fahrenheit.

#celsius = float(input("ingresa la temperatura en celsius: "))

#fahrenheit = (celsius * 9/5) + 32

#print("temperatura en fahrenheit:", fahrenheit)

#3- Generador de secuencia Fibonacci:
#Pide al usuario que ingrese un número entero positivo.
#Genera los primeros n números de la secuencia Fibonacci, donde n es el número ingresado por el usuario.
#Muestra la secuencia Fibonacci resultante.

#n = int(input("ingresa un numero entero positivo: "))

#a = 0
#b = 1

#print("secuencia fibonacci:")

#for i in range(n):
#    print(a, end=" ")
#    siguiente = a + b
#    a = b
#    b = siguiente

#4- Validador de contraseña:
#Solicita al usuario que cree una contraseña.
#Verifica si la contraseña cumple con los siguientes criterios:
#Tiene al menos 8 caracteres de longitud.
#Contiene al menos una letra mayúscula y una letra minúscula.
#Tiene al menos un número.
#Tiene al menos un carácter especial (por ejemplo, !, @, #, $, %, etc.).
#Informa al usuario si la contraseña es válida o no.

#contraseña = input("crea una contraseña: ")

#tiene_mayuscula = False
#tiene_minuscula = False
#tiene_numero = False
#tiene_especial = False

#especiales = "!@#$%^&*()-_=+[]{};:,.<>/?"

#for c in contraseña:
#    if c.isupper():
#        tiene_mayuscula = True
#    elif c.islower():
#        tiene_minuscula = True
#    elif c.isdigit():
#        tiene_numero = True
#    elif c in especiales:
#        tiene_especial = True

#if (len(contraseña) >= 8 and
#    tiene_mayuscula and
#    tiene_minuscula and
#    tiene_numero and
#    tiene_especial):
#    print("contraseña valida")
#else:
#    print("contraseña invalida")

#5- Juego de adivinanza de números:
#Genera un número aleatorio entre 1 y 100.
#Pide al usuario que adivine el número.
#Proporciona pistas al usuario si el número es demasiado alto o demasiado bajo.
#Continúa solicitando al usuario que adivine hasta que lo haga correctamente.
#Muestra el número de intentos necesarios para adivinar.

#import random

#numero = random.randint(1, 100)

#intentos = 0
#adivinanza = 0

#print("adivina el numero entre 1 y 100")

#while adivinanza != numero:
#    adivinanza = int(input("ingresa un numero: "))
#    intentos += 1

#    if adivinanza < numero:
#        print("mas alto")
#    elif adivinanza > numero:
#        print("mas bajo")
#    else:
#        print("correcto, adivinaste el numero")
#        print("cantidad de intentos:", intentos)

#6- Administrador de tareas:
#Permite al usuario agregar tareas con una descripción y una fecha de vencimiento.
#Muestra la lista de tareas agregadas.
#Permite al usuario marcar una tarea como completada y eliminar tareas de la lista.

#tareas = []

#while True:
#    print("menu:")
#    print("1. agregar tarea")
#    print("2. mostrar tareas")
#    print("3. marcar tarea como completada")
#    print("4. eliminar tarea")
#    print("5. salir")

#    opcion = input("elige una opcion: ")

#    if opcion == "1":
#        descripcion = input("descripcion de la tarea: ")
#        fecha = input("fecha de vencimiento: ")

#        tarea = {
#            "descripcion": descripcion,
#            "fecha": fecha,
#            "completada": False
#        }

#        tareas.append(tarea)
#        print("tarea agregada")

#    elif opcion == "2":
#        if len(tareas) == 0:
#            print("no hay tareas")
#        else:
#            for i, t in enumerate(tareas):
#                estado = "completada" if t["completada"] else "pendiente"
#                print(i, "-", t["descripcion"], "|", t["fecha"], "|", estado)

#    elif opcion == "3":
#        indice = int(input("ingresa el numero de tarea a completar: "))
#        if 0 <= indice < len(tareas):
#            tareas[indice]["completada"] = True
#            print("tarea marcada como completada")
#        else:
#            print("indice invalido")

#    elif opcion == "4":
#        indice = int(input("ingresa el numero de tarea a eliminar: "))
#        if 0 <= indice < len(tareas):
#            tareas.pop(indice)
#            print("tarea eliminada")
#        else:
#            print("indice invalido")

#    elif opcion == "5":
#        print("saliendo...")
#        break

#    else:
#        print("opcion invalida")

#7- Calculadora de descuento de compra:
#Solicita al usuario que ingrese el precio original del artículo y el porcentaje de descuento.
#Calcula el precio final después del descuento.
#Muestra el precio final al usuario.

#precio = float(input("ingresa el precio original: "))
#descuento = float(input("ingresa el porcentaje de descuento: "))

#precio_final = precio - (precio * descuento / 100)

#print("precio final:", precio_final)

#8- Generador de contraseñas aleatorias:
#Solicita al usuario que ingrese la longitud deseada para la contraseña.
#Genera una contraseña aleatoria con la longitud especificada.
#Utiliza caracteres alfanuméricos y caracteres especiales para mayor seguridad.
#Muestra la contraseña generada al usuario.

#import random
#import string

#longitud = int(input("ingresa la longitud de la contraseña: "))

#caracteres = string.ascii_letters + string.digits + string.punctuation

#contraseña = ""
#for i in range(longitud):
#    contraseña += random.choice(caracteres)

#print("contraseña generada:", contraseña)