num = int(input('Введите 6ти занчное число: '))
num_str = str(num)

sum1 = 0
sum2 = 0

while len(num_str) > 0:
    sum1 = sum1 + int(num_str[-1])
    sum2 = sum2 + int(num_str[0])
    num_str = num_str[1:-1]

print(sum1)
print(sum2)
if sum1 == sum2:
    print('yes')
else:
    print('no')
