from random import *

print("~d4~")
print(randint(1, 4))
print("~d6~")
print(randint(1, 6))
print("~d8~")
print(randint(1, 8))
print("~d10~")
print(randint(1, 10))
print("~d12~")
print(randint(1, 12))
print("~d20~")
print(randint(1, 20))
print("~hundreds integer~")
items = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = sample(items, 1)
print(x[0])