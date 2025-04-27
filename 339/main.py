from typing import List


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        pass

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        pass

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        The result is undefined if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        The result is undefined if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        """
        approach
        recursive
        for each list, go through the values
        if any are lists, recur with +1 depth
        add products
        """

        def depthSumRecur(nestedList: List[NestedInteger], depth: int) -> int:
            total_sum = 0
            for nested_integer in nestedList:
                if nested_integer.isInteger():
                    total_sum += nested_integer.getInteger() * depth
                else:
                    total_sum += depthSumRecur(nested_integer.getList(), depth + 1)
            return total_sum

        return depthSumRecur(nestedList, 1)
