def solution(s):
    answer = ' '
    answer_list = list()

    int_list = [int(x) for x in s.split(' ')]
    min_int = str(min(int_list))
    max_int = str(max(int_list))
    answer_list.append(min_int)
    answer_list.append(max_int)

    answer = answer.join(answer_list)

    return answer