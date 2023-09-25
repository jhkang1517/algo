def solution(numbers, k):
    answer = 0

    while numbers:
        n = numbers.pop(0)
        answer += 1

        if answer == k:
            return n

        numbers.append(n)
        numbers.append(numbers.pop(0))

    return answer


def solution1(numbers, k):
    # (k - 1) : 0부터 시작 하는 인덱스 사용을 위함
    # 2 * (k - 1) : 공을 던지는 사람의 인덱스 번호
    # % len(numbers) 배열의 길이 보다 큰 인덱스 발생시, 나머지 값으로 계산
    return numbers[2 * (k - 1) % len(numbers)]
