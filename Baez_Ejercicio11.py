a = int(input("Ingrese un número para luego evaluar si está o no en una lista: "))
l = []
b = int(input("Ingrese el primer valor de la lista: "))
c = int(input("Ingrese el segundo valor de la lista: "))
d = int(input("Ingrese el tercer valor de la lista: "))

#l = [a, b, c, d]

#print("El número", a, "está en la lista?", (l[0] == l[1] or l[0] == l[2] or l[0] == l[3]))

l = [b, c, d]

print("El número", a, "está en la lista", l, "?", a in l)
