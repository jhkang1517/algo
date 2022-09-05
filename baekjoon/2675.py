for _ in range(int(input())):
    R, S = map(str, input().split())
    ans = ""
    for s in S:
        ans += s*int(R)
    print(ans)
