n = int(input('Введите длину шиколадки: '))
m = int(input('Введите ширину шиколадки: '))
k = int(input('Введите дольку шиколадки которую хотите отломить: '))

if (k % n == 0 or k % m == 0) and k < n * m:
    print('yes')
else:
    print('no')
