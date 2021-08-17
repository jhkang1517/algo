def solution(n):
    answer = 0
    start_num = 1
    target_num = 0
    add_num = 0

    while True:
        if start_num >= n:
            break

        elif target_num < n:
            add_num += 1
            target_num += add_num

        elif target_num == n:
            answer += 1
            start_num += 1
            target_num = 0
            add_num = start_num

        else:
            start_num += 1
            target_num = 0
            add_num = start_num

    return answer