"""
OOP:
- pola klasy
- metody klas
- metody statyczne
- (pseudo)prywatność
- properties (właściwości): getter, setter, deleter; robimy tylko dla prywatnych
"""

class Telefon(object):

    vat = 1.23
    marza = 1.2
    __system = 'Android'
    system = 'Blabla'

    def __init__(self, producent, nazwa, system, cale, cena):
        self.producent = producent
        self.nazwa = nazwa
        if system is None:
            system = __class__.__system
        self.system = system
        self.cale = cale
        # if self.sprawdz_cene(cena) is False:
        if __class__.sprawdz_cene(cena) is False:
            cena = 99999
        self.__cena = cena

    # getter
    @property
    def cena(self):
        return '{} zł'.format(self.__cena * __class__.marza * __class__.vat)

    # setter
    @cena.setter
    def cena(self, wartosc):
        self.__cena = wartosc

    # deleter
    @cena.deleter
    def cena(self):
        self.__cena = 0

    def cena_brutto(self):
        return self.__cena * __class__.vat

    @staticmethod
    def sprawdz_cene(cena):
        if cena <= 0:
            return False
        return True

    @classmethod
    def SamsungS10(cls):
        return cls('Samsung', 'S10', 'Android 7.0', 6, 3000)

    @classmethod
    def SamsungS4(cls):
        return cls('Samsung', 'S4', None, 4, 0)

tel_1 = Telefon(producent='Apple', nazwa='iPhone', system='OSx10', cale=5.5, cena=2000)
tel_2 = Telefon.SamsungS10()
tel_3 = Telefon.SamsungS4()

print(tel_1.producent, tel_1.nazwa, tel_1.cena)
print(tel_2.producent, tel_2.nazwa, tel_2.cena_brutto())
print(tel_3.producent, tel_3.nazwa, tel_3.cena_brutto(), tel_3.system)

print(Telefon.marza)
print(Telefon._Telefon__system)   # odwołanie do prywatnej metody
print(Telefon.system)
print(tel_1.__dict__)

print('\nProperties:')
print(tel_2.cena)
tel_2.cena = 120   # bez settera nie można przypisać nowej ceny!
print(tel_2.cena)
del tel_2.cena
print(tel_2.cena)