"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            distances = {}
            for q in points:
                x_dist = p[0]-q[0]
                y_dist = p[1]-q[1]
                distances[x_dist*x_dist + y_dist*y_dist] = 1 + distances.get(x_dist*x_dist + y_dist*y_dist, 0)
            for k in distances:
                res += distances[k] * (distances[k] -1)
        return res
    #     res = 0
    #     for p in points:
    #         seenDists = {}
    #         print("Examining point " + str(p))
    #         for q in points:
    #             dist = self.getSquaredDist(p, q)
    #             print("   With point " + str(q))
    #             seenDists[dist] = 1 + seenDists.get(dist, 0)
    #             print("points are " + str(dist) + " squared units apart")
    #             print("have seen " + str(seenDists[dist]) + " points at this distance")
    #         print("\nConsidering the potential boomerang [" + str(p) + ", j, k]")
    #         for d in seenDists:
    #             res += seenDists[d] * (seenDists[d] - 1)
    #             print("   Recall seeing squared distance of " + str(d) + " a total of " + str(seenDists[d]) + " times, so")
    #             print("there are " + str(seenDists[d]) + " choices for j, and " + str(seenDists[d] - 1) + " choices for k; add " + str(seenDists[d]) + " * " + str(seenDists[d] - 1) + " to res.")
    #         print("res is currently " + str(res))
    #         print("\n")
    #     return res

# def getSquaredDist(self, a, b):
#     return (a[0] - b[0])**2 + (a[1] - b[1])**2

ans = Solution()
print(ans.numberOfBoomerangs([[0,0],[1,0],[2,0]]))