name = ''
while name == '':
    name = input("Hej, jak masz na imię?: ")
# name = name.strip(' ')
name = name.replace(' ', '')
name_length = len(name)
# last_character = name[name_length-1]
last_character = name[-1]

# print("\nSuper, cześć " + name + "! Jak się masz?")
print("\nSuper, cześć %s! Jak się masz?" % name.capitalize())

print("Twoje imię ma %i znaków." % name_length)
print("Twoja ostatnia litera imienia to: " + last_character)

if last_character == 'a':
    if name.lower() == 'kuba':
        print("Wiem, że jesteś mężczyzną.")
    else:
        print("Wiem, że jesteś kobietą! :)")
else:
    print("Wiem, że jesteś mężczyzną.")
