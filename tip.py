def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # split_data = d.split()
    # split_data.pop(0)
    # join_data = ''.join(split_data)
    # return float(join_data)
    cleaned_data = ''.join(char for char in d if char.isdigit() or char == '.')
    f = float(cleaned_data)
    return f * 0.01

def percent_to_float(p):
    # split_data = p.split()
    # split.pop(0)
    # join_data = ''.join(split_data)
    # return float(join_data)
    cleaned_data = ''.join(char for char in p if char.isdigit() or char == '.')
    return float(cleaned_data)

main()