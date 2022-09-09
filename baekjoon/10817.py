A, B, C = map(int, input().split())
MX = 0
MD = 0
MN = 0
if A >= B:
    MX = A
    if B >= C:
        MD = B
        MN = C
    else:
        if C >= A:
            MX = C
            MD = A
            MN = B
        else:
            MD = C
            MN = B
elif B >= A:
    MX = B
    if A >= C:
        MD = A
        MN = C
    else:
        if C >= B:
            MX = C
            MD = B
            MN = A
        else:
            MD = C
            MN = A
print(MD)
