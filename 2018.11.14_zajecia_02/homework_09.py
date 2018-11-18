"""
Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7
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

check = {'3':check_3, '5':check_5, '7':check_7}

print('')
for i in check:
    rest = check.get(i)
    if rest == 0:
        print("\t Podana przez Ciebie liczba jest podzielna przez %s." % i)
    else:
        print("\t Podana przez Ciebie liczba NIE jest podzielna przez %s." % i)
