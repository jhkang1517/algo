def solution(lottos, win_nums):
    answer = []
    count = 0
    zero_count = lottos.count(0)
    correct = {6: 1,
               5: 2,
               4: 3,
               3: 4,
               2: 5,
               1: 6,
               0: 6}

    for i in lottos:
        if i in win_nums:
            count += 1

    answer.append(correct[zero_count+count])
    answer.append(correct[count])

    return answer