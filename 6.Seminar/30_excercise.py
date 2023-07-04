array = [0]
n = int(input('Введите кол-во элементов массива: '))
b = int(input('Введите разность элементов массива: '))
array[0] = int(input('Введите первый элемент массива: '))

for i in range(1, n):
    array.append(array[i - 1] + b)

print(array)
