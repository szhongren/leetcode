"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""

import random as rnd

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        l = len(ratings)
        forward = [1] * l
        backward = [1] * l
        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:
                forward[i] = forward[i - 1] + 1
        for i in range(l - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                backward[i] = backward[i + 1] + 1
        return sum(map(max, zip(forward, backward)))

ans = Solution()
for i in range(10):
    kids = [rnd.randrange(10) for _ in range(rnd.randrange(15))]
    print(kids, "\n", ans.candy(kids))
