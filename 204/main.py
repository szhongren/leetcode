"""
Count the number of prime numbers less than a non-negative number, n.
"""
import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [True for _ in range(n)]
        count = 0
        seived = eratosthenes(primes)
        for b in seived:
            if b:
                count += 1
        return count

def eratosthenes(ls):
    if len(ls) >= 1:
        ls[0] = False
    if len(ls) > 1:
        ls[1] = False
    for i in range(2, len(ls)):
        if i % 2 == 0 and i != 2:
            ls[i] = False
    i = 3
    end = math.ceil(math.sqrt(len(ls)))
    while i <= end:
        if ls[i]:
            moving = i * i
            while moving < len(ls):
                ls[moving] = False
                moving += i + i
        i += 2

    return ls

ans = Solution()
print(ans.countPrimes(150000))