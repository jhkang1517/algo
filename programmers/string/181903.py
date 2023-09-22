def solution1(q, r, code):
    answer = ''

    for i, c in enumerate(code):

        if i % q == r:
            answer += c

    return answer


def solution2(q, r, code):
    return code[r::q]
