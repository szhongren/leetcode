"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""

import math

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return "p[" + self.x + self.y + "]"

class Line(object):
    def __init__(self, m = 0, c = 0):
        self.m = m
        self.c = c

    def __str__(self):
        return "y = " + str(self.m) + "x + " + str(self.c)

def getSlope(p0, p1):
    if p0.y == p1.y:
        return 0
    elif p0.x == p1.x:
        return math.inf
    return (p0.y - p1.y)/(p0.x - p1.x)

def getYIntercept(p0, p1):
    m = getSlope(p0, p1)
    return p0.y - m * p0.x

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        max_count = 0
        seen = {}
        for i in range(len(points)):
            count = 1
            for j in range(i + 1, len(points)):
                m = getSlope(points[i], points[j])
                c = getYIntercept(points[i], points[j])
                l = Line(m, c)
                if l not in seen:
                    seen[l] = 2
                else:
                    seen[l] += 1
                    count = max(count, seen[l])

            max_count = max(max_count, count)
        return max_count

ans = Solution()
print(ans.maxPoints([Point(0, 1), Point(1, 0), Point(0, 0)]))