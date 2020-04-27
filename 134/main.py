"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        l = len(gas)
        excess = [gas[i % l] - cost[i % l] for i in range(2 * l)]
        max_i = -1
        max_excess = 0
        for i in range(l):
            if excess[i] > max_excess:
                max_excess = excess[i]
                max_i = i
        if min(excess) < max_excess:
            return -1
        else:
            return max_i

ans = Solution()
print(ans.canCompleteCircuit([1,2,3,3], [2,1,5,1]))