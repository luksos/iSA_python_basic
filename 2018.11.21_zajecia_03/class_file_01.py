
zmienna = r"To jest jakiś \ntekst"
print(zmienna)

zmienna = 'To jest jakiś: "tekst"'
print(zmienna)

zmienna = "To jest jakiś: 'tekst'"
print(zmienna)

napis = "encyklopedia"
zmienna = f"To jest jakiś napis: {napis}"
print(zmienna)

napis = 23
zmienna = "To jest jakiś napis: " + str(napis)
print(zmienna)

zmienna = 12.3300
print("Zmienna %s" % zmienna)
print("Zmienna %f" % zmienna)
print("Zmienna %d" % zmienna)

print("To jest {} sposób na wprowadzenie {}".format(3, 'zmiennych'))
print("To jest {ilosc} sposób na wprowadzenie {nazwa}".format(ilosc=3, nazwa='zmiennych'))

# print("{}")
