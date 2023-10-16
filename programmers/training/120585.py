# 머쓱이보다 키 큰 사람
# 기존
def solution1(array, height):
    answer = 0

    for a in array:
        if a > height:
            answer += 1

    return answer


# 개선
# list comprehension을 사용할 때 변수에 사용하지 않는 경우에는 굳이 [ ] 로 감싸지 않아도 사용이 가능하다.
def solution2(array, height):
    return sum(1 for a in array if a > height)
