"""
Napisz program do sprawdzania czy podany rok jest rokiem przestępnym.
"""

year = 'wrong_input'
while year == 'wrong_input':
    try:
        year = int(input("\nPodaj dowolną liczbę całkowitą: "))
    except ValueError:
        year = 'wrong_input'

print('')
check_1 = year%4
check_2 = year%100
check_3 = year%400

if check_1 == 0 and check_2 != 0 or check_3 == 0:
    print("\t Podany przez Ciebie rok %i jest rokiem przestępnym." % year)
else:
    print("\t Podany przez Ciebie rok %i NIE jest rokiem przestępnym." % year)
