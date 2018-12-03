"""
analogicznie jak w pracy domowej - sprawdzić ile jest poszczególnych liter w tekście i zapisać to do pickle'a
1. otwórz plik z danymi
2. przeiteruj każdy znak w danych wejściowych
3. porównaj znak do znaku bazowego
4. zwiększ licznik dla danego znaku
5. zapisz licznik do pickle
"""

import string
import pickle
import sys

letters = string.ascii_letters

def text_read():
    try:
        with open("class_file_05_input.txt") as file:
            full_text = file.read()
    except Exception as e:
        print('Oooops, probably file doesn\'t exists')
        print('Let\'s look at exception: \n{}'.format(e))
        print('\nProgram will stop now. Bye')
        sys.exit()
    return full_text

def letters_statistics(text):
    results = {}
    for letter in letters:
        count = 0
        count = text.count(letter)
        results[letter] = [count]
    return results

def results_output(result):
    with open('class_file_05_output', 'wb') as picklefile:
        pickle.dump(result, picklefile)

def results_from_pickle():
    with open('class_file_05_output', 'rb') as picklefile:
        data = pickle.load(picklefile)
        print('')
        for key, item in data.items():
            print(key, '-', item[0])

def main():
    full_text = text_read()
    results = letters_statistics(full_text)
    results_output(results)
    # print(results)
    results_from_pickle()

main()
