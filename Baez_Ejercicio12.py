a = int(input("Ingrese un número para evaluar en qué posición de la lista está: "))
l = []
b = int(input("Ingrese el primer valor de la lista: "))
c = int(input("Ingrese el segundo valor de la lista: "))
d = int(input("Ingrese el tercer valor de la lista: "))

l = [b, c, d]

if a in l:
    print(f"El número {a} está en la posición {l.index(a)}")
else:
    print("-1")

