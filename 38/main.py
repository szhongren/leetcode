"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

def next_seq(prev):
    out = ""
    prev_ch = prev[0]
    count = 1
    for ch in prev[1:]:
        if prev_ch == ch:
            count += 1
        else:
            out += str(count) + prev_ch
            count = 1
        prev_ch = ch
    return out + str(count) + prev_ch

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        results = ["" for _ in range(n)]
        if n == 0:
            return ""
        else:
            results[0] = "1"
            for i in range(1, n):
                results[i] = next_seq(results[i - 1])
            return results[-1]

ans = Solution()
for i in range(8):
    print(ans.countAndSay(i))