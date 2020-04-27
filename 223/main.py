"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total = (C - A) * (D - B) + (G - E) * (H - F)
        x_overlap = [max(A, E), min(C, G)]
        y_overlap = [max(B, F), min(D, H)]
        if x_overlap[1] > x_overlap[0] and y_overlap[1] > y_overlap[0]:
            total -= (x_overlap[1] - x_overlap[0]) * (y_overlap[1] - y_overlap[0])
        return total

ans = Solution()
print(ans.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))