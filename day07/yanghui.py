def main():
    row = int(input("row = "))
    yh = [[]] * row

    for i in range(row):
        yh[i] = [None] * (i + 1)
        for j in range(len(yh[i])):
            if j == 0 or j == i:
                yh[i][j] = 1;
            else:
                yh[i][j] = yh[i-1][j] + yh[i-1][j-1]
            print(yh[i][j], end='\t')
        print()


if __name__ == '__main__':
    main()
