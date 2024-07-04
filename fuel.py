while True:
    fuel = input("fraction: ")
    try:
        X, Y = fuel.split("/")
        int_x = int(X)
        int_y = int(Y)
        value = int_x / int_y
        if value <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass

val = value * 100
if val <= 1:
    print('E')
elif val >= 99:
    print('F')
else:
    print('{0:.0f}%'.format(val))


