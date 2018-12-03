"""
CSV - coma separated values
"""

import csv

with open('adresy.csv', 'r+', newline='') as csvfle:
    # for line in csvfle.readlines():
    #     print(line)
    reader = csv.reader(csvfle)
    for row in reader:
        print(row)

    # writer = csv.writer(csvfle)
    # writer.writerow(['Jan', 'Kowalski', 'Sopot, Gdansk', '123-432-111'])
