import re

def is_int(string):
    result = ''
    for s in string:
        try:
            if type(int(s)) == int:
                result += s
            else:
                pass
        except:
            pass
    return int(result)

def solution(dartResult=''):
    fst = [0, 0, 0]
    flag = 0
    score_list = re.findall('[0-9]{1,2}[a-zA-Z#*]{1,2}', dartResult)

    for s in score_list:
        num = is_int(s)

        if 'S' in s:
            fst[flag] += num ** 1

        elif 'D' in s:
            fst[flag] += num ** 2

        elif 'T' in s:
            fst[flag] += num ** 3

        if '*' in s:
            if flag == 0:
                fst[flag] *= 2

            else:
                fst[flag] *= 2
                fst[flag-1] *= 2

        if '#' in s:
            fst[flag] *= -1

        flag += 1

    answer = sum(fst)
    return answer