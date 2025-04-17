from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            print(key)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return [value for value in groups.values()]


sol = Solution()
sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
