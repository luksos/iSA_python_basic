"""
Kalkulator do wyliczania wieku psa.
Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
Np: 15 ludzkich lat to 73 psie lata
"""

def hello():
    print("""\
    ================================================================================
    \tWitaj w kalkulatorze do wyliczania wieku psa.
    \tNa podstawie podanego wieku człowieka wyliczę odpowiednik dla wieku psa!
    \tPrawda że super?! :)
    ================================================================================""")

def getting_input():
    human_age = 'wrong_input'
    print()
    while human_age == 'wrong_input':
        try:
            human_age = input("Podaj wiek człowieka: ")
            human_age = int(human_age)
        except ValueError:
            print("\tNależy podać wiek jako liczbę całkowitą...")
            human_age = 'wrong_input'
            continue
        if human_age <= 0:
            print("\tWiek człowieka musi być przynajmniej równy 1...")
            human_age = 'wrong_input'
            continue
        elif human_age >= 150:
            print("\tSerio? Znasz kogoś w tym wieku? C'mon...")
            human_age = 'wrong_input'
            continue
    return human_age

def dog_age_calc(human_age):
    early_years = 10.5
    late_years = 4
    dog_age = 0
    for year in range(human_age):
        if year <= 1:
            dog_age += early_years
        else:
            dog_age += late_years
    if human_age == 1:
        print("\n%i ludzki rok to odpowiednik %.1f psich lat.\n" % (human_age, dog_age))
    elif human_age <= 4:
        print("\n%i ludzkie lata to odpowiednik %i psich lat.\n" % (human_age, dog_age))
    elif human_age >= 5:
        print("\n%i ludzkich lat to odpowiednik %i psich lat.\n" % (human_age, dog_age))
    else:
        print("Whoops, coś nakiełbasiłem...")

def main():
    hello()
    exit_program = None
    while exit_program not in ('t', 'tak'):
        exit_program = None
        human_age = getting_input()
        dog_age_calc(human_age)
        while exit_program not in ('t', 'tak', 'n', 'nie'):
            exit_program = (input("Zakończyć program? (T/N): ")).lower()
    print(" Do zobaczenia ".center(29, ':').upper())

main()
