months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

while True:
    date_string = input("date: ")
    try:
        month, day, year = map(int, date_string.split('/'))
        if (month >= 1 and month <= 12 and day >= 1 and day <= 31):
            break
    except:
        try:
            old_month, old_day, old_year = map(int, date_string.split(" "))
            for ind in range(len(months)):
                if old_month == months[ind]:
                    month = ind + 1
            day = old_day.replace(",", "")
            if (int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31):
                break

        except:
            print()
            pass
    continue

print(f'{year}-{int(month):02}-{int(day):02}')