"""
Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
   +------+------+------+
   | col1 | col2 | col3 |
   +------+------+------+
Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn :)
"""

def list_items_input():
    """
    Funkcja zwraca listę wprowadzoną przez użytkownika
    :return: [list]
    """
    some_list = []
    print("\nStwórz listę podając jej kolejne elementy. Program ją wyświetli.\n"
          "UWAGA #1: Element może być listą, jeśli jego elementy oddzielisz spacją.\n"
          "UWAGA #2: Aby zakończyć podawanie elementów, po prostu wprowadź pusty (naciśnij enter).\n")
    i = 1
    while True:
        item = input("Podaj %s. element listy: " % i)
        i += 1
        if item != '':
            some_list.append(item)
        else:
            break
    return some_list

def nested_list(input_list):
    """
    Funkcja sprawdza, czy użytkownik nie wprowadził w poszczególnych elementach listy danych odseparowanych spacją.
    W takim wypadku element ten jest przekształcany na listę, przez co otrzymujemy efekt zagnieżdżonych list.
    :param input_list: pierwotna lista wprowadzona przez użytkownika [list]
    :return: [list]
    """
    index_1 = 0
    rows = 1
    for x in input_list:
        if ' ' in x:
            x = x.split(' ')
            index_2 = 0
            for y in x:
                if y[-1] == ',':
                    y = y[0:-1]
                    x[index_2] = y
                index_2 += 1
            input_list[index_1] = x
            if index_2 >= rows:
                rows = index_2
        index_1 += 1

    return input_list, rows

def max_length(input_list):
    """
    Funkcja sprawdza i zwraca długość najdłuższego elementu listy, w tym elementów zawartych w zagnieżdżonych listach.
    :param input_list: lista użytkownika z ewentualnymi zagnieżdżonymi listami [list]
    :return: [int]
    """
    item_max_length = 0
    for i in input_list:
        if type(i) == str:
            item_length = len(i)
            if item_length > item_max_length:
                item_max_length = item_length
        elif type(i) == list:
            for x in i:
                item_length = len(x)
                if item_length > item_max_length:
                    item_max_length = item_length
    return item_max_length

def item_length_format(items_list, item_max_length):
    """
    Funkcja formatuje każdy element listy tak, aby był wyjustowany do lewej strony i odpowiedniej, jednakowej długości.
    :param items_list: [list]
    :param item_max_length: [int]
    :return: [list]
    """
    index_number_1 = 0
    for i in items_list:
        if type(i) == str:
            if len(i) >= 31:
                i = i[0:27]+'...'
            elif len(i) <= 30 and item_max_length >= 31:
                i = '{:<30}'.format(i)
            elif len(i) <= 30 and item_max_length <= 30:
                i = i + ' ' * (item_max_length-len(i))
            items_list[index_number_1] = i
        if type(i) == list:
            index_number_2 = 0
            for nested_item in i:
                if len(nested_item) >= 31:
                    nested_item = nested_item[0:27] + '...'
                elif len(nested_item) <= 30 and item_max_length >= 31:
                    nested_item = '{:<30}'.format(nested_item)
                elif len(nested_item) <= 30 and item_max_length <= 30:
                    nested_item = nested_item.ljust(item_max_length)
                i[index_number_2] = nested_item
                index_number_2 += 1
        index_number_1 += 1
    return items_list

def printout(item_max_length, list_length, items_list, rows):
    """
    Funkcja drukuje wprowadzoną przez użytkownika listę w odpowiedniej formie graficznej.
    :param item_max_length: [int]
    :param list_length: [int]
    :param items_list: [list]
    :param rows: [int]
    """
    top_bottom = '+' + ('-' * (item_max_length + 2) + '+') * list_length
    for y in range(rows):
        middle = ''
        for x in items_list:
            if type(x) == str:
                if y == 0:
                    middle += "| " + x + " "
                else:
                    middle += "| " + ' ' * item_max_length + " "
            elif type(x) == list:
                try:
                    middle += "| " + x[y] + " "
                except IndexError:
                    middle += "| " + ' ' * item_max_length + " "
        middle += "|"
        print(top_bottom)
        print(middle)
    print(top_bottom)

def main():
    input_list = list_items_input()
    input_list, max_rows = nested_list(input_list)
    list_length = len(input_list)
    item_max_length = max_length(input_list)
    altered_list = item_length_format(input_list, item_max_length)
    print(altered_list)
    print('Max rows: ', max_rows)
    printout(item_max_length, list_length, altered_list, max_rows)

main()
