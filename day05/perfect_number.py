max = int(input("最大范围："))

for x in range(2, max+1):
    sum = 0
    for y in range(1, x):
        if x % y == 0:
            sum += y
    if sum == x:
        print(x)
