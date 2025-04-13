class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        2 ptrs
        if match, continue
        if b == len (needle) return a - b
        else, continue and start from 0 for b
        """
        b = 0
        for a in range(len(haystack)):
            if b == len(needle):
                return a - b
            print(f"a: {a}, {haystack[a]} - {b}, {needle[b]}")
            if needle[b] == haystack[a]:
                b += 1
            elif needle[0] == haystack[a]:
                b = 1
            else:
                b = 0

        if b == len(needle):
            return a - b
        return -1

    def create_kmp_array(self, needle: str):
        pass


sol = Solution()
print(sol.strStr("leetcode", "leeto"))
print(sol.strStr("sadbutsad", "but"))
print(sol.strStr("mississippi", "issip"))
