# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: list, l2: list):

        l1 = [str(x) for x in l1]
        l2 = [str(x) for x in l2]

        numl1 = int(''.join(l1)[::-1])
        numl2 = int(''.join(l2)[::-1])

        return numl1 + numl2