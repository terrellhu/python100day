def is_palindrome_number(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


x = int(input('输入数字：'))
if is_palindrome_number(x):
    print('is palindrome')
else:
    print('not palindrome')
