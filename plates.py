def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum() or s.isalpha():
        for i in s:
            if i.isdigit():
                ind = s.index(i)
                if s[ind:].isdigit() and int(i) != 0:
                    return True
                else:
                    return False
    return False



main()