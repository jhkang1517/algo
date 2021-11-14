def sum67(nums):
    total = 0

    for idx, val in enumerate(nums):
        total += val

        if nums[idx] == 6:
            while nums[idx] != 7:
                idx += 1
                total -= nums[idx]

                if nums[idx] == 6:
                    break
                elif nums[idx] == 7:
                    total -= 6

    return total
