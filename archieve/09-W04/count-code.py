def solution(string):
    count = 0

    for i in [
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z'
    ]:
        code = ('co' + i + 'e')

        if code in string:
            count += string.count(code)

    return count
