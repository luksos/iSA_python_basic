"""
OOP >>> dziedziczenie
"""

class Zwierze(object):
    def witaj(self):
        hello = "Grrrrrrrr..."
        return print(hello)

class Magister(object):
    def witaj(self):
        print('Cześć, jestem magistrem')

class Inzynier(object):
    def witaj(self):
        print('Trust me, I\'m an engineer!')

class Czlowiek(Zwierze, Magister, Inzynier):
    def __init__(self, ilosc_nog=2):
        self.ilosc_nog = ilosc_nog

    def witaj(self):
        hello = "Cześć"
        return print(hello)

class Kot(Zwierze):
    def __init__(self, ilosc_nog=4):
        self.ilosc_nog = ilosc_nog

class Pies(Zwierze):
    def __init__(self, ilosc_nog=4):
        self.ilosc_nog = ilosc_nog

class Student(Czlowiek):
    pass

class Bokser(Pies):
    def __init__(self, ):
        super(Bokser, self).__init__(ilosc_nog=666)
        self.nazwa = 'blabla'

class Jamnik(Pies):
    pass

zwierze = Zwierze()
# zwierze.witaj()
czlowiek = Czlowiek()
# czlowiek.witaj()
print('Ilość nóg człowieka:', czlowiek.ilosc_nog)
student = Student()
# student.witaj()
kot = Kot()
print('Ilość nóg kota:', kot.ilosc_nog)
pies = Pies()
print('Ilość nóg psa:', pies.ilosc_nog)
bokser = Bokser()
print('Ilość nóg psa boksera:', bokser.ilosc_nog)
jamnik = Jamnik()
print('Ilość nóg psa jamnika:', jamnik.ilosc_nog)

