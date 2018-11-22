"""
Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
    | (bok)
    - (góra/dół)
    + (wierzchołek)

Rozwiązanie zadania z zajec
"""

szerokosc = 10
wysokosc = 10

# version #1
print('+' + '-'*szerokosc + '+')
print(('|' + ' '*szerokosc + '|\n')*wysokosc, end='')
print('+' + '-'*szerokosc + '+')

print('')

# version #2
top_bottom = '+' + '-'*szerokosc + '+'
print(top_bottom + ('|' + ' '*szerokosc + '|\n')*wysokosc + top_bottom, end='')