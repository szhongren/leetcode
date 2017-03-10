"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = {}
        max_count = 0
        for i in s:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
            max_count = max(max_count, counts[i])
        strings = ["" for _ in range(max_count)]
        for k, v in counts.items():
            strings[max_count - v] += v * k
        return ''.join(strings)

ans = Solution()
print(ans.frequencySort("tree"))
print(ans.frequencySort("cccaaa"))
print(ans.frequencySort("Aabb"))
