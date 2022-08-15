def solution(s=''):
    temp_l = list()
    step = 1
    min_num = len(s)

    while step <= int(len(s)/2):
        print('-'*15)
        min_str = ''
        same_count = 1

        for i in range(0, len(s), step):
            temp_l.append(s[i:i+step])

        print(temp_l)

        for j in range(len(temp_l)):

            if j == 0:
                pass

            elif temp_l[j] == last_j:
                if j == len(temp_l)-1:
                    same_count += 1
                    min_str += str(same_count) + last_j
                else:
                    same_count += 1

            else:
                if j == len(temp_l)-1:
                    min_str += temp_l[j]

                if same_count != 1:
                    min_str += str(same_count)+last_j
                    same_count = 1

                else:
                    min_str += last_j
                    same_count = 1

            last_j = temp_l[j]

        print('min_str: ', min_str)

        if len(min_str) < min_num:
            min_num = len(min_str)

        step += 1
        temp_l = list()

    return min_num

