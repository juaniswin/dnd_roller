from random import *

print("Press d on the keyboard then fill in for (x); x = 4, 6, 8, 10, 12, 20, or 100")


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
    if dice == 100:
        items = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        x = sample(items, 1)
        print(x[0])
