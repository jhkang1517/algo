from collections import deque

class Solution:
    def twoSum(self, nums: list, target: int):
        q = deque([nums[0]])
        idx = 1

        while q:
            for i in range(len(nums)):
                q.append(nums[i])

                if idx-1 == i:
                    q.pop()
                    continue

                if sum(q) == target:
                    temp = list()
                    temp.append(idx-1)
                    temp.append(i)
                    return temp

                else:
                    q.pop()

            q.append(nums[idx])
            q.popleft()
            idx += 1



