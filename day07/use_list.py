def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
    print(len(list1), len(list2))
    print(list1[0])
    print(list1[-1])
    print(list1[-3])
    list1[2] = 300
    print(list1)

    list1.append(200)
    list1.insert(1, 400)
    list1 += [1000, 2000, 3]
    print(list1)

    list1.remove(3)
    list1.remove(3)
    if 1234 in list1:
        list1.remove(1234)
    del list1[0]
    print(list1)

    list1.clear()
    print(list1)


if __name__ == '__main__':
    main()
