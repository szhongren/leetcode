from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        approach
        get the modulo of the running sum at each point
        if I've seen this modulo before, that means the difference between this point and previous point where I saw same modulo is divisible by k
        return True
        """
        modulo_list = [0]
        running_sum = 0
        for num in nums:
            running_sum += num
            modulo_list.append(running_sum % k)
        seen = {}
        for i, modulo in enumerate(modulo_list):
            if modulo not in seen:
                seen[modulo] = i
            if i - seen[modulo] > 1:
                return True
        return False


sol = Solution()
sol.checkSubarraySum([23, 2, 4, 6, 6], 7)
