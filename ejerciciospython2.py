#1  Escribe un programa que identifique el color de un objeto y muestre un mensaje según el color.

#color = input("ingresa el color del objeto: ")

#if color == "rojo":
#    print("el objeto es rojo, suele asociarse con peligro")

#if color == "azul":
#    print("el objeto es azul, suele asociarse con tranquilidad")

#if color == "verde":
#    print("el objeto es verde, suele asociarse con la naturaleza")

#if color != "rojo" and color != "azul" and color != "verde":
#    print("color no reconocido")

#2  Escribe un programa que muestre los números del 0 al 4 usando un ciclo while.

#i = 0

#while i <= 4:
#    print(i)
#    i += 1

#2 1. Escribe un programa que solicita al usuario que ingrese números enteros positivos y muestre la suma de esos números. La entrada de números continuará hasta que el usuario ingrese un número negativo, momento en el que el programa mostrará la suma total.

#suma = 0

#numero = int(input("ingrese un número entero positivo: "))

#while numero >= 0:
#    suma += numero
#    numero = int(input("ingrese otro número (negativo para terminar): "))

#print("la suma total es:", suma)

#3  Escribe un programa que muestra la primer, última u otra letra de una cadena de carcateres, inclusive una rebanada.

#texto = input("ingrese una cadena de caracteres: ")

#print("primera letra:", texto[0])

#print("última letra:", texto[-1])

#if len(texto) > 1:
#    print("segunda letra:", texto[1])

#print("rebanada (1 a 4):", texto[1:4])

#4  Crear una lista de frutas y mostrar en consola algunas frutas de la lista, también por rebanadas.

#frutas = ["manzana", "banana", "naranja", "pera", "uva", "kiwi"]

#print("primera fruta:", frutas[0])
#print("tercera fruta:", frutas[2])
#print("última fruta:", frutas[-1])

#print("primeras 3 frutas:", frutas[0:3])
#print("del medio:", frutas[2:5])
#print("todas desde la posición 1:", frutas[1:])

#5  Escribe un programa que recorra una lista de frutas y muestre cada fruta.

#frutas = ["manzana", "banana", "naranja", "pera", "uva"]

#for fruta in frutas:
#    print(fruta)

#5 1. Agregar otras frutas a la lista.

#frutas = ["manzana", "banana", "naranja"]

#frutas.append("pera")

#frutas.extend(["uva", "kiwi"])

#for fruta in frutas:
#    print(fruta)

#5 2. Escribe un programa verifique si una fruta específica está en una lista de frutas y muestra un mensaje correspondiente.

#frutas = ["manzana", "banana", "naranja", "pera", "uva"]

#buscar = input("ingrese una fruta: ")

#if buscar in frutas:
#    print("la fruta está en la lista")
#else:
#    print("la fruta NO está en la lista")

#6  Escribe un programa que recorra una lista de números y muestre si cada número es par o impar.

#numeros = [1, 2, 3, 4, 5, 6, 7, 8]

#for numero in numeros:
#    if numero % 2 == 0:
#        print(numero, "es par")
#    else:
#        print(numero, "es impar")

#7  Escribe un programa que recorra una cadena de texto y cuente cuántas veces aparece la letra 'a' en la cadena.

#texto = input("ingrese una cadena de texto: ")

#contador = 0

#for letra in texto:
#    if letra == "a":
#        contador += 1

#print("la letra 'a' aparece", contador, "veces")

#8  Integrador: Escribe un programa que permita a un usuario crear una lista de nombres. El programa continuará pidiendo nombres hasta que el usuario ingrese "fin". Luego, el programa mostrará la lista de nombres en orden alfabético, indicará cuántos nombres empiezan con la letra 'A' o 'E',y mostrará si un nombre específico está en la lista.
#nombres = []

#while True:
#    nombre = input("ingrese un nombre (o 'fin' para terminar): ")
    
#    if nombre.lower() == "fin":
#        break
    
#    nombres.append(nombre)

#nombres.sort()

#print("lista de nombres ordenada:")
#for n in nombres:
#    print(n)

#contador = 0
#for n in nombres:
#    if n.lower().startswith("a") or n.lower().startswith("e"):
#        contador += 1

#print("cantidad de nombres que empiezan con a o e:", contador)

#buscar = input("ingrese un nombre para buscar en la lista: ")

#if buscar in nombres:
#    print("el nombre está en la lista.")
#else:
#    print("el nombre no está en la lista.")
