import copy

# listy są referencyjne!!!!!
lista_1 = ['a', 'b', 'c']
lista_2_1 = copy.copy(lista_1)
lista_2_2 = lista_1[:]
lista_3 = lista_1
lista_3[1] = 'd'

print(lista_1)      # oryginał
print(lista_2_1)    # kopia
print(lista_2_2)    # kopia
print(lista_3)      # referencja listy 1

lista_a = ['AAA', ['BBB', ['CCC', ['DDD']]]]
lista_b = lista_a
lista_c = copy.copy(lista_a)
lista_d = copy.deepcopy(lista_a)
lista_b[0] = 'XXX'
lista_b[1][0] = 'YYY'

print(lista_a)
print(lista_b)
print(lista_c)
print(lista_d)
