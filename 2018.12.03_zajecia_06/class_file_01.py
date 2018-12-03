"""
powrót do globali i scopie zmiennych (przestrzeń nazw, zasięg)
scope globalny
"""

zmienna_globalna_1 = 'A'
zmienna_globalna_2 = 'B'

def rodzic():
    zmienna_lokalna = 'C'
    global zmienna_globalna_2
    zmienna_globalna_1 = 'A zmienione'
    zmienna_globalna_2 = 'B zmienione'
    print('Funkcja rodzic: ' + zmienna_globalna_1)
    print('Funkcja rodzic: ' + zmienna_globalna_2)
    # print(zmienna_lokalna)
    return zmienna_lokalna

print(zmienna_globalna_1)
print(zmienna_globalna_2)
rodzic()
print(zmienna_globalna_1)
print(zmienna_globalna_2)
zmienna_lokalna = rodzic()
print(zmienna_lokalna)