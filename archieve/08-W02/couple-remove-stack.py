def solution(s=''):
    stack = []

    for i in s:
        if len(stack) > 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if stack == []:
        return 1
    else:
        return 0

