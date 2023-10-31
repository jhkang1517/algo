# 다음에 올 숫자
def solution(common):
    diff1 = common[0] - common[1]
    diff2 = common[1] - common[2]

    if diff1 == diff2:
        return common[-1] - diff1
    else:
        return common[-1] * (common[1] // common[0])
