
# file = open("test.txt", "r+")
# print("CALY PLIK TEKSTOWY W FORMIE PIERWOTNEJ")
# print(file.read()+'\n')
# print("CZYTANIE PLIKU TEKSTOWEGO W FORMIE PIERWOTNEJ")
# file.seek(0)
# print(file.readline(), end='')
# file.seek(0)
# print(file.readline(), end='')
# file.seek(4)
# print(file.readline(), end='')
# print(file.readline(), end='')
# file.write('aaaaaa')
# file.seek(0)
# print("\nCALY PLIK TEKSTOWY PO DOPISANIU ZMIAN")
# print(file.read())
# file.close()


# # Coś tu jest nie tak... Pokombinować!!!!
# file = open("dane", "r+")
# file.write('AAAAAAA')
# file.seek(0)
# file.write('CCC')
# print(file.readlines())
# file.close()


# def open_file_count():
#     file = open("dane", "r+")
#     count = int(file.readline())
#     count += 1
#     print(count)
#     file.seek(0)
#     file.write(str(count))
#     file.close()
# open_file_count()


# with open("dane", "r+") as file:
#     count = int(file.readline())
#     count += 1
#     print(count)
#     file.seek(0)
#     file.write(str(count))


# with open("test.txt", "r+") as f:
#     # print(file.read().upper())
#     for line in f.readlines():
#         print(line, end='')


# program 'pamietniczek' :)
# pobieramy dane od uzytkownika (imie, wpis) i dodajemy do pamietniczka
def diary():
    name = input("Jakie jest Twoje imie: ")
    diary_input = input("Treść wpisu:\n")

    with open("diary", "a") as f:
        diary = f.write("{}:\n{}\n\n".format(name, diary_input))
    with open("diary", "r") as f:
        print(f.read())
diary()
