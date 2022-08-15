import itertools

def make_integer(something):
    a = int(''.join(something))

    return a


def sosu(n):

    if n < 2:
        return False

    for i in range(2, n // 2 + 1):

        if n % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    answer_list = list()

    for i in range(1, len(numbers)+1):
        answer_list.extend(list(map(make_integer, itertools.permutations(numbers, i))))

    for i in set(answer_list):

        if sosu(i) == True:
            answer += 1

    return answer