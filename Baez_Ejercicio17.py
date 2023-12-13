a = input("Ingrese el primer elemento de la lista: ")
b = input("Ingrese el segundo elemento de la lista: ")
c = input("Ingrese el tercer elemento de la lista: ")
d = input("Ingrese el cuarto elemento de la lista: ")
e = input("Ingrese un nuevo elemento a la lista: ")
p = int(input(
    "Ingrese una posición en la que insertar este nuevo elemento de la lista \n"
    "(tenga en cuenta que las posiciones van desde 0 a 3): "))

l = [a, b, c, d]

l.insert(p, e)

print("La lista actualizada es: ", l)
