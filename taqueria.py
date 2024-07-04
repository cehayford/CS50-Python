d = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

# try:
#     item = input('Name of the fruit: ').lower()
# except EOFError:
#     pass
# while item != 0:
#     counter = 0
#     if item in d:
#         print(d[item])
#     item = input('Name of the fruit: ').lower()

total_cost = 0.00

try:
    while True:
        item = input('Name of the item: ').lower()
        if item == "":
            continue
        elif item in d:
            item_cost = d[item]
            total_cost += item_cost
            print(f"${total_cost:.2f}")
        else:
            print("Item not found.")
except EOFError:
    pass