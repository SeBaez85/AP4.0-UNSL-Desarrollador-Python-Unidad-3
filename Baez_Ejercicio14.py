a = int(input("Ingrese un número para luego evaluar cuántas veces está en una lista: "))
l = []
b = int(input("Ingrese el primer valor de la lista: "))
c = int(input("Ingrese el segundo valor de la lista: "))
d = int(input("Ingrese el tercer valor de la lista: "))

l = [b, c, d]

print(f"El número {a} está {l.count(a)} vez/veces en la lista")
