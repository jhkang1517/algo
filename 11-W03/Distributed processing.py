example = int(input())
array = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6, 4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1, 9, 1]]

for i in range(example):
    a, b = map(int, input().split())

    if a % 10 == 0:
        print(10)
        continue

    elif a % 10 == 1 or a % 10 == 5 or a % 10 == 6:
        print(a % 10)
        continue

    if b == 0:
        print(1)

    elif b % 4 == 0:
        print(array[a % 10][3])

    else:
        print(array[a % 10][b % 4 - 1])
