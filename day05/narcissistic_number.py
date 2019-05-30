for x in range(100, 1000):
    i = x // 100
    j = x % 100 // 10
    k = x % 10
    if x == i**3 + j**3 + k**3:
        print(x)
