import sys
sys.setrecursionlimit(10**6)

def solution(n):
    """
    피보나치 수는 F(0) = 0, F(1) = 1일 때,
    1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
    """
    pibo_list = list()

    def F(i):
        if i == 0:
            return 0
        elif i == 1:
            return 1
        else:
            try:
                return pibo_list[i]
            except:
                return F(i-1) + F(i-2)

    for i in range(n+1):
        pibo_list.append(F(i))

    F(n)

    return pibo_list[n] % 1234567