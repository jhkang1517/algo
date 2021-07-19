# 1st Solution

def solution(numbers, hand):
    answer = ''

    correct = dict()

    correct['*'] = [hand, 4, 3, 2, 1]
    correct['#'] = [hand, 4, 3, 2, 1]
    correct[1] = [hand, 1, 2, 3, 4]
    correct[2] = [hand, 0, 1, 2, 3]
    correct[3] = [hand, 1, 2, 3, 4]
    correct[4] = [hand, 2, 1, 2, 3]
    correct[5] = [hand, 1, 0, 1, 2]
    correct[6] = [hand, 2, 1, 2, 3]
    correct[7] = [hand, 3, 2, 1, 2]
    correct[8] = [hand, 2, 1, 0, 1]
    correct[9] = [hand, 3, 2, 1, 2]
    correct[0] = [hand, 3, 2, 1, 0]

    lhand = '*'
    rhand = '#'

    for n in numbers:

        if n in [1, 4, 7]:
            answer += 'L'
            lhand = n

        elif n in [3, 6, 9]:
            answer += 'R'
            rhand = n

        else:

            if n == 2:
                num1 = correct[lhand][1]
                num2 = correct[rhand][1]

                if num1 > num2:
                    answer += 'R'
                    rhand = n

                elif num1 < num2:
                    answer += 'L'
                    lhand = n

                else:
                    if hand == 'right':
                        answer += 'R'
                        rhand = n
                    else:
                        answer += 'L'
                        lhand = n

            elif n == 5:
                num1 = correct[lhand][2]
                num2 = correct[rhand][2]

                if num1 > num2:
                    answer += 'R'
                    rhand = n

                elif num1 < num2:
                    answer += 'L'
                    lhand = n

                else:
                    if hand == 'right':
                        answer += 'R'
                        rhand = n
                    else:
                        answer += 'L'
                        lhand = n

            elif n == 8:
                num1 = correct[lhand][3]
                num2 = correct[rhand][3]

                if num1 > num2:
                    answer += 'R'
                    rhand = n

                elif num1 < num2:
                    answer += 'L'
                    lhand = n

                else:
                    if hand == 'right':
                        answer += 'R'
                        rhand = n
                    else:
                        answer += 'L'
                        lhand = n

            elif n == 0:
                num1 = correct[lhand][4]
                num2 = correct[rhand][4]

                if num1 > num2:
                    answer += 'R'
                    rhand = n

                elif num1 < num2:
                    answer += 'L'
                    lhand = n

                else:
                    if hand == 'right':
                        answer += 'R'
                        rhand = n
                    else:
                        answer += 'L'
                        lhand = n
    return answer


# 2nd Solution
def solution2(numbers, hand):
    answer = ''

    correct = dict()
    correct['*'] = [1, 4, 3, True, 2, 1]
    correct['#'] = [1, 4, 3, True, 2, 1]
    correct[1] = [4, 1, 2, True, 3, 4]
    correct[2] = [3, 0, 1, True, 2, 3]
    correct[3] = [4, 1, 2, True, 3, 4]
    correct[4] = [3, 2, 1, True, 2, 3]
    correct[5] = [2, 1, 0, True, 1, 2]
    correct[6] = [3, 2, 1, True, 2, 3]
    correct[7] = [2, 3, 2, True, 1, 2]
    correct[8] = [1, 2, 1, True, 0, 1]
    correct[9] = [2, 3, 2, True, 1, 2]
    correct[0] = [0, 3, 2, True, 1, 0]

    lhand = '*'
    rhand = '#'

    for n in numbers:

        if n in [1, 4, 7]:
            answer += 'L'
            lhand = n

        elif n in [3, 6, 9]:
            answer += 'R'
            rhand = n

        else:

            num1 = correct[lhand][int(n / 2)]
            num2 = correct[rhand][int(n / 2)]

            if num1 > num2:
                answer += 'R'
                rhand = n

            elif num1 < num2:
                answer += 'L'
                lhand = n

            else:
                if hand == 'right':
                    answer += 'R'
                    rhand = n
                else:
                    answer += 'L'
                    lhand = n

    return answer