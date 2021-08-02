def solution(nums):
    check_num = int(len(nums) / 2)
    poket_num = len(set(nums))

    if check_num < poket_num:
        return check_num
    else:
        return poket_num