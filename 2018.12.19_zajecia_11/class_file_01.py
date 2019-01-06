"""
OOP - Object Oriented Programming
"""


class Krzeslo(object):
    def __init__(self, nazwa='Wing', material='sklejka', kolor='jasny', cena_netto=20, marza=10):
        self.ilosc_nog = 4
        self.ilosc_podlokietnikow = 0
        self.oparcie = True
        self.wymiary = (80,40,40)
        self.producent = 'Bodzio'

        self.nazwa = nazwa
        self.material = material
        self.kolor = kolor
        self.cena_netto = cena_netto

        self.marza = marza
        self.cena_do_sprzedazy = None

    def __str__(self):
        # graficzna reprezentacja naszego obiektu
        return 'Jestem {} za {} i mam {} nogi.'.format(self.nazwa, self.cena_brutto(), self.ilosc_nog)

    def __add__(self, other):
        suma_nog = self.ilosc_nog + other.ilosc_nog
        return 'Suma nóg wszystkich krzeseł: {}'.format(suma_nog)

    def __lt__(self, other):
        if self.marza < other.marza:
            return '{} ma mniejszą marżę od {}'.format(self.nazwa, other.nazwa)
        elif other.marza < self.marza:
            return '{} ma mniejszą marżę od {}'.format(other.nazwa, self.nazwa)

    def __len__(self):
        return self.ilosc_nog

    def cena_sprzedazy(self):
        self.cena_do_sprzedazy = self.cena_netto * (1 + self.marza/100)
        return self.cena_do_sprzedazy

    def cena_brutto(self):
        return self.cena_sprzedazy() * 1.23

    def cena_brutto_euro(self):
        return self.cena_sprzedazy() * 4.30


print()
obiekt_1 = Krzeslo()
print(obiekt_1)
print('nazwa modelu:\t\t\t', obiekt_1.nazwa)
# print(obiekt_1.material)
# print(obiekt_1.kolor)
print('cena sprzedaży (PLN):\t', obiekt_1.cena_sprzedazy())
print('cena brutto (PLN):\t\t', obiekt_1.cena_brutto())
print('cena brutto (EUR):\t\t', obiekt_1.cena_brutto_euro())

print()
obiekt_2 = Krzeslo('Wing Lux', 'drewno', 'ciemny', 1500, 50)
print(obiekt_2)
print('nazwa modelu:\t\t\t', obiekt_2.nazwa)
# print(obiekt_2.material)
# print(obiekt_2.kolor)
print('cena sprzedaży (PLN):\t', obiekt_2.cena_sprzedazy())
print('cena brutto (PLN):\t\t', obiekt_2.cena_brutto())
print('cena brutto (EUR):\t\t', obiekt_2.cena_brutto_euro())


# wykorzystanie funkcji __add__
print()
print(obiekt_1 + obiekt_2)

# wykorzystanie funkci __lt__
print()
print(obiekt_1 < obiekt_2)
print(obiekt_1 > obiekt_2)

print()
# wykorzystanie funkcji __len__
print('Ilość nóg krzesła {}:'.format(obiekt_1.nazwa), len(obiekt_1))
print('Ilość nóg krzesła {}:'.format(obiekt_2.nazwa), len(obiekt_2))