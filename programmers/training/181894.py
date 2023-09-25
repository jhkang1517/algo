def solution(arr):
    answer = [i for i, v in enumerate(arr) if v == 2]
    if answer:
        return list(arr[answer[0]:answer[-1] + 1])
    return [-1]


def solution2(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2): len(arr) - arr[::-1].index(2)]
