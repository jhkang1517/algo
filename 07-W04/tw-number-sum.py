def solution(numbers):
    answer = []

    for i in range(-1, (len(numbers)-1)):

        for j in range(i, (len(numbers)-1)):

            if j == i:
                continue

            answer.append(numbers[i]+numbers[j])

    return sorted(list(set(answer)))