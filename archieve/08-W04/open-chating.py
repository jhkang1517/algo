def solution(record):
    answer = []
    correct = dict()

    for txt in record:
        temp_list = txt.split(' ')

        if temp_list[0] in ('Enter', 'Change'):
            correct[temp_list[1]] = temp_list[2]

    for r in record:
        message = ''
        l = r.split(' ')
        if l[0] == 'Enter':
            message += correct[l[1]]+'님이 들어왔습니다.'
            answer.append(message)

        elif l[0] == 'Leave':
            message += correct[l[1]]+'님이 나갔습니다.'
            answer.append(message)

        else:
            pass

    return answer