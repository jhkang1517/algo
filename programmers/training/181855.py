# 문자열 묶기
def solution(strArr):
    dct = {}

    for s in strArr:
        dct[len(s)] = dct.get(len(s), 0) + 1

    return max(dct.values())