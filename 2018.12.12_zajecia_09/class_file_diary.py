"""
Program dzienniczka z opcjami dodawania, usuwanie i wyświetlania wszystkich wpisów.
Dodatkowe funkcje to np wyszukiwanie po dacie lub treść.
Przeglądanie wpisów poprzez wybór "następny", "poprzedni"

login: isapy@int.pl
haslo: isapython
smtp: poczta.int.pl
port: 465
zabezpieczenie: SSL
"""

import pickle
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
            # print('\nWpisy z pamiętnika:')
            # count = 1
            # for entry in data:
            #     print('\tWpis #{} z dnia {}:'.format(count, entry['date']))
            #     print('\t\t{}'.format(entry['body']))
            #     count += 1
            return data
    except FileNotFoundError or EOFError:
        create_empty_file(file)
        return read_diary(file)

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
    except AttributeError:
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
            if entry['date'] == date:
                entry_removing = True
                entry_body = entry['body']
                del(old_entries[index])
                print('## Wpis usunięty z pamiętnika ##')
        new_entries = old_entries
        if entry_removing:
            with open(file, 'rb+') as picklefile:
                picklefile.seek(0)
                pickle.dump(new_entries, picklefile)
            send_mail(date, entry_body)
        if not entry_removing:
            print('## Taki wpis nie istnieje w pamiętniku ##')
    else:
        print('W pamiętniku nie ma żadnych wpisów - brak zawartości do usunięcia.')

def search_diary_entry(file):
    """ szukamy wpisu po jego treści """
    if read_diary(file) is not None:
        searched_phrase = input("Podaj szukaną frazę: ")
        entries = read_diary(file)
        entries_number = len(entries)
        entry_found = False
        count = 0
        found_entries = []
        for index, entry in enumerate(entries):
            if searched_phrase in (entry['body']).lower():
                entry_found = True
                found_entries.append(entry['body'])
                count += 1
        if entry_found:
            print('Znaleziono wpisów: {} z {}:'.format(count, entries_number))
            for index, item in enumerate(found_entries):
                print('Wpis #{}: {}'.format(index+1, item))
        if not entry_found:
            print('## Nie znaleziono szukanej frazy w żadnym z {} wpisów ##'.format(entries_number))
    else:
        print('W pamiętniku nie ma żadnych wpisów - brak zawartości do przeszukania.')

def create_empty_file(file):
    with open(file, 'wb') as picklefile:
        new_list = []
        pickle.dump(new_list, picklefile)

def send_mail(date, entry_body):
    topic = 'Lukasz Sosnowski - ktoś usunął wpis w pamiętniku.'
    body = 'Usunięto wpis z dnia {}.'.format(date)
    body = body + '\nTreść wpisu:\n{}'.format(entry_body)

    mail = MIMEMultipart()
    mail['Subject'] = topic
    mail['To'] = 'isapy@o2.pl'
    mail['From'] = 'isapy@int.pl'

    content = MIMEText(body)
    mail.attach(content)

    server = smtplib.SMTP('poczta.int.pl')
    server.login('isapy@int.pl', 'isapython;')
    server.send_message(mail)
    server.quit()

    print('Wysłano mail z tematem:\n'+topic)
    print('Wysłano mail o treści:\n'+body)


def main():
    while True:
        choice = menu()
        if choice == 1:
            data = read_diary(diary_file)
            print('\nWpisy z pamiętnika:')
            count = 1
            for entry in data:
                print('\tWpis #{} z dnia {}:'.format(count, entry['date']))
                print('\t\t{}'.format(entry['body']))
                count += 1
        elif choice == 2:
            add_diary_entry(diary_file)
        elif choice == 3:
            del_diary_entry(diary_file)
        elif choice == 4:
            search_diary_entry(diary_file)
        elif choice == 5:
            print("Do zobaczenia...")
            sys.exit()

main()
