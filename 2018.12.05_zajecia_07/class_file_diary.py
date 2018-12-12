"""
!!!!!!!!!! NOT FINISHED !!!!!!!!
"""
"""
Program dzienniczka z opcjami dodawania, usuwanie i wyświetlania wszystkich wpisów.
Dodatkowe funkcje to np wyszukiwanie po dacie lub treść.
Przeglądanie wpisów poprzez wybór "następny", "poprzedni"
"""

import pickle
import sys

diary_file = 'diary'

def menu():
    options = """OPCJE:
    1 - przeczytaj pamiętnik
    2 - dodaj wpis
    3 - usuń wpis
    4 - wyszukaj wpis
    5 - wyjdź z programu
    """
    print(options)
    choice = 0
    while choice not in (1, 2, 3, 4, 5):
        try:
            choice = int(input("Podaj co chcesz zrobić: "))
        except ValueError:
            choice = 0
    return choice

def read_diary(file):
    with open(file, 'rb') as picklefile:
        data = pickle.load(picklefile)
        return data

def add_diary_entry(file):
    date = input("Podaj datę: ")
    body = input("Podaj treść: ")
    new_entry = {'date': date, 'body': body}
    old_entries = read_diary(diary_file)
    diary_list = []
    diary_list.append(old_entries)
    diary_list.append(new_entry)
    with open(file, 'rb') as picklefile:
        picklefile.seek(0)
        pickle.dump(diary_list, picklefile)

def del_diary_entry(file):
    date = input("Podaj datę: ")
    data = read_diary(file)


def search_diary_entry():
    None

def main():
    choice = menu()
    if choice == 1:
        print("Oto Twoje wpisy:")
        diary = read_diary(diary_file)
        print(diary)
    elif choice == 2:
        add_diary_entry(diary_file)
    elif choice == 3:
        del_diary_entry()
    elif choice == 4:
        search_diary_entry()
    elif choice == 5:
        print("Do zobaczenia...")
        sys.exit()

main()
