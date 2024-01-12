def t(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return t(n - 2) + t(n - 1)

print(t(60))