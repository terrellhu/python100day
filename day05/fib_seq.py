seq = int(input('输入序号：'))
f1 = 1
f2 = 1
print(1, end='\t')
print(1, end='\t')
for x in range(2, seq):
    f1 = f1 + f2
    f1, f2 = f2, f1
    print(f2, end='\t')
