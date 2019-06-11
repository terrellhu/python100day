def main():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('len=', len(set1))

    set2 = set(range(1, 10))
    print(set2)

    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    print(set1)
    print(set2)

    set2.discard(5)
    if 4 in set2:
        set2.remove(4)
    print(set2)

    for elem in set2:
        print(elem ** 2, end=' ')
    print()

    set3 = set((1, 2, 3, 4, 2, 1))
    print(set3.pop())
    print(set3)

    print('-----------------------')
    print(set1)
    print(set2)
    print(set1 & set2)
    print(set1 | set2)
    print(set1 - set2)
    print(set1 ^ set2)

    print(set2 <= set1)


if __name__ == '__main__':
    main()
