import random

answer = random.randint(1, 100)
counter = 0

while True:
    counter += 1
    number = int(input('number='))
    if number > answer:
        print('有点大')
    elif number < answer:
        print('有点小')
    else:
        print('success!')
        break

print('total count=%d' % counter)
