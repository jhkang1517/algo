l, s = map(int, input().split())
coins = [int(input()) for _ in range(l)]

# me
cnt = 0
while s != 0:
    lcm = 100000001
    c = 0
    for coin in coins:
        cm = s // coin
        if cm != 0 and cm < lcm:
            lcm = cm
            c = coin
    cnt += lcm
    s -= lcm * c
print(cnt)

# teacher
N, K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
ans = 0
for coin in coins:
    ans += K // coin
    K %= coin
