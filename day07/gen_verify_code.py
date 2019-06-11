from random import randint

def gen_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_pos = len(all_chars)
    code = ''

    for _ in range(code_len):
        index = randint(0, max_pos)
        code += all_chars[index]
    return code


def main():
    n = int(input('len='))
    print(gen_code(n))


if __name__ == '__main__':
    main()
