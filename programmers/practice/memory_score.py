def solution(name, yearning, photo):
    answer = []
    dct = {n: yearning[idx] for idx, n in enumerate(name)}

    for p in photo:
        cnt = 0
        for h in p:
            try:
                cnt += dct[h]
            except KeyError:
                pass
        answer.append(cnt)
    return answer


if __name__ == '__main__':
    solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])