def solution(name, yearning, photo):
    answer = list()
    dct = dict(zip(name, yearning))

    for p in photo:
        cnt = 0
        for h in p:
            if h in dct:
                cnt += dct[h]
        answer.append(cnt)
    return answer