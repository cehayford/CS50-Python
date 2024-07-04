def main():
    inter = input("which time? ")
    time = convert(inter)
    if time >=7 and time<=8:
        print("breakfast time")
    if time >=12 and time<=13:
        print("lunch time")
    if time >=18 and time<=19:
        print("dinner time")


def convert(time):
    hour, mins = time.split(':')
    new_mins = float(mins) /60
    new_hour = float(hour) + new_mins
    return new_hour


if __name__ == "__main__":
    main()