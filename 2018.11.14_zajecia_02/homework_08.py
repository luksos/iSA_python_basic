"""
Napisz program do rozpoznawania czy podane liczba jest parzysta czy nie.
"""

number = 'wrong_input'
while number == 'wrong_input':
    try:
        number = int(input("Podaj dowolną liczbę całkowitą: "))
    except ValueError:
        number = 'wrong_input'

check = number%2

if check == 0:
    print("\n\t Podana przez Ciebie liczba jest liczbą parzystą.")
else:
    print("\n\t Podana przez Ciebie liczba NIE jest liczbą parzystą.")
