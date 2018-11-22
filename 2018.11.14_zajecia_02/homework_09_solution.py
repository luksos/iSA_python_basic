"""
Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7


"""

liczba = 13456

# ver1
if liczba % 3 == 0:
    print('liczba podzielna przez 3')
elif liczba % 5 == 0:
    print('liczba podzielna przez 5')
else:
    print('liczba nie jest podzielna przez 3 i 5')

# ver2
if liczba % 3 == 0 and liczba % 5 == 0:
    print('liczba podzielna przez 3 i 5')
elif liczba % 3 == 0 or liczba % 5 == 0:
    print('liczba podzielna przez 3 lub 5')
