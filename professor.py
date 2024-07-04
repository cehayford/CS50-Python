import random


def main():
    level = get_level()
    score = game_sim(level)
    print('Score: ', score)
    # generate_integer(level)


def get_level():
    while True:
        try:
            level  = int(input('Level: '))
            if level in [1, 2, 3]:
                # print("level: ", level)
                break
        except:
            pass
    return level


def generate_integer(level):
    score = 0
    if level == 1:
        X = random.randint(0, 9)
        Y = random.randint(0, 9)
    elif level == 2:
        X = random.randint(10, 99)
        Y = random.randint(10, 99)
    else:
        X = random.randint(100, 999)
        Y = random.randint(100, 999)
    return X, Y

def round_sim(X, Y):
    trails = 1
    while trails <= 3:
        try:
            feed = X + Y
            answer = int(input('{0} + {1} = '.format(X, Y)))
            if answer == (X + Y):
                return True
            else:
                trails += 1
                print("EEE")
            print('{0} + {1} = {2}'.format(X, Y, feed))

        except:
            trails += 1
            print("EEE")

def game_sim(level):
    # for i in round_sim():
    #     pass
    count_round = 1
    score = 0
    while count_round <= 10:
        X, Y = generate_integer(level)
        response = round_sim(X, Y)
        if response == True:
            score += 1
        count_round += 1
    return score

if __name__ == "__main__":
    main()
