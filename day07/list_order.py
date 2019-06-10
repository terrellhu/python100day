def main():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    list3 = sorted(list1, reverse=True)
    list4 = sorted(list1, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)

    list1.sort(reverse=True)
    print(list1)


if __name__ == '__main__':
    main()
