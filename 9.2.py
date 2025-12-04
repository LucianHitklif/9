line = 0
count = False
name = input("Введите имя ")

while name != 'Левон':
    if name == 'Александра':
        count = True
    elif count:
        line += 1
    name = input("Введите имя ")

print(line)