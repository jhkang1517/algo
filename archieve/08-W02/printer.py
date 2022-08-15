def solution(priorities, location):
    answer = 0
    stack = list()
    priorities.insert(location+1, False)

    while True:
        stack.append(priorities.pop(0))

        if stack[0] < max(priorities):
            priorities.append(stack.pop())

        else:
            answer += 1

            if priorities[0] == False:
                return answer

            stack.pop()