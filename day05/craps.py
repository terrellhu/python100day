"""
Craps赌博游戏：
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜
其他情况游戏继续玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束。
"""
from random import randint
total = 1000

while total > 0:
    print('余额=%d' % total)
    bet = int(input('请下注：'))
    if bet > total:
        print('余额不足，重新下注，余额=%d' % total)
        continue
    x = randint(1, 6)
    y = randint(1, 6)
    first = x + y
    print('first=%d' % first)
    if 7 == first or 11 == first:
        total += bet
        continue
    elif 2 == first or 3 == first or 12 == first:
        total -= bet
        continue

    while True:
        x = randint(1, 6)
        y = randint(1, 6)
        print('continue=%d' % (x+y))
        if 7 == x + y:
            total -= bet
            break
        elif first == x + y:
            total += bet
            break
        else:
            continue
print('你输完了')
