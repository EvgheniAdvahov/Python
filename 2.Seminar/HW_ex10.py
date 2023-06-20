from random import randint

coins = int(input('Введите кол-во монеток '))
eagle = 0
mon = 0

for coin in range(coins):
    coin = randint(0,1)
    print((coin))
    if coin == 0: mon +=1
    else: eagle +=1

if mon == 0 or eagle == 0:
    print('не надо ничего переворачивать')
elif mon < eagle:
    print(mon)
else:
    print(eagle)


