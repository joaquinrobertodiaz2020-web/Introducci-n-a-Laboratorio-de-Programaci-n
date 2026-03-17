#se quiere realizar un programa que lea por 
# teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
# A continuacion debe mostrar todas las notas,
# la nota media, la nota mas alta que ha sacado y la menor
notas = []

for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1} (0-10): "))
    
    while nota < 0 or nota > 10:
        print("Error. La nota debe estar entre 0 y 10.")
        nota = float(input(f"Ingrese nuevamente la nota {i+1}: "))
    
    notas.append(nota)

print("Notas ingresadas:", notas)

promedio = sum(notas) / len(notas)

nota_max = max(notas)
nota_min = min(notas)

print("Promedio:", promedio)
print("Nota más alta:", nota_max)
print("Nota más baja:", nota_min)