from random import randint

n = int(input('Введите кол-во кустов: '))

array = []

for item in range(n):
    array.append(randint(1, 9))
print(array)

max = 0
for i in range(n):
    temp = array[i] + array[i - 1] + array[i - 2]
    if temp > max:
        max = temp
    else:
        temp = 0

print(max)
