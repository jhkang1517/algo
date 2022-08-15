def solution(prices):
    answer = []

    for j in range(len(prices)):

        for i in range(j+1,len(prices)):

            if prices[j] > prices[i]:
                break

        answer.append(i-j)

    return answer