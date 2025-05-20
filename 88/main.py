from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        * 2 pointers
        * go from back to keep it simple
        """
        target = len(nums1) - 1
        a, b = m - 1, n - 1
        while a >= 0 and b >= 0:
            val1, val2 = nums1[a], nums2[b]
            if val1 < val2:
                # swap b
                nums1[target] = nums2[b]
                target -= 1
                b -= 1
            else:
                nums1[target] = nums1[a]
                target -= 1
                a -= 1
        while b >= 0:
            nums1[target] = nums2[b]
            target -= 1
            b -= 1
