def solution(s):
    answer = []
    s = s.replace('{{', '').replace('}}','')
    temp = [x.split(',') for x in s.split('},{')]

    length = 1
    while True:

        for t in temp:
            if len(t) == length:
                for u in t:
                    if int(u) not in answer:
                        answer.append(int(u))
                        break

        length += 1
        if length-1 == len(temp):
            break

    return answer