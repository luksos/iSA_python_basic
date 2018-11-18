"""
Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.
"""

binary_number = 0
while binary_number == 0:
    try:
        binary_number = input("Podaj dowolną liczbę w zapisie binarnym (tylko 6 znaków): ")
        int_test = int(binary_number)
        if len(binary_number) != 6:
            binary_number = 0
    except ValueError:
        binary_number = 0

decimal_number = 0
for i in range(6):
    calculation = int(binary_number[-(i+1)])
    calculation = calculation * 2 ** i
    decimal_number += calculation

print("\n\tLiczba w zapisie binarnym:\t\t%s" % binary_number)
print("\tLiczba w zapisie dziesiętnym:\t%i" % decimal_number)
print("\tSprawdzenie - przeliczenie powrotne za pomocą wbudowanej funkcji: " + str(bin(decimal_number)))
