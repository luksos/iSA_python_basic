"""
Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
"""

import time
import math

pi = math.pi

def circle_radius():
    radius = 'wrong_input'
    while radius == 'wrong_input':
        try:
            radius = round(float(input("Podaj promień okręgu w [cm] (dokładność 1mm): ")), 1)
        except ValueError:
            radius = 'wrong_input'
    return radius

def circle_area(radius):
    time.sleep(1)
    print("\nSuper, podałeś promień r = %.1f [cm]. Zaraz wyliczymy na jego podstawie powierzchnię okręgu." % radius)
    time.sleep(2)
    print("\tWzór wygląda tak: P = pi*r^2")
    time.sleep(2)
    print("\tPrzeliczmy to...")
    time.sleep(2)
    print("\tP = %.2f*%.2f^2" % (pi, radius), end='')
    time.sleep(1)
    calc = round(pi*radius**2, 2)
    print(" = %.2f" % calc)
    time.sleep(1)
    print("\nP = %.2f [cm^2]" % calc)

def main():
    print("\nProgram do wyliczania pola okręgu o zadanym przez użytkownika promieniu.\n")
    radius = circle_radius()
    circle_area(radius)

main()
