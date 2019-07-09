from random import *


def d(dice):
    if dice == 4:
        print(randint(1, 4))
    if dice == 6:
        print(randint(1, 6))
    if dice == 8:
        print(randint(1, 8))
    if dice == 10:
        print(randint(1, 10))
    if dice == 12:
        print(randint(1, 10))
    if dice == 20:
        print(randint(1, 12))
    elif dice == 100:
        items = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        x = sample(items, 1)
        print(x[0])
