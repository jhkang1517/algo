# 세 개의 구분자
def solution1(myStr):
    answer = []
    start = 0

    for i in range(len(myStr)):
        if myStr[i] in 'abc':
            answer.append(myStr[start:i])
            start = i + 1

    answer.append(myStr[start:])
    answer = [x for x in answer if x != '']

    return answer if answer else ['EMPTY']


def solution2(myStr):
    myStr = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split()
    return myStr if myStr else ['EMPTY']