def solution(numbers):
    pos = sorted([x for x in numbers if x >= 0])
    neg = sorted([x for x in numbers if x < 0])

    maxp = 0
    maxn = 0

    if len(pos) > 1:
        maxp = pos[-2] * pos[-1]

    if len(neg) > 1:
        maxn = neg[-2] * neg[-1]

    if len(pos) == 1 and len(neg) == 1:
        return pos[0] * neg[0]

    return maxp if maxp > maxn else maxn


