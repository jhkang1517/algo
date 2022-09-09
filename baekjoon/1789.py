S = int(input())
N = 0
s = 0
for i in range(1, S+1):
    s += i
    if s > S:
        break
    N += 1
print(N)
