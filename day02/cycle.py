import math

radius = float(input('输入圆的半径：'))
perimeter = radius * 2 * math.pi
area = math.pi * radius * radius
print('周长：%.1f 面积：%.1f' % (perimeter, area))