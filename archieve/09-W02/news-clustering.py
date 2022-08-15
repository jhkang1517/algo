def solution(str1, str2):
    alphabet = 'zxcvbnmasdfghjklqwertyuiop'
    list_1 = list()
    list_2 = list()

    for i in range(0, len(str1)):
        temp_word = str1[i:i+2].lower()

        if len(temp_word) == 2:
            if temp_word[0] in alphabet and temp_word[1] in alphabet:
                list_1.append(temp_word)
        else:
            pass

    for i in range(0, len(str2)):
        temp_word = str2[i:i+2].lower()

        if len(temp_word) == 2:
            if temp_word[0] in alphabet and temp_word[1] in alphabet:
                list_2.append(temp_word)
        else:
            pass

    if list_1 == [] and list_2 == []:
        return 65536

    set_1 = set(list_1)
    set_2 = set(list_2)

    intersec = set_1.intersection(set_2)
    union = set_1.union(set_2)

    multi_intersec = list()
    for i in intersec:
        for j in range(min(list_1.count(i), list_2.count(i))):
            multi_intersec.append(i)

    multi_union = list()
    for i in union:
        for j in range(max(list_1.count(i), list_2.count(i))):
            multi_union.append(i)

    return int(len(multi_intersec)/len(multi_union)*65536)