from math import sqrt

sum = int(input('Введите Сумму: '))
multipl = int(input('Введите Произведение: '))

D = sqrt(sum*sum - 4*multipl)
print(D)

x1 = (sum + D)/2
x2 = (sum -D)/2

print(x1,x2)


