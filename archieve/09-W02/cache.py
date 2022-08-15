def solution(cacheSize, cities):
    answer = 0
    cities = [ i.upper() for i in cities]
    q = [cities.pop(0)]

    while q:
        if cacheSize == 0:
            answer += len(cities) * 5 + 5
            break

        else:
            if cities == list():
                answer += len(q)*5
                break

            c = cities.pop(0)

            if c in q:
                answer += 1
                q.remove(c)
                q.append(c)

            else:
                if len(q) == cacheSize:
                    q.pop(0)
                    answer += 5
                    q.append(c)
                else:
                    q.append(c)

    return answer