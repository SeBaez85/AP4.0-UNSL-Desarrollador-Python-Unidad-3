notas = [9, 7, 4, 8, 6]

print(notas)
print("La cuarta nota es:", notas[3])

#Si intento imprimir o acceder a un índice en el que no hay una nota, por ejemplo:
#print(notas[8])
#Me encuentro con la excepción "IndexError: list index out of range" y se corta la ejecución del programa

#La longitud de una lista se calcula con la función len:
print("La longitud de la lista es:", len(notas))