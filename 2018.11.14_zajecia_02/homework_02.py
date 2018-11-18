"""
Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
"""

import time

def fahr_temp():
    temp_f = 'wrong_input'
    while temp_f == 'wrong_input':
        try:
            temp_f = round(float(input("Podaj temperaturę w Fahrenheitach: ")), 2)
        except ValueError:
            temp_f = 'wrong_input'
    return temp_f

def cels_temp(temp_f):
    time.sleep(1)
    print("\nSuper, podałeś wartość %.2fF. Zaraz to przeliczymy na stopnie Celsjusza." % temp_f)
    time.sleep(2)
    print("\tWzór jest bardzo prosty: C = (F-32)/1.8")
    time.sleep(2)
    print("\tPrzeliczmy to razem...")
    time.sleep(2)
    print("\tC = (%.2f-32)/1.8" % temp_f, end='')
    time.sleep(1)
    calc = round(temp_f-32, 2)
    print(" = %.2f/1.8" % calc, end='')
    time.sleep(1)
    calc = round(calc/1.8, 2)
    print(" = %.2f" % calc)
    time.sleep(1)
    print("\n%.2fF = %.2f'C" %(temp_f, calc))

def main():
    print("\nProgram do przeliczania Fahrenheita na stopnie Celsjusza.\n")
    temp_f = fahr_temp()
    cels_temp(temp_f)

main()
