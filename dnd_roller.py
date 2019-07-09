from random import *

print("~D4~")
print(randint(1, 4))
print("~D6~")
print(randint(1, 6))
print("~D8~")
print(randint(1, 8))
print("~D10~")
print(randint(1, 10))
print("~D12~")
print(randint(1, 12))
print("~D20~")
print(randint(1, 20))
print("~Hundreds Integer~")
items = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = sample(items, 1)
print(x[0])
