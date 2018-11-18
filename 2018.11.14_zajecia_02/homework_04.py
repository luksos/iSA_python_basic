"""
Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
"""

def number_input():
    number = 'wrong_input'
    while number == 'wrong_input':
        try:
            number = input("Podaj dowolną liczbę: ")
            if '.' in number:
                number = float(number)
            else:
                number = int(number)
        except ValueError:
            number = 'wrong_input'
    return number

def first_last_digit(number):
    number = str(number)
    first_digit = number[0]
    last_digit = number[-1]
    print("\n\tPierwsza cyfra podanej liczby, to: " + first_digit)
    print("\tOstatnia cyfra podanej liczby, to: " + last_digit)

def main():

    number = number_input()
    first_last_digit(number)

main()
