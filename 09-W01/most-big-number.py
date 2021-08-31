def solution(numbers):
    copy_numbers = [str(x) for x in numbers]
    copy_numbers.sort(key = lambda x: (x*4)[:4], reverse = True) # 인덱스가 부족하다면, 곱해서 강제적으로 길이를 늘린다.

    if max(copy_numbers) == '0':
        return '0'

    answer = ''.join(copy_numbers)
    return answer