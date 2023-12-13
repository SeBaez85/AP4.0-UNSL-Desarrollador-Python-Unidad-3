print("Vamos a averiguar el valor máximo y el mínimo dentro de una lista con los números ingresados")
l = []
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
d = int(input("Ingrese el cuarto número: "))
e = int(input("Ingrese el quinto número: "))
f = int(input("Ingrese el sexto número: "))

l = [a, b, c, d, e, f]
l.sort()

mayor = max(l)
menor = min(l)

print("La lista con los números ingresados ordenados de menor a mayor es: ", l)
print("El elemento mayor es:", mayor)
print("El elemento menor es:", menor)
