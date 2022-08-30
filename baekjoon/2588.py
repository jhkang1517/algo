a = int(input())
b = input()
ans = 0
for i in range(0, 3):
    s = a * int(b[2-i])
    print(s)
    ans += s * (10**i)
print(ans)