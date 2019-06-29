def main():
    kw = input("ed2k or magnet:")
    with open('1.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            pos = line.find(kw)
            if pos >= 0:
                line = line[pos:]
                pos = line.find("\"")
                line = line[:pos]
                print(line)


if __name__ == '__main__':
    main()
