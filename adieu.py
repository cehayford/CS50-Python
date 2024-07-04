import inflect

name = []
p = inflect.engine()

while True:
    try:
        inp = input('Name: ')
        if inp == '':
            break
        else:
            name.append(inp)
    except EOFError:
        print()
        break


fetch = p.join(name)
print("Adieu, adieu, to " + fetch)