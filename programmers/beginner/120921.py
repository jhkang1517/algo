def solution(A, B):
    a = list(A)
    count = 0

    for _ in range(len(A)):
        if ''.join(a) == B:
            return count

        a.insert(0, a.pop())
        count += 1

    return -1
