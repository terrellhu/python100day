from math import sqrt

num = int(input("输入一个数："))
if num == 1:
    print("这不是一个素数")

end = int(sqrt(num))
is_prime = True;
for x in range(3, end + 1):
    if num % x == 0:
        is_prime = False
        break

if is_prime:
    print('这是一个素数')
else:
    print('这不是一个素数')