def solution(arr, queries):
    answer = []

    for i, q in enumerate(queries):
        s = q[0]
        e = q[1]
        k = q[2]

        if s <= i <= e:
            m = list()
            a = arr[s:e + 1]
            while a:
                n = a.pop()
                if n > k:
                    m.append(n)
        else:
            continue

        if m:
            answer.append(min(m))
        else:
            answer.append(-1)
    return answer
