import re

def solution(dartResult=''):
    answer = 0
    print(re.findall('[0-9]{1,2}[a-zA-Z#*]{1,2}', dartResult))

    return answer

solution('1D2S#10S')