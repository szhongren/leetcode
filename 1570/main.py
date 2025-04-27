from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.locations = {}
        for i, item in enumerate(nums):
            self.locations[i] = item

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        union = set(self.locations.keys()).union(vec.locations.keys())
        total = 0
        for location in union:
            total += self.locations[location] * vec.locations[location]
        return total


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
