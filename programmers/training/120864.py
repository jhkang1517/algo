from string import ascii_lowercase


def solution1(my_string):
    lowers = my_string.lower()

    for alp in list(ascii_lowercase):
        lowers = lowers.replace(alp, ',')

    return sum([int(x) for x in lowers.split(',') if x != ''])



def solution2(my_string):
    s = ''.join(x if x.isdigit() else ' ' for x in my_string)
