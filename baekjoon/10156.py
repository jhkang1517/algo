K, N, M = map(int, input().split())
ans = K*N-M
if ans >= 0:
    print(ans)
else:
    print(0)
