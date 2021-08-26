def solution(skill='', skill_trees=list()):
    answer = 0

    for sk in skill_trees:
        temp = list()

        for s in skill:

            try:
                temp.append(sk.index(s))

            except:
                pass

        if temp == sorted(temp):
            j = 0
            flag = True
            for i in temp:
                if sk[i] != skill[j]:
                    flag = False
                    break
                j += 1

            if flag == True:
                answer += 1

        else:
            pass

    return answer