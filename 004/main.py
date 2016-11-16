# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 + l2 <= 4:
            return median(l1 + l2)
        else:
            return median([median(nums1), median(nums2)])

def findMedianSortedArraysHelper(nums1, nums2, start1, end1, start2, end2):


def median(ls):
    length = len(ls)
    half_length = length // 2
    if length % 2 == 0:
        return sum(ls[half_length - 1: half_length + 1])/2
    else:
        return ls[half_length]

ans = Solution()
nums1 = [1, 3]
nums2 = [2]
print(ans.findMedianSortedArrays(nums1, nums2))
nums1 = [1, 2]
nums2 = [3, 4]
print(ans.findMedianSortedArrays(nums1, nums2))