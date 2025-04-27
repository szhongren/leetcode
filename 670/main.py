class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        approach
        go from the back and record the biggest value before an index, preferring later i for tiebreaker
        go from the front, for the first value with a larger value after, swap it
        """
        digits = [int(x) for x in str(num)]
        largest_after = [0 for _ in range(len(digits))]
        largest_so_far = 0
        last_seen_values = {}
        for i in range(len(digits) - 1, -1, -1):
            largest_after[i] = largest_so_far
            largest_so_far = max(digits[i], largest_so_far)
            if digits[i] not in last_seen_values:
                last_seen_values[digits[i]] = i
        for i in range(len(digits)):
            if digits[i] < largest_after[i]:
                digits[i], digits[last_seen_values[largest_after[i]]] = (
                    digits[last_seen_values[largest_after[i]]],
                    digits[i],
                )
                total = 0
                for digit in digits:
                    total *= 10
                    total += digit
                return total
        return num


sol = Solution()
print(sol.maximumSwap(2736))
