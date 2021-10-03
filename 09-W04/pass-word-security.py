def solution(pw):
    num = 0
    lower = 0
    upper = 0
    numlist = ['1', '2', '3', '4', '5',
               '6', '7', '8', '9', '0']

    if len(pw) < 10:
        return False

    for i in range(len(pw)):
        if pw[i:i + 1] in numlist:
            num = 1
            continue
        if pw[i:i + 1].isupper() == False:
            lower = 1
            continue
        if pw[i:i + 1].isupper():
            upper = 1
            continue

    if num + lower + upper == 3:
        return True
    else:
        return False