def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    n = int(input("n = "))
    for val in fib(n):
        print(val, end=' ')
    print()


if __name__ == '__main__':
    main()
