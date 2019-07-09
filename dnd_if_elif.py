from random import *

def dice(die):
    if die == 4:
        print(randint(1, 4))
    if die == 6:
        print(randint(1, 6))
    if die == 8:
        print(randint(1, 8))
    if die == 10:
        print(randint(1, 10))
    if die == 12:
        print(randint(1, 10))
    if die == 20:
        print(randint(1, 12))
    if die == 100:
        items = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        x = sample(items, 1)
        print(x[0])