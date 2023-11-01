# 크기가 작은 부분 문자열
def solution(t, p):
    return sum(1 for i in range(len(t) - len(p) + 1) if int(t[i:i + len(p)]) <= int(p))
