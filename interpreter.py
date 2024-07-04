
inp = input("Which expression? ")
x, y, z = inp.split(" ")

x_data, z_data = float(x), float(z)

if y == "+":
    data = x_data + z_data
elif y == "-":
    data = x_data - z_data
if y == "*":
    data = x_data * z_data
elif y == "/":
    data = x_data / z_data

print(round(data, 1))
