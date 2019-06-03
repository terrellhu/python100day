def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)


x1 = int(input('x = '))
y1 = int(input('y = '))
print('gcd=%d' % gcd(x1, y1))
print('lcm=%d' % lcm(x1, y1))

