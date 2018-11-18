"""
Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7
"""

number = 'wrong_input'
while number == 'wrong_input':
    try:
        number = int(input("\nPodaj dowolną liczbę całkowitą: "))
    except ValueError:
        number = 'wrong_input'

check_3 = number%3
check_5 = number%5
check_7 = number%7

check = [check_3, check_5, check_7]

print('')
if check == [0, 0, 0]:
    print("\t Podana przez Ciebie liczba jest podzielna jednocześnie przez 3, 5 i 7.")
else:
    print("\t Podana przez Ciebie liczba NIE jest podzielna jednocześnie przez 3, 5 i 7")
print("\t\t%i : 3 = %.2f" % (number, (number/3)))
print("\t\t%i : 5 = %.2f" % (number, (number/5)))
print("\t\t%i : 7 = %.2f" % (number, (number/7)))
