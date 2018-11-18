"""
Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
"""

import time

def cels_temp():
    temp_c = 'wrong_input'
    while temp_c == 'wrong_input':
        try:
            temp_c = round(float(input("Podaj temperaturę w stopniach Celsjusza: ")), 2)
        except ValueError:
            temp_c = 'wrong_input'
    return temp_c

def fahr_temp(temp_c):
    time.sleep(1)
    print("\nSuper, podałeś wartość %.2f'C. Zaraz to przeliczymy na Fahrenheity." % temp_c)
    time.sleep(2)
    print("\tWzór jest bardzo prosty: F = 1.8C+32")
    time.sleep(2)
    print("\tPrzeliczmy to razem...")
    time.sleep(2)
    print("\tF = 1.8*%.2f+32" % temp_c, end='')
    time.sleep(1)
    calc = round(1.8*temp_c, 2)
    print(" = %.2f+32" % calc, end='')
    time.sleep(1)
    calc = round(calc+32, 2)
    print(" = %.2f" % calc)
    time.sleep(1)
    print("\n%.2f'C = %.2fF" %(temp_c, calc))

def main():
    print("\nProgram do przeliczania stopni Celsjusza na Fahrenheita\n")
    temp_c = cels_temp()
    fahr_temp(temp_c)

main()
