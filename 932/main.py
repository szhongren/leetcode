from typing import List


class Solution:
    def beautifulArray(self, n: int):
        memo = {1: [1]}

        def compute_number_sequence(n):
            if n not in memo:
                print(f"{n} not in memo")
                odds = compute_number_sequence((n + 1) // 2)
                evens = compute_number_sequence(n // 2)
                memo[n] = [2 * x - 1 for x in odds] + [2 * x for x in evens]
            return memo[n]

        return compute_number_sequence(n)


sol = Solution()
print(sol.beautifulArray(1))
print(sol.beautifulArray(2))
print(sol.beautifulArray(3))
print(sol.beautifulArray(4))
print(sol.beautifulArray(5))
print(sol.beautifulArray(10))
