

# def wyswietl_napis(napis, koniec='.'):
#     print(napis+koniec)
#
# wyswietl_napis('ala')
# wyswietl_napis('ala', '!')
# zmienna_na_koniec = '!'*20
# wyswietl_napis('ala', zmienna_na_koniec)


def policz_litery(litera, napis):
    ilosc_liter = napis.lower().count(litera)
    print('\nW napisie "{}" litera "{}" występuje {} raz(y)'.format(napis, litera, ilosc_liter))

policz_litery('a', 'Ala ma kota')


def policz_litery_2(litera, napis):
    """
    Funkcja która liczy ilość danego znaku w tekście i nie zwraca uwagi na wielkość danego znaku.
    :param litera: litera której szukamy w tekście [string]
    :param napis: tekst w którym szukamy porządanej litery [string]
    :return:
    """
    litera = litera.lower()
    napis = napis.lower()
    i = 0
    for litera_w_napisie in napis:
        if litera_w_napisie == litera:
            i += 1
    return i

print(policz_litery_2('a', 'ALA MA KOTA'))

print(print.__doc__)