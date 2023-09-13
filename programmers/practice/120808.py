import math


def solution(numer1, denom1, numer2, denom2):
    numer1 *= denom2
    numer2 *= denom1
    denom1 *= denom2

    a, b = numer1+numer2, denom1
    gcd = math.gcd(numer1+numer2, denom1)

    return [int(a/gcd), int(b/gcd)]


if __name__ == '__main__':
    a = solution(1, 2, 3, 4)
    print(a)
