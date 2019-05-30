col = int(input('请输入行数：'))
for i in range(1, col+1):
    for j in range(1, i+1):
        print('*', end='')
    print()

for i in range(col):
    for j in range(col):
        if j < col - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(col):
    for _ in range(col-i-1):
        print(' ', end='')
    for _ in range(i*2+1):
        print('*', end='')
    print()
