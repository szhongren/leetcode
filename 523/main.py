from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modulo_list = [0]
        running_sum = 0
        for num in nums:
            running_sum += num
            modulo_list.append(running_sum % k)
        print(modulo_list)
        seen = {}
        for i, modulo in enumerate(modulo_list):
            if modulo not in seen:
                seen[modulo] = i
            if i - seen[modulo] > 1:
                return True
        return False


sol = Solution()
sol.checkSubarraySum([23, 2, 4, 6, 6], 7)
