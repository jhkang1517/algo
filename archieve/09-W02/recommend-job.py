def solution(table, languages, preference):

    score_list = [0] * len(table)
    idx_dict = {'1': 5, '2': 4, '3': 3, '4': 2, '5': 1}
    table.sort(key=lambda table: table[0])

    for t in range(len(table)):
        ts = table[t].split(' ')

        for l in range(len(languages)):

            try:
                score_list[t] += idx_dict[str(ts.index(languages[l]))] * preference[l]

            except:
                pass

    idx_max = score_list.index(max(score_list))
    return table[idx_max].split(' ')[0]