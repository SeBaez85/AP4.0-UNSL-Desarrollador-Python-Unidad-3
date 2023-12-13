a = int(input("Ingrese el primer valor de la lista: "))
b = int(input("Ingrese el segundo valor de la lista: "))
c = int(input("Ingrese el tercer valor de la lista: "))
d = int(input("Ingrese el cuarto valor de la lista: "))

l = [a, b, c, d]

n = int(input("Ingrese el número por el cual se van a sumar los elementos de la lista: "))

s = [n + l[0], n + l[1], n + l[2], n + l[3]]

m = int(input("Ingrese el número por el cual se van a restar los elementos de la lista: "))

r = [l[0] - m, l[1] - m, l[2] - m, l[3] - m]

print("Lista original:", l)
print("Lista con los valores de la lista sumados a", n, ":",s)
print("Lista con los valores de la lista restados a", m, ":",r)
