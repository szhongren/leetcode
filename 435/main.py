"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
Example 1:
Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:
Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:
Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""

import random as rnd

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def overlapping(i0, i1):
    if i0[0] == i1[0]:
        return True
    elif i0[0] < i1[0]:
        return i0[1] > i1[0]
    elif i1[0] < i0[0]:
        return i1[1] > i0[0]

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 1:
            return 0

        else:
            ls = [[x.start, x.end] for x in intervals]
            ls.sort(key = lambda x: x[1])
            curr = ls[0]
            count = 1
            for i in range(1, len(intervals)):
                if not overlapping(curr, ls[i]):
                    curr = ls[i]
                    count += 1

            return len(intervals) - count

ans = Solution()
print(ans.eraseOverlapIntervals([
    Interval(-100,-87),
    Interval(-99,-44),
    Interval(-98,-19),
    Interval(-97,-33),
    Interval(-96,-60),
    Interval(-95,-17),
    Interval(-94,-44),
    Interval(-93,-9),
    Interval(-92,-63),
    Interval(-91,-76),
    Interval(-90,-44),
    Interval(-89,-18),
    Interval(-88,10),
    Interval(-87,-39),
    Interval(-86,7),
    Interval(-85,-76),
    Interval(-84,-51),
    Interval(-83,-48),
    Interval(-82,-36),
    Interval(-81,-63),
    Interval(-80,-71),
    Interval(-79,-4),
    Interval(-78,-63),
    Interval(-77,-14),
    Interval(-76,-10),
    Interval(-75,-36),
    Interval(-74,31),
    Interval(-73,11),
    Interval(-72,-50),
    Interval(-71,-30),
    Interval(-70,33),
    Interval(-69,-37),
    Interval(-68,-50),
    Interval(-67,6),
    Interval(-66,-50),
    Interval(-65,-26),
    Interval(-64,21),
    Interval(-63,-8),
    Interval(-62,23),
    Interval(-61,-34),
    Interval(-60,13),
    Interval(-59,19),
    Interval(-58,41),
    Interval(-57,-15),
    Interval(-56,35),
    Interval(-55,-4),
    Interval(-54,-20),
    Interval(-53,44),
    Interval(-52,48),
    Interval(-51,12),
    Interval(-50,-43),
    Interval(-49,10),
    Interval(-48,-34),
    Interval(-47,3),
    Interval(-46,28),
    Interval(-45,51),
    Interval(-44,-14),
    Interval(-43,59),
    Interval(-42,-6),
    Interval(-41,-32),
    Interval(-40,-12),
    Interval(-39,33),
    Interval(-38,17),
    Interval(-37,-7),
    Interval(-36,-29),
    Interval(-35,24),
    Interval(-34,49),
    Interval(-33,-19),
    Interval(-32,2),
    Interval(-31,8),
    Interval(-30,74),
    Interval(-29,58),
    Interval(-28,13),
    Interval(-27,-8),
    Interval(-26,45),
    Interval(-25,-5),
    Interval(-24,45),
    Interval(-23,19),
    Interval(-22,9),
    Interval(-21,54),
    Interval(-20,1),
    Interval(-19,81),
    Interval(-18,17),
    Interval(-17,-10),
    Interval(-16,7),
    Interval(-15,86),
    Interval(-14,-3),
    Interval(-13,-3),
    Interval(-12,45),
    Interval(-11,93),
    Interval(-10,84),
    Interval(-9,20),
    Interval(-8,3),
    Interval(-7,81),
    Interval(-6,52),
    Interval(-5,67),
    Interval(-4,18),
    Interval(-3,40),
    Interval(-2,42),
    Interval(-1,49),
    Interval(0,7),
    Interval(1,104),
    Interval(2,79),
    Interval(3,37),
    Interval(4,47),
    Interval(5,69),
    Interval(6,89),
    Interval(7,110),
    Interval(8,108),
    Interval(9,19),
    Interval(10,25),
    Interval(11,48),
    Interval(12,63),
    Interval(13,94),
    Interval(14,55),
    Interval(15,119),
    Interval(16,64),
    Interval(17,122),
    Interval(18,92),
    Interval(19,37),
    Interval(20,86),
    Interval(21,84),
    Interval(22,122),
    Interval(23,37),
    Interval(24,125),
    Interval(25,99),
    Interval(26,45),
    Interval(27,63),
    Interval(28,40),
    Interval(29,97),
    Interval(30,78),
    Interval(31,102),
    Interval(32,120),
    Interval(33,91),
    Interval(34,107),
    Interval(35,62),
    Interval(36,137),
    Interval(37,55),
    Interval(38,115),
    Interval(39,46),
    Interval(40,136),
    Interval(41,78),
    Interval(42,86),
    Interval(43,106),
    Interval(44,66),
    Interval(45,141),
    Interval(46,92),
    Interval(47,132),
    Interval(48,89),
    Interval(49,61),
    Interval(50,128),
    Interval(51,155),
    Interval(52,153),
    Interval(53,78),
    Interval(54,114),
    Interval(55,84),
    Interval(56,151),
    Interval(57,123),
    Interval(58,69),
    Interval(59,91),
    Interval(60,89),
    Interval(61,73),
    Interval(62,81),
    Interval(63,139),
    Interval(64,108),
    Interval(65,165),
    Interval(66,92),
    Interval(67,117),
    Interval(68,140),
    Interval(69,109),
    Interval(70,102),
    Interval(71,171),
    Interval(72,141),
    Interval(73,117),
    Interval(74,124),
    Interval(75,171),
    Interval(76,132),
    Interval(77,142),
    Interval(78,107),
    Interval(79,132),
    Interval(80,171),
    Interval(81,104),
    Interval(82,160),
    Interval(83,128),
    Interval(84,137),
    Interval(85,176),
    Interval(86,188),
    Interval(87,178),
    Interval(88,117),
    Interval(89,115),
    Interval(90,140),
    Interval(91,165),
    Interval(92,133),
    Interval(93,114),
    Interval(94,125),
    Interval(95,135),
    Interval(96,144),
    Interval(97,114),
    Interval(98,183),
    Interval(99,157)]))