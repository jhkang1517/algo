def solution(myString, pat):
    answer = ''
    occured = False

    for i in myString.partition(pat):
        if occured:
            if i == pat:
                answer += i
            else:
                break
        else:
            answer += i
            if i == pat:
                occured = True

    return answer