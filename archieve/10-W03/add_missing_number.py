def solution(numbers):
    ll = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in numbers:
        ll[n] = 0

    return sum(ll)

