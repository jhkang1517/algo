def solution(s):
    word_list = s.split(' ')
    t = list()

    for w in word_list:

        try:
            change = w[0].upper()
            w = change + w[1:].lower()
            t.append(w)
        except:
            t.append(w)

    answer = ' '.join(t)
    return answer