def convert(word):
    first = True
    for ch in word:
        if first:
            res = ch.lower()
        elif ch.isupper():
            res += '_' + ch.lower()
        else:
            res += ch
        first = False
    return res


if __name__ == '__main__':
    word = input().strip()
    snake = convert(word)
    print(snake)