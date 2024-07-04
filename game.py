import random

while True:
    try:
        inp = int(input("Level: "))
        if inp > 0:
            break
    except:
        pass

generate = random.randint(1, inp)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < generate:
                print("Too small!")
            elif guess > generate:
                print("Too large!")
            else:
                print("Just right!")
                break
    except:
        pass