"""
Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
    | (bok)
    - (góra/dół)
    + (wierzchołek)
"""

dimensions = []
draw_elements = ['|', '-', '+', ' ']

for i in range(2):
    if i == 0:
        which_dimension = 'wysokość'
    else:
        which_dimension = 'szerokość'
    dimension = 0
    while dimension == 0:
        try:
            dimension = int(input("Podaj %s prostokąta: " % which_dimension))
        except ValueError:
            dimension = 0
    dimensions.append(dimension)


print('\nRysunek prostokąta o wymiarach ' + str(dimensions[1]) + 'x' + str(dimensions[0]) + ' wygląda tak:\n')

for y in range(dimensions[0]):
    print('\t', end='')
    for x in range(dimensions[1]):
        if (x == 0 and y == 0) or (x == 0 and y == dimensions[0]-1):
            print(draw_elements[2], end='')
        elif (x == dimensions[1]-1 and y == 0) or (x == dimensions[1]-1 and y == dimensions[0]-1):
            print(draw_elements[2])
        elif y == 0 or y == dimensions[0]-1:
            print(draw_elements[1], end='')
        elif x == 0:
            print(draw_elements[0], end='')
        elif x == dimensions[1]-1:
            print(draw_elements[0])
        else:
            print(draw_elements[3], end='')
