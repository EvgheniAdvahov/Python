my_array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
n = int(input('введите минимум диапазона: '))
m = int(input('введите максимум диапазона: '))

for i in range(len(my_array)):
    if n <= my_array[i] <= m:
        print(i, end=" ")
