def sumi(a, b):
    if a == 0 and b == 0:
        return 0
    elif (a > 0):
        return 1 + sumi(a - 1, b)
    elif b > 0:
        return 1+ sumi(a, b-1)


print(sumi(7, 3))
