def is_prime(num):
    if num < 4:
        return True
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


num = int(input("num = "))
if is_prime(num):
    print('is prime')
else:
    print('not prime')
