from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        * 2 pointers
        * go from back to keep it simple
        """
        end = m + n - 1
        while m > 0 and n > 0:
            a, b = nums1[m - 1], nums2[n - 1]
            if a < b:
                nums1[end] = b
                n -= 1
            else:
                nums1[end] = a
                m -= 1
            end -= 1

        if n > 0:
            while n > 0:
                nums1[n - 1] = nums2[n - 1]
                n -= 1
