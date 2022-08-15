# 괄호
for _ in range(int(input())):
    stk = list()
    for ch in input():
        stk.append(ch)

        if len(stk) < 2:
            continue

        if stk[-2] + stk[-1] == '()':
            stk.pop()
            stk.pop()

    print("NO" if stk else "YES")