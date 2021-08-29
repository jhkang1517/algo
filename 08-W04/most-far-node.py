from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    len_list = [0] * (n + 1)
    len_list[1] = 1

    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)

    q = deque([1])
    while q:
        # print('='*15)
        node = q.popleft()
        
        for nei in graph[node]:
            # print('neighbor : ', nei)

            if len_list[nei] == 0:
                len_list[nei] = len_list[node] + 1
                q.append(nei)

            # print('length: ', len_list)

    max_length = max(len_list)
    for l in len_list:
        if l == max_length:
            answer += 1

    return answer