"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return findRepeatedDnaSequences_k(s, 10)

def findRepeatedDnaSequences_k(s, k):
    l = len(s)
    if k > l:
        return []
    else:
        kmers = []
        for i in range(l - k + 1):
            kmers.append(s[i: i + k])
        kmers.sort()
        results = []
        repeat = False
        for i in range(1, len(kmers)):
            if kmers[i] != kmers[i - 1]:
                repeat = False
            else:
                if repeat:
                    continue
                else:
                    repeat = True
                    results.append(kmers[i])
        return results

ans = Solution()
print(ans.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))