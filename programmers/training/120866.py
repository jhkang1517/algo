# 안전지대
def solution(board):
    cnt = 0
    n = len(board[0])
    answer = [[0] * n for _ in range(n)]

    for i in range(len(board)):

        for j in range(len(board[i])):

            if board[i][j] == 1:

                for a in range(-1, 2):

                    for b in range(-1, 2):

                        if (i + a != -1) and (j + b != -1):
                            try:
                                answer[i + a][j + b] = 1
                            except:
                                pass

    for a in answer:
        cnt += a.count(0)

    return cnt