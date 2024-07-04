grocery_list = {}

while True:
    try:
        item = input().lower()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    except EOFError:
        sorted_items = sorted(grocery_list.keys())
        for item in sorted_items:
            count = grocery_list[item]
            print(f"{count} {item.upper()}")
        break



# return grocery_list

