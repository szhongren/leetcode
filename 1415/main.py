class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        happy strings
        a b c
        ab ac ba bc ca cb
        aba abc aca acb bab bac bca bcb cab cac cba cbc
        0   1   2   3   4   5   6   7   8   9   10  11
        recursive solution
        first check to see if k < 3 * 2 ^ (n - 1)
        if not return ""
        else, recursive call
        k // 2
        if k < 3
        return a, b or c
        k % (total / 3) gives which char to append
        """
        total_strings = int(3 * (2 ** (n - 1)))
        if k > total_strings:
            return ""

        def getHappyStringRecur(n: int, k: int, total_strings: int):
            if n == 1:
                return ["a", "b", "c"][k]
            prefix = getHappyStringRecur(n - 1, k // 2, total_strings / 2)
            next_map = {
                "a": ["b", "c"],
                "b": ["a", "c"],
                "c": ["a", "b"],
            }
            return prefix + next_map[prefix[-1]][k % 2]

        return getHappyStringRecur(n, k, total_strings)


sol = Solution()

print(sol.getHappyString(2, 0))
2, 0, 6
1, 0, 3
"a"
print(sol.getHappyString(2, 1))
print(sol.getHappyString(2, 2))
