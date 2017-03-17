"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""
from collections import deque
import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # uglies = [1]
        # def gen(prime):
        #     for ugly in uglies:
        #         yield ugly * prime
        # merged = heapq.merge(*map(gen, primes))
        # while len(uglies) < n:
        #     ugly = next(merged)
        #     if ugly != uglies[-1]:
        #         uglies.append(ugly)
        # return uglies[-1]

        numbers = {prime: deque([1]) for prime in primes}
        # numbers = {prime: deque([prime]) for prime in primes}
        # val_indexes = {}
        # seen = {prime: True for prime in primes}
        # seen[1] = True

        ans = None
        for i in range(n):
            min_val = min([numbers[fact][0] for fact in primes])

            # min_val = 999999999999999
            # min_val_i = None

            # for fact in primes:
            #     first_num = numbers[fact][0]
            #     if first_num < min_val:
            #         min_val = first_num
            #         min_val_i = fact
            #     if first_num in val_indexes:
            #         val_indexes[first_num].add(fact)
            #     else:
            #         val_indexes[first_num] = set([fact])

            for factor in primes:
                numbers[factor].append(factor * min_val)
                if numbers[factor][0] == min_val:
                    numbers[factor].popleft()

            # for j in val_indexes[min_val]:
            #     numbers[j].popleft()

            # del val_indexes[min_val]

            ans = min_val
        return ans

ans = Solution()
print(ans.nthSuperUglyNumber(100000, [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]))
print(ans.nthSuperUglyNumber(4000, [2,3,5,13,19,29,31,41,43,53,59,73,83,89,97,103,107,109,127,137,139,149,163,173,179,193,197,199,211,223,227,229,239,241,251,257,263,269,271,281,317,331,337,347,353,359,367,373,379,389,397,409,419,421,433,449,457,461,463,479,487,509,521,523,541,547,563,569,577,593,599,601,613,619,631,641,659,673,683,701,709,719,733,739,743,757,761,769,773,809,811,829,857,859,881,919,947,953,967,971]))
for i in range(1, 15):
    print(ans.nthSuperUglyNumber(i, [2, 7, 13, 19]))
