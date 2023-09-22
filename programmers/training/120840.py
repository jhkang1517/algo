def solution(balls, share):
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    return answer


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
