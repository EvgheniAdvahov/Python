def powi(a, b):
    if b <= 1:
        return a
    return a * powi(a, b - 1)

print(powi(3,3))