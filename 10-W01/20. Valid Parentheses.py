class Solution:
    def isValid(self, s):
        count = 1
        while count < 10000:
            s = s.replace('()','')
            s = s.replace('{}','')
            s = s.replace('[]','')

            if s == '':
                return True
            count += 1

        return False
