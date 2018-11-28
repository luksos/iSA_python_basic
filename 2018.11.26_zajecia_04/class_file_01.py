#
# liczby = range(0, 50)
#
# for i in liczby:
#     if i%2 != 0:
#         continue
#     print(i)
#
# # wersja druga
# liczby = range(0, 50, 2)
#
# for i in liczby:
#     print(i)
#
# tekst = "ala ma kota"
# for i in tekst:
#     print(i)
#
# tekst = list(tekst)
# for i in tekst:
#     print(i)

lista_imion = ['Ola', 'Ala', 'Tomek', 'Jakub']
lista_nazwisk = ['Kowalska', 'Turek', 'Ukuje', 'Kasprzycki']

# for imie in lista_imion:
#     print(imie)
#
# for indeks, imie in enumerate(lista_imion):
#     print(indeks, '-', imie)
#     print('Na pozycji: {} jest imie {}'.format(indeks, imie))

for imie, nawisko in zip(lista_imion, lista_nazwisk):
    print('{} {}'.format(imie, nawisko))

