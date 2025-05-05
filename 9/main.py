class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        cases
        neg -> false
        positive -> recursive
        return true after loop or at base case
        """
        if x < 0:
            return False

        def isPalindromeRecur(x: int, p: int) -> bool:
            # 1 digit or 0
            if p <= 1:
                return True
            last_digit = x % 10
            first_digit = x // p
            print(x, p)
            print(last_digit, first_digit)
            if last_digit != first_digit:
                return False
            return isPalindromeRecur((x - (first_digit * p)) // 10, p / 100)

        p = 10
        while p <= x:
            p *= 10
        p /= 10
        return isPalindromeRecur(x, p)


sol = Solution()
print(sol.isPalindrome(1001))

"""
0 -> True
1 -> True
10 -> False
11 -> True
100 -> False
101 -> True
100011 -> False
"""
