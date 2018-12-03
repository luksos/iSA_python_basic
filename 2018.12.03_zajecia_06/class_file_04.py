"""
pickle
"""

import pickle

with open('adresy.pickle', 'rb+') as picklefile:
    dane = pickle.load(picklefile)
    print(dane)
    # lista = [1,2,3]
    # pickle.dump(lista, picklefile)