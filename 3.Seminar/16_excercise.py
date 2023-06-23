import random

n = int(input("введите кол-во элементов в массиве "))
num = int(input("введтие число Х: "))
array = []
for i in range(n):
    array.append(random.randint(1, 9))

print(array)
print(array.count(num))
