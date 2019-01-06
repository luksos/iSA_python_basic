"""
Przepisanie dziennika z zajęć 7-9 na wersję obiektową.
Proponuje zrobić klasę "Dziennik" a w atrybutach np trzymać handler do otwartego pliku (plik_dz), wpisy.
Dzięki temu np gdy otworzymy plik w konstruktorze do będziemy mieli handler dostępny w każdej metodzie obiektu.
Funkcja zapytaj() niech będzie poza klasą i steruje programem czyli wywoływaniem odpowiednich metod z obiektu.
"""

import pickle
import smtplib
import pprint
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

plik_dziennika = 'dziennik.dz'

class Dziennik(object):
    def __init__(self):
        self.plik_dz = Dziennik.otworz_dziennik(self)

    def otworz_dziennik(self):
        """
        Funkcja która otwiera plik dzinnika i zwraca handler do pliku w trybie zapis/odczyt
        """
        dziennik = open(plik_dziennika, 'rb+')
        return dziennik

    def zamknij_dziennik(self):
        """
        Funkcja która zamyka plik dzinnika
        """
        self.plik_dz.close()

    def dodaj_wpis(self):
        """
        Funkcja, która pyta użytkownika o dane do nowego wpisu i dodaje go do aktualnej listy plików
        """
        data = input("Podaj datę: ")
        tresc = input("Podaj treść: ")
        nowy_wpis = {"data": data, "tresc": tresc}

        stare_wpisy = self.przeczytaj_plik()
        nowe_wpisy = stare_wpisy

        try:
            nowe_wpisy.append(nowy_wpis)
        except:
            print('Nie było żadnego wpisu. Dodaje pierwszy wpis :)')
            nowe_wpisy = []
            nowe_wpisy.append(nowy_wpis)

        self.plik_dz.seek(0)
        pickle.dump(nowe_wpisy, self.plik_dz)
        print("Wpis został dodany prawidłowo.")

    def wyswietl_menu(self):
        """
        Proste wyświtlanie
        """
        print("Mój dziennik v0.1 alpha\n"
              "1. Wyświetlanie\n"
              "2. Dodawanie\n"
              "3. Usuwanie\n"
              "4. Szukanie\n"
              "5. Wyjscie")

    def przeczytaj_plik(self):
        """
        Funckja która z otwartego pliku czyta dane i zwraca nam w naszym przypadku w postaci listy słowników
        czyli dokłądnie tak jak je zapisujemy (użycie picka)
        """
        try:
            dane = pickle.load(self.plik_dz)
            return dane
        except:
            print('Błąd')

    def usun_wpis(self):
        """
        Funckaj usuwa wpis z dziennika na podstawie numeru podanego przez użytkownika
        Dodatkowo po usunięciu wysyła mail informacyjnego
        """
        wpisy = self.przeczytaj_plik()
        ilosc_wpisow = len(wpisy)
        print("Ilość wpisów w dzienniczku to: {}".format(ilosc_wpisow))
        wpis_do_usuniecia = int(input("Proszę podaj wpis"))

        if wpis_do_usuniecia <= ilosc_wpisow and wpis_do_usuniecia > 0:
            indeks_do_usuniecia = wpis_do_usuniecia-1
            del(wpisy[indeks_do_usuniecia])
            self.plik_dz.seek(0)

            temat = "Ktoś usunął wpis"
            tresc = "Usunięto wpis o indeksie: {}".format(indeks_do_usuniecia)
            tresc = tresc + "\na dla użytkownika jest to wpis numer: {}".format(wpis_do_usuniecia)

            self.wyslij_mail(temat, tresc)
            pickle.dump(wpisy, self.plik_dz)
            print("Właśnie usunąłem wpis")
        else:
            print("Nie ma takiego wpisu")

    def wyslij_mail(self, temat, tresc):
        """
        Funkcaj która wysła maila o określonym temacie i treści do "isapy@o2.pl"
        """

        mail = MIMEMultipart()
        mail["Subject"] = temat
        mail["To"] = 'isapy@o2.pl'
        mail["From"] = 'isapy@int.pl'

        body = MIMEText(tresc)
        mail.attach(body)

        serwer = smtplib.SMTP('poczta.int.pl')
        serwer.login('isapy@int.pl', 'isapython;')
        serwer.send_message(mail)
        serwer.quit()

        print("Wysłano mail!")

    def wyszukaj(self):
        """
        Funkcja w otwartym dzienniku szuka wpisu zawierającego w tresc zadaną przez użytkownika fraze
        Wyświetla też podsumowanie wyszukiwania
        """
        wpisy = self.przeczytaj_plik()
        fraza = input("Podaj szukaną treść: ")

        znaleziono_cos = False
        ilosc_wynikow = 0
        for index, wpis in enumerate(wpisy):
            if fraza in wpis["tresc"]:
                znaleziono_cos = True
                ilosc_wynikow += 1
                print(wpis["tresc"])
                print('Na indeksie: {}'.format(index))

        if ilosc_wynikow == 0:
            print("W całym dzienniku nie ma takiej frazy")
        else:
            print("Ilość wpisów: {}".format(ilosc_wynikow))

        # if znaleziono_cos is False:
        #     print("W całym dzienniku nie ma takiej frazy")

def zapytaj():
    """
    Nasz pseudo "controler" do zarządzania flow w programie
    """
    decyzja = input("Co wybierasz?")
    if decyzja == "1":
        print("Oto twoje wpisy:")

        moj_dziennik.otworz_dziennik()
        wpisy = moj_dziennik.przeczytaj_plik()
        pprint.pprint(wpisy)
        moj_dziennik.zamknij_dziennik()
    if decyzja == "2":
        print("Dodawanie wpisu:")

        moj_dziennik.otworz_dziennik()
        moj_dziennik.dodaj_wpis()
        moj_dziennik.zamknij_dziennik()
    if decyzja == "3":
        print("Usuń wpis:")

        moj_dziennik.otworz_dziennik()
        moj_dziennik.usun_wpis()
        moj_dziennik.zamknij_dziennik()
    if decyzja == "4":
        print("Wyszukiwarka:")

        moj_dziennik.otworz_dziennik()
        moj_dziennik.wyszukaj()
        moj_dziennik.zamknij_dziennik()
    elif decyzja == "5":
        exit()

moj_dziennik = Dziennik()

while True:
    moj_dziennik.wyswietl_menu()
    zapytaj()
