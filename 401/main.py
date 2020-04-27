"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
"""

def countBits(v):
    """
    :type v: int
    :rtype: int
    """
    count = 0
    while v != 0:
        if v % 2 == 1:
            count += 1
        v >>= 1
    return count

num_bits = [countBits(i) for i in range(60)]

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        results = []
        for h in range(12):
            for m in range(60):
                time = str(h) + ":"
                if num_bits[h] + num_bits[m] == num:
                    if m < 10:
                        time += "0"
                    time += str(m)
                if time[-1] != ":":
                    results.append(time)
        return results

ans = Solution()
print(ans.readBinaryWatch(2))