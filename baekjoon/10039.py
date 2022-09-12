S = 0
for _ in range(5):
    s = int(input())
    if s < 40:
        S += 40
    else:
        S += s
print(int(S / 5))
