l = [34, 3.2, "Juan", "Pedro", -2]
print("Vamos a trabajar con la siguiente lista:", l)
string = input("Ingrese un string para agregar al final de la lista: ")
l.append(string)
print("Lista actualizada:", l)
print("Ahora ingrese un elemento para evaluar cuántas veces está en la lista")
opcion = int(input("Qué tipo de elemento desea? (Entero: 1/Flotante: 2/String: 3): "))
if opcion == 1:
    nuevoElemento = int(input("Escriba el número entero: "))
else:
    if opcion == 2:
        nuevoElemento = float(input("Escriba el número flotante: "))
    else:
        nuevoElemento = input("Escriba el string: ")

print("La lista es:", l)
print(f"Y el elemento ingresado: {nuevoElemento} está {l.count(nuevoElemento)} vez/veces en la lista")