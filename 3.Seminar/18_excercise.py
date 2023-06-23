import random

n = int(input("введите кол-во элементов в массиве "))
array = []
if n == 0:
    print('массив пустой: ')
else:
    num = int(input("введтие число Х: "))
    for i in range(n):
        array.append(random.randint(0, 9))

if num > max(array):
    print(max(array))
elif num < min(array):
    print(min(array))
else:
    for i in range(max(array) + 1):
        if (num - i) in array:
            print("Ближайшее число: ", num - i)
            print(array)
            break
        elif (num + i) in array:
            print("Ближайшее число: ", num + i)
            print(array)
            break
print("True array: ", array)
