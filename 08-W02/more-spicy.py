import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while 1:

        if len(scoville) == 0:
            return -1

        elif len(scoville) == 1:
            if scoville[0] >= K:
                return count

            else:
                return -1

        most_low = heapq.heappop(scoville)

        if most_low >= K:
            return count

        second_low = heapq.heappop(scoville)
        mix_scov = most_low + (second_low * 2)
        scoville.append(mix_scov)

        count += 1