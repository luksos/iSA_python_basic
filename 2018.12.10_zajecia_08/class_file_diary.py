"""
Program dzienniczka z opcjami dodawania, usuwanie i wyświetlania wszystkich wpisów.
Dodatkowe funkcje to np wyszukiwanie po dacie lub treść.
Przeglądanie wpisów poprzez wybór "następny", "poprzedni"
"""

import pickle
import sys

diary_file = 'diary'
diary_list = []

def menu():
    options = """
    =========================
    OPCJE:
    1 - przeczytaj pamiętnik
    2 - dodaj wpis
    3 - usuń wpis
    4 - wyszukaj wpis
    5 - wyjdź z programu
    =========================
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
    try:
        with open(file, 'rb') as picklefile:
            picklefile.seek(0)
            data = pickle.load(picklefile)
            return data
    except FileNotFoundError or EOFError:
        create_empty_file(file)
        return read_diary(file)

def create_empty_file(file):
    with open(file, 'wb') as picklefile:
        new_list = []
        pickle.dump(new_list, picklefile)

def add_diary_entry(file):
    date = input("Podaj datę: ")
    body = input("Podaj treść: ")
    new_entry = {'date': date, 'body': body}
    try:
        old_entries = read_diary(diary_file)
    except FileNotFoundError:
        create_empty_file(file)
        old_entries = read_diary(diary_file)
    try:
        old_entries.append(new_entry)
        diary_list = old_entries
    # except AttributeError:
    except:
        old_entries = []
        old_entries.append(new_entry)
        diary_list = old_entries
    with open(file, 'rb+') as picklefile:
        picklefile.seek(0)
        pickle.dump(diary_list, picklefile)
    print('## Wpis dodany do pamiętnika ##')

def del_diary_entry(file):
    if read_diary(file) is not None:
        date = input("Podaj datę wpisu do usunięcia: ")
        old_entries = read_diary(file)
        entry_removing = False
        for index, entry in enumerate(old_entries):
            print(index, entry)
            if entry['date'] == date:
                entry_removing = True
                del(old_entries[index])
                # old_entries.remove(index)
                print('## Wpis usunięty z pamiętnika ##')
        new_entries = old_entries
        if entry_removing:
            with open(file, 'rb+') as picklefile:
                picklefile.seek(0)
                pickle.dump(new_entries, picklefile)
            send_mail(date)
        if not entry_removing:
            print('## Taki wpis nie istnieje w pamiętniku ##')
    else:
        print('W pamiętniku nie ma żadnych wpisów - brak zawartości do usunięcia.')

def search_diary_entry():
    pass

def send_mail(date):
    topic = 'Ktoś usunął wpis w pamiętniku.'
    body = 'Usunięto wpis z dnia {}.'.format(date)

    print('Wysłano mail z tematem:\n'+topic)
    print('Wysłano mail o treści:\n'+body)


def main():
    while True:
        choice = menu()
        if choice == 1:
            print("Oto Twoje wpisy:")
            diary = read_diary(diary_file)
            print(diary)
        elif choice == 2:
            add_diary_entry(diary_file)
        elif choice == 3:
            del_diary_entry(diary_file)
        elif choice == 4:
            search_diary_entry()
        elif choice == 5:
            print("Do zobaczenia...")
            sys.exit()

main()
