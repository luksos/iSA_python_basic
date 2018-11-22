
range1 = range(1,15)
lista1 = [1, 2, 3, 'cztery']
lista1[1] = 'dwa'
lista1.append(5)
del(lista1[0])
lista2 = list("dwa")
lista3 = list(lista1)
lista4 = list(range1)

print(range1)
print(lista1)
print(lista1[0])
print(lista1[3])
print(lista1.pop())
print(lista1)
lista1.remove(3)
print(lista1)
# print(lista2)
# print(lista3)
# print(lista4)
