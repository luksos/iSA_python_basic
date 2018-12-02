"""
Zadanie

1) Napisz program, który poda statystki dowolnego tekstu pobranego z pliku, wypisze takie dane jak: ilość użyć poszczególnych literek i cyfr, ilość wyrazów, zdań etc.
   Nie będzie możliwość wyboru tryb case sensitivity.
   Niech program tworzy też plik ze statystyką swojej pracy. Czyli np:
   "
   Ilość uruchomień programu:
   10
   Przeanalizowanych znaków:
   1223435991
   Znalezionych wyrazów:
   2399
   Znalezionych liczb:
   122
   Znalezionych małych liter:
   68923455
   etc
   "

   Oczywiście dopuszalna jest ułomność takiego programu.
   Dokładne policzenie ilość zdań nie jest trywialne ale może jakiś fajny algorytm uda się Wam wymyśleć.
   Rodzaje statystyk zostawiam waszej fantacji :)

    Przydatny generator: http://lipsum.pl/
"""

import string

letters = string.ascii_letters
letters_upper = string.ascii_uppercase
letters_lower = string.ascii_lowercase
digits = string.digits
punctuation = string.punctuation
whitespaces = string.whitespace
things_to_check = [letters, letters_upper, letters_lower, digits, punctuation, whitespaces]
results = []

print("\n*** ANALIZA TEKSTU ***")
print("Program służy do przeanalizowania tekstu źródłowego i podania pewnych statystyk.\n")

def setup():
    case_sensitive = None
    case_decision = None
    while case_decision not in ('t', 'tak', 'n', 'nie'):
        case_decision = (input("Czy program ma rozróżniać duże i małe litery? (T/N): ")).lower()
        if case_decision in ('t', 'tak'):
            case_sensitive = True
        elif case_decision in ('n', 'nie'):
            case_sensitive = False
        else:
            case_decision = None
    return case_sensitive

def text_read():
    file = open("homework_input.txt")
    full_text = file.read()
    file.close()
    return full_text

def statistics_simple(text, check, results):
    for i, thing_to_check in enumerate(check):
        whole_count = 0
        for character in thing_to_check:
            count = text.count(character)
            whole_count += count
        results.append(whole_count)
    return results

def statistics_words(text, results):
    words = text.split()
    words_count = len(words)
    results.append(words_count)
    return results

def statistics_sentences(text, results):
    sentences = text.split('. ')
    sentences_count = len(sentences)
    results.append(sentences_count)
    return results

def results_printout(results, case_sensitive):
    text_0 = "\nWYNIKI ANALIZY:" \
             "\n- znakow w sumie:\t\t\t\t{}".format(results[0]+results[3]+results[4]+results[5])
    text_1 = "\n- duzych liter:\t\t\t\t\t{}".format(results[1])+"\n- malych liter:\t\t\t\t\t{}".format(results[2])
    text_2 = "\n- liter:\t\t\t\t\t\t{}".format(results[0])
    text_3 = "\n- cyfr:\t\t\t\t\t\t\t{}".format(results[3])
    text_4 = "\n- znakow interpunkcyjnych:\t\t{}". format(results[4])
    text_5 = "\n- spacji i znakow specjalnych:\t{}". format(results[5])
    text_6 = "\n- slow:\t\t\t\t\t\t\t{}".format(results[6])
    text_7 = "\n- zdan:\t\t\t\t\t\t\t{}".format(results[7])
    if case_sensitive:
        text = text_0 + text_1 + text_3 + text_4 + text_5 + text_6 + text_7
    elif not case_sensitive:
        text = text_0 + text_2 + text_3 + text_4 + text_5 + text_6 + text_7
    else:
        text = 'Oops, something went wrong...'
    print(text)
    file = open('homework_output.txt', 'w')
    file.write(text)
    file.close()


case_sensitive = setup()
full_text = text_read()
results = statistics_simple(full_text, things_to_check, results)
results = statistics_words(full_text, results)
results = statistics_sentences(full_text, results)
results_printout(results, case_sensitive)
