def solution(n):
    r = n + 1
    n_bin = format(n, 'b')
    n_bin_cnt = n_bin.count('1')

    while True:
        r_bin = format(r, 'b')
        r_bin_cnt = r_bin.count('1')

        if n_bin_cnt == r_bin_cnt:
            return r

        r += 1