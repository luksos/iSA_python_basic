"""
Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej.
"""

def instructions():
    instruction = """
    Program bierze podaną przez użytkownika kwotę - w złotówkach, z dokładnością do 10 groszy, np. 10.30 -
    i przelicza ją na konkretne monety, tak aby było ich jak najmniej.  
    """
    print(instruction)

def money_input():
    money = 0
    while money == 0:
        try:
            money = float(input("Podaj kwotę: "))
        except ValueError:
            money = 0
        if money <= 0:
            money = 0
        elif len(str(money).split('.')[1]) >= 3:
            print("Heeeeeloooooooooooooł... najmniejsza jednostka walutowa to 1 grosz! Nie przesadzasz z dokładnością?")
            money = 0
        else:
            pass
    money = round(money,1)
    return money

def coins_calc(money):
    coins = []
    for i in (5, 2, 1, 0.5, 0.2, 0.1):
        coin_number = money // i
        money = money % i
        coins.append(coin_number)
    return coins

def coins_print(coins, money):
    print("\nW kwocie %.2f zł:" % money)
    print("\tmonet 5 zł jest:\t%i" % coins[0])
    print("\tmonet 2 zł jest:\t%i" % coins[1])
    print("\tmonet 1 zł jest:\t%i" % coins[2])
    print("\tmonet 50 gr jest:\t%i" % coins[3])
    print("\tmonet 20 gr jest:\t%i" % coins[4])
    print("\tmonet 10 gr jest:\t%i" % coins[5])


def main():
    instructions()
    money = money_input()
    coins = coins_calc(money)
    coins_print(coins, money)

main()
