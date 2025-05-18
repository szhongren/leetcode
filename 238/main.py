from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        approach
        get prefix product and suffix product
        then, insert solution into result
        """
        n = len(nums)
        prefix_product = [1] * n
        suffix_product = [1] * n
        prefix_product[0] = nums[0]
        suffix_product[-1] = nums[-1]
        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i]
        for i in range(n - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i]
        result = [suffix_product[1]]
        for i in range(1, n - 1):
            result.append(prefix_product[i - 1] * suffix_product[i + 1])
        result.append(prefix_product[-2])
        return result
