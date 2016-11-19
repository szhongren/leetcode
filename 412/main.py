# FizzBuzz
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n+1):
            add = ""
            if i % 3 == 0:
                add += "Fizz"
            if i % 5 == 0:
                add += "Buzz"
            if i % 5 != 0 and i % 3 != 0:
                add = str(i)
            result.append(add)
        return result

ans = Solution()
print(ans.fizzBuzz(18))
