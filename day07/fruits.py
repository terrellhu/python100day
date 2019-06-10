def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    for fruit in fruits:
        print(fruit.title(), end=' ')
    print()
    fruit2 = fruits[1:4]
    print(fruit2)

    fruit3 = fruits[:]
    print(fruit3)

    fruit4 = fruits[-3:-1]
    print(fruit4)

    fruit5 = fruits[::-1]
    print(fruit5)


if __name__ == '__main__':
    main()
