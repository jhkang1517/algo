import sys
import heapq

pq = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(pq, (abs(x), x))
    else:
        if not pq:
            print(0)
        else:
            print(heapq.heappop(pq)[1])
