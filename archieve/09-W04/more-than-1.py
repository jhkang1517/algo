def solution(a, b, c):
    if abs(a - b) == 1 and abs(a - c) == 1:
        return False

    if abs(b - a) == 1 and abs(b - c) == 1:
        return False

    if abs(c - a) == 1 and abs(c - b) == 1:
        return False

    else:
        return True