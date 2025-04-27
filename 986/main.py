from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        """
        for each pair, find intersections
        then advance the one with a smaller end
        """

        def find_intersection(a: List[int], b: List[int]) -> List[int]:
            left = max(a[0], b[0])
            right = min(a[1], b[1])
            if left <= right:
                return [left, right]
            else:
                return None

        a, b = 0, 0
        result = []
        while a < len(firstList) and b < len(secondList):
            first_item, second_item = firstList[a], secondList[b]
            intersection = find_intersection(first_item, second_item)
            if intersection:
                result.append(intersection)
            if first_item[1] > second_item[1]:
                b += 1
            else:
                a += 1
        return result
