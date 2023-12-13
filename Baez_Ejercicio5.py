t = [5, 10, 15, 20, 25]
n = int(input("Ingrese el número por el cual se van a multiplicar los elementos de la lista: "))

t2 = [n * t[0], n * t[1], n * t[2], n * t[3], n * t[4]]

# for i in t:
#   t2.append(i*n)

print("Lista original:", t)
print("Lista modificada multiplicada por", n, t2)
