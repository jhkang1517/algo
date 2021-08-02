def solution(left, right):
    answer = 0
    num_l = [i for i in range(left, right+1)]

    for num in num_l:

        if num == 1:
            answer -= 1
            continue
        div = 1
        div_cnt = 0

        while div <= num:

            if (num%div) == 0:
                div_cnt += 1
            else:
                pass
            div += 1

        if div_cnt == 1 or div_cnt%2 == 0:
            answer += num
        else:
            answer -= num

    return answer