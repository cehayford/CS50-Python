amnt = 50

while amnt > 0:
    print("Amount Due:", amnt)
    coin = int(input('what coin? '))
    if coin== 25 or coin == 10 or coin ==5:
        amnt -= coin

owed = abs(amnt)
print("Change Owed: {0}".format(owed))
