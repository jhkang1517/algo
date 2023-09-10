def solution(n, m, section):
    answer = 0
    painted = dict()

    while section:
        end = section.pop()

        if end in painted:
            continue
        else:
            answer += 1

        for x in range(m):
            painted[end - x] = True

    return answer
