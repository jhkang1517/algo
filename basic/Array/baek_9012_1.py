# 괄호
for _ in range(int(input())):
    vps = '()'
    text = input()
    while vps in text:
        text = text.replace(vps, '')

    print("NO" if text else "YES")