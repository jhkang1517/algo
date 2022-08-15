class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)

        if len(nums1) % 2 == 1:

            return nums1[len(nums1)//2]

        else:
            return (nums1[len(nums1)//2] + nums1[len(nums1)//2 - 1]) / 2