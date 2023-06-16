n = 777
sum = 0

while n > 0:
    sum = sum + n % 10
    n = round(n / 10)

print(sum)


