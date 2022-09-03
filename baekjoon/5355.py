a = "*=3"
b = "+=5"
c = "-=7"

for _ in range(int(input())):
    s = input().replace("@", a).replace("%", b).replace("#", c).split()
    ans = float(s[0])
    for i in s[1:]:
        exec("ans"+i)

    print('{0:.2f}'.format(ans))
