def transpose_matrix(m):
    row = len(m)
    col = len(m[0])
    matrix = [[0 for row in range(row)] for col in range(col)]

    for i in range(row):
        for j in range(col):
            matrix[j][i] = m[i][j]

    return matrix

def solution(scores):
    scores = transpose_matrix(scores)
    answer = ''

    for i in range(len(scores)):
        cpy_l = scores[i].copy()

        if cpy_l[i] == max(cpy_l) or cpy_l[i] == min(cpy_l):
            max_or_min = cpy_l[i]
            cpy_l.remove(cpy_l[i])

            if max_or_min in cpy_l:
                cpy_l.append(max_or_min)
                score = sum(cpy_l) / len(cpy_l)
            else:
                score = sum(cpy_l) / len(cpy_l)
        else:
            score = sum(cpy_l) / len(cpy_l)

        if score >= 90:
            answer += 'A'

        elif score < 90 and score >= 80:
            answer += 'B'

        elif score < 80 and score >= 70:
            answer += 'C'

        elif score < 70 and score >= 50:
            answer += 'D'

        elif score < 50:
            answer += 'F'

    return answer