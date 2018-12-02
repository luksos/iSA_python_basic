

slownik = {
    "imie": ["Ala", "Jan", "Ania"],
    "nazwisko": ["Kowalska", "Malinowska", "Zubilewicz"]
}

miasta = {"miasto": ["Warszawa", "Gdańsk", "Sopot", "Kraków"]}


# print('\n', type(slownik))
# print(slownik, '\n')
#
# print(slownik.keys())
# print(slownik.values())
# print(slownik.items(), '\n')

# for key, item in slownik.items():
#     print(key + ':')
#     for x in item:
#         print('\t-> ' + x)
#
# nazwiska = slownik["nazwisko"]
# for i in nazwiska:
#     print(i)

# moja słaba wersja
# slownik.update(miasta)
# for i in range(3):
#     print("Mam na imie {} {} i mieszkam w {}.".format(slownik["imie"][i], slownik["nazwisko"][i], slownik["miasto"][i]))

def wyswietl_slownik():
    for indeks, imie in enumerate(slownik["imie"]):
        nazwisko = slownik["nazwisko"][indeks]
        miasto = miasta["miasto"][indeks]
        print("Mam na imie {} {} i mieszkam w {}.".format(imie, nazwisko, miasto))

wyswietl_slownik()