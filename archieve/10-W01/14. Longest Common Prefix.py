class Solution:
    def longestCommonPrefix(self, strs):

        strs.sort(key=len)
        prefix_list = list()

        if len(strs) == 1:
            return strs[0]

        count = 1
        while count <= len(strs[0]):
            prefix_list.append(strs[0][0:count])
            count += 1

        prefix_list.sort(key=len, reverse=True)
        flag = False

        for p in prefix_list:
            p_len = len(p)

            for i in range(1, len(strs)):

                if p == strs[i][:p_len]:
                    flag = True

                else:
                    flag = False
                    p = '%'

            if flag == True:
                return p

        if flag == False:
            return ""