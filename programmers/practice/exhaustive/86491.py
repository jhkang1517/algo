def solution(sizes):
    width = list()
    height = list()

    for s in sizes:
        if s[0] > s[1]:
            width.append(s[0])
            height.append(s[1])
        else:
            width.append(s[1])
            height.append(s[0])

    return max(width) * max(height)


if __name__ == '__main__':
    solution([[60, 50], [30, 70], [60, 30], [80, 40]])
