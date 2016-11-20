"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

Hint:

A direct way is to use the backtracking approach.
Backtracking should contains three states which are (the current number, number of steps to get that number and a bitmask which represent which number is marked as visited so far in the current number). Start with state (0,0,0) and count all valid number till we reach number of steps equals to 10n.
This problem can also be solved using a dynamic programming approach and some knowledge of combinatorics.
Let f(k) = count of numbers with unique digits with length equals k.
f(1) = 10, ..., f(k) = 9 * 9 * 8 * ... (9 - k + 2) [The first factor is 9 because a number cannot start with 0].
"""

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        else:
            prev = self.countNumbersWithUniqueDigits(n - 1)
            result = 9
            for i in range(9, 9 - n + 1, -1):
                result *= i
            return result + prev

ans = Solution()
for i in range(4):
    print(ans.countNumbersWithUniqueDigits(i))

"""
100 f
101 f
102 t
103 t
104 t
105 t
106 t
107 t
108 t
109 t
-> 2f 8t

110 f
111 f
112 f
113 f
114 f
115 f
116 f
117 f
118 f
119 f
-> 10f

120 t
121 f
122 f
123 t
124 t
125 t
126 t
127 t
128 t
129 t
-> 2f 8t

130 t
131 f
132 t
133 f
134 t
135 t
136 t
137 t
138 t
139 t
-> 2f 8t

8 * 9 * 9 + 81, n == 3

1000 f
1001 f
1002 f
1003 f
1004 f
1005 f
1006 f
1007 f
1008 f
1009 f
-> 10f

1200 f
1201 f
1202 f
1203 t
1204 t
1205 t
1206 t
1207 t
1208 t
1209 t
-> 3f 7t


"""