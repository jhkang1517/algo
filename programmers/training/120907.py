def solution1(quiz):
    answer = []

    for q in quiz:
        qs = q.split(' = ')
        a = eval(qs[0])
        b = int(qs[1])
        if a == b:
            answer.append('O')
        else:
            answer.append('X')

    return answer


# 수식이 올바른지에 대해서만 검증
def solution2(quiz):
    return ['O' if eval(q.replace(' = ', ' == ')) else 'X' for q in quiz]
