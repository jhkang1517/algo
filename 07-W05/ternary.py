def solution(n):
    answer = ''
    sum = 0

    while True:

        # 2021.07.26 비효율적...
        if n == 1:
            return 1

        elif n == 2:
            return 2

        rmn = n % 3
        answer += str(rmn)
        n = n // 3

        if n < 3:
            answer += str(n)
            break

    for i in range((len(answer)-1),-1,-1):
        sum += ((3 ** i) * int(answer[::-1][i]))

    return sum