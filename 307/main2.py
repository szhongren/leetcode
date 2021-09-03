"""
Given an integer array nums, handle multiple queries of the following types:

    Update the value of an element in nums.
    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

    NumArray(int[] nums) Initializes the object with the integer array nums.
    void update(int index, int val) Updates the value of nums[index] to be val.
    int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

 

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
"""

from typing import List


class SegmentTreeNode:
    def __init__(self, start, end) -> None:
        self.value = 0
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"({self.value}: {self.start} -> {self.end}, {self.left}, {self.right})"


class NumArray:
    def __init__(self, nums: List[int]):
        # self.nums = nums
        # self.sums = nums.copy()
        # for i in range(1, len(self.sums)):
        #     self.sums[i] += self.sums[i - 1]
        def build_tree(nums, start, end):
            if start == end:
                # leaf
                leaf = SegmentTreeNode(start, end)
                leaf.value = nums[start]
                return leaf
            midpoint = (end + start) // 2

            current_node = SegmentTreeNode(start, end)
            current_node.left = build_tree(nums, start, midpoint)
            current_node.right = build_tree(nums, midpoint + 1, end)
            current_node.value = current_node.left.value + current_node.right.value
            return current_node

        self.root = build_tree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        # self.nums[index] = val
        # if index == 0:
        #     self.sums[index] = val
        # for i in range(max(index, 1), len(self.sums)):
        #     self.sums[i] = self.nums[i] + self.sums[i - 1]
        def update_node(root, index, val):
            if root.start == index == root.end:
                root.value = val
                return
            midpoint = (root.start + root.end) // 2
            if index <= midpoint:
                update_node(root.left, index, val)
            else:
                update_node(root.right, index, val)
            root.value = root.left.value + root.right.value

        update_node(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        # if left == 0:
        #     return self.sums[right]
        # return self.sums[right] - self.sums[left - 1]
        def sum_range_on_node(root, i, j):
            if root.start == i and root.end == j:
                return root.value

            mid = (root.start + root.end) // 2

            if j <= mid:
                return sum_range_on_node(root.left, i, j)

            elif i >= mid + 1:
                return sum_range_on_node(root.right, i, j)

            else:
                return sum_range_on_node(root.left, i, mid) + sum_range_on_node(
                    root.right, mid + 1, j
                )

        return sum_range_on_node(self.root, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

numArray = NumArray([1, 3, 5])
print(numArray.sumRange(0, 2))  # return 1 + 3 + 5 = 9
print(numArray.root)
numArray.update(1, 2)  # nums = [1, 2, 5]
print(numArray.root)
print(numArray.sumRange(0, 2))  # return 1 + 2 + 5 = 8
print(numArray.sumRange(1, 2))  # return 1 + 2 + 5 = 8
print(numArray.sumRange(2, 2))  # return 1 + 2 + 5 = 8

numArray1 = NumArray([-1])
print(numArray1.root)
print(numArray1.sumRange(0, 0))
numArray1.update(0, 1)
print(numArray1.sumRange(0, 0))
