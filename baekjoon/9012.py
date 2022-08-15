# 괄호
for _ in range(int(input())):
    vps = '()'
    text = input()
    while vps in text:
        text = text.replace(vps, '')

    print("NO" if text else "YES")

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

# 괄호
for _ in range(int(input())):
    stk = list()
    isVPS = True
    for ch in input():
        if ch == '(':
            stk.append(ch)
        else:
            if stk:
                stk.pop()
            else:
                isVPS = False
                break

    if stk:
        isVPS = False

    print("YES" if isVPS else "NO")