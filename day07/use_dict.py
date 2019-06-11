def main():
    scores = {'张三': 95, '李四': 78, '王五':82}
    print(scores['张三'])

    for elem in scores:
        print('%s--->%d' % (elem,scores[elem]))

    scores['赵大'] = 65
    scores['诸葛亮'] = 99
    scores.update(冷面=67, 云中鹤=50)
    print(scores)

    if '武大' in scores:
        print(scores['武大'])
    print(scores.get('武大', 60))

    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('张三', 100))
    print(scores)

    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()
