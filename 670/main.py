class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        approach
        go from the back, keep track of largest value so far, and for each position store the largest value after
        then from the front, first value with a value larger after, swap with the larger value
        """
        digits = [int(x) for x in str(num)]
        n = len(digits)
        largest_so_far = 0
        largest_so_far_i = None
        largest_after = [(0, None)] * n
        for i in range(n - 1, -1, -1):
            largest_after[i] = largest_so_far, largest_so_far_i
            if digits[i] <= largest_so_far:
                continue
            largest_so_far = digits[i]
            largest_so_far_i = i
        for i in range(n):
            largest, largest_i = largest_after[i]
            if digits[i] >= largest:
                continue
            digits[i], digits[largest_i] = digits[largest_i], digits[i]
            return sum([x * (10 ** (n - i - 1)) for i, x in enumerate(digits)])
        return num


sol = Solution()
print(sol.maximumSwap(1234))
print(sol.maximumSwap(2763))
print(sol.maximumSwap(2736))
print(sol.maximumSwap(7531))
