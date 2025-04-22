from typing import List
from pprint import pprint


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        approach:
        build a trie like structure with ordering first, word by word
        then, traverse the trie, for each branch, that tells us the relative order between items. we can then come up with the rules of the ordering
        """

        # step 1: parse rules
        adjacency = {c: set() for word in words for c in word}
        in_degree = {c: 0 for word in words for c in word}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            # Find first different character
            if len(word1) > len(word2) and word1[: len(word2)] == word2:
                return ""
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in adjacency[c1]:
                        adjacency[c1].add(c2)
                        in_degree[c2] += 1
                    break
        # step 2:
        stack = [c for c in in_degree if in_degree[c] == 0]
        if len(stack) == 0:
            return ""
        ordered = ""
        while stack:
            c = stack.pop()
            ordered += c
            for next_c in adjacency[c]:
                in_degree[next_c] -= 1
                if in_degree[next_c] == 0:
                    stack.append(next_c)
        # check for cycle
        if len(ordered) != len(adjacency):
            return ""
        return ordered


sol = Solution()

print(sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
print(sol.alienOrder(["z", "x"]))
print(sol.alienOrder(["z", "x", "z"]))
print(sol.alienOrder(["ac", "ab", "zc", "zb"]))
