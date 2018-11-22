"""
Program rysujący piramidę o określonej wysokości, np dla 3:
      #
     ###
    #####
"""

def instructions():
    print("""
    Witaj w programie rysującym fantastico piramidki!
    Zostań nowym faraonem już dziś...
    """)

def height_input():
    height = 0
    while height == 0:
        try:
            height = int(input("Podaj wysokość piramidy: "))
        except ValueError:
            height = 0
            continue
        if height <= 0:
            height = 0
            continue
        elif height >= 101:
            print("Hej, nie przesadzasz? Gdzie ja Ci tą choinkę wydrukuję?")
            continue
    return height

def draw_pyramid(pyramid_height):
    print()
    for i in range(pyramid_height):
        row = "#" + "#" * i * 2
        print(row.center(pyramid_height*2+1))

def main():
    instructions()
    height = height_input()
    draw_pyramid(height)
    if height <= 2:
        print("\nHmmm... Ale kurduplasta ta piramidka...")
        decision = (input("Nie chcesz spróbować zbudować większej? (T/N): ")).lower()
        if decision in ('t', 'tak'):
            height = height_input()
            draw_pyramid(height)
        else:
            print("\nDo zobaczenia")

main()
