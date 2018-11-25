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
    some_list = []
    print("\nStwórz listę podając jej kolejne elementy. Program ją wyświetli.\n"          
          "UWAGA: Aby zakończyć podawanie elementów, po prostu wprowadź pusty (naciśnij enter).\n")
    i = 1
    while True:
        item = input("Podaj %s. element listy: " % i)
        i += 1
        if item != '':
            some_list.append(item)
        else:
            break
    return some_list

def max_length(input_list):
    item_max_length = 0
    for i in input_list:
        item_length = len(i)
        if item_length > item_max_length:
            item_max_length = item_length
    return item_max_length

def item_length_format(items_list, item_max_length):
    index_number = 0
    for i in items_list:
        if len(i) >= 31:
            i = i[0:27]+'...'
        elif len(i) <= 30 and item_max_length >= 31:
            i = '{:<30}'.format(i)
        elif len(i) <= 30 and item_max_length <= 30:
            i = i.ljust(item_max_length)
        items_list[index_number] = i
        index_number += 1
    return items_list

def printout(item_max_length, list_length, items_list):
    top_bottom = '+' + ('-' * (item_max_length + 2) + '+') * list_length
    middle = ''
    for i in items_list:
        middle += "| " + i + " "
    middle += "|"
    print('\n'+top_bottom)
    print(middle)
    print(top_bottom)

def main():
    input_list = list_items_input()
    list_length = len(input_list)
    item_max_length = max_length(input_list)
    altered_list = item_length_format(input_list, item_max_length)
    printout(item_max_length, list_length, altered_list)

main()
