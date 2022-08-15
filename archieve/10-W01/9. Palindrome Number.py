class Solution:
    def isPalindrome(self, x):

        t = str(x)
        if t == t[::-1]:
            return True

        else:
            return False
