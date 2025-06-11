from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n + 1)
        # last is zero, to handle the base case
        dp[-1] = True
        for i in range(n):
            for word in words:
                # if word longer than number of letters we have already seen
                if i - len(word) < -1:
                    continue
                # if word does not match
                if not s[: i + 1].endswith(word):
                    continue
                # if previous spot was not a potential string
                if not dp[i - len(word)]:
                    continue
                dp[i] = True
        return dp[-2]


ans = Solution()
print(ans.wordBreak("leetcode", ["leet", "code"]))
print(ans.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(
    ans.wordBreak(
        "bccdbacdbdacddabbaaaadababadad",
        [
            "cbc",
            "bcda",
            "adb",
            "ddca",
            "bad",
            "bbb",
            "dad",
            "dac",
            "ba",
            "aa",
            "bd",
            "abab",
            "bb",
            "dbda",
            "cb",
            "caccc",
            "d",
            "dd",
            "aadb",
            "cc",
            "b",
            "bcc",
            "bcd",
            "cd",
            "cbca",
            "bbd",
            "ddd",
            "dabb",
            "ab",
            "acd",
            "a",
            "bbcc",
            "cdcbd",
            "cada",
            "dbca",
            "ac",
            "abacd",
            "cba",
            "cdb",
            "dbac",
            "aada",
            "cdcda",
            "cdc",
            "dbc",
            "dbcb",
            "bdb",
            "ddbdd",
            "cadaa",
            "ddbc",
            "babb",
        ],
    )
)
print(ans.wordBreak("aaaaaaa", ["aaaa", "aaa"]))
print(ans.wordBreak("goalspecial", ["go", "goal", "goals", "special"]))
print(
    ans.wordBreak(
        "acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb",
        [
            "abbcbda",
            "cbdaaa",
            "b",
            "dadaaad",
            "dccbbbc",
            "dccadd",
            "ccbdbc",
            "bbca",
            "bacbcdd",
            "a",
            "bacb",
            "cbc",
            "adc",
            "c",
            "cbdbcad",
            "cdbab",
            "db",
            "abbcdbd",
            "bcb",
            "bbdab",
            "aa",
            "bcadb",
            "bacbcb",
            "ca",
            "dbdabdb",
            "ccd",
            "acbb",
            "bdc",
            "acbccd",
            "d",
            "cccdcda",
            "dcbd",
            "cbccacd",
            "ac",
            "cca",
            "aaddc",
            "dccac",
            "ccdc",
            "bbbbcda",
            "ba",
            "adbcadb",
            "dca",
            "abd",
            "bdbb",
            "ddadbad",
            "badb",
            "ab",
            "aaaaa",
            "acba",
            "abbb",
        ],
    )
)
print(
    ans.wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        [
            "a",
            "aa",
            "aaa",
            "aaaa",
            "aaaaa",
            "aaaaaa",
            "aaaaaaa",
            "aaaaaaaa",
            "aaaaaaaaa",
            "aaaaaaaaaa",
        ],
    )
)
print(
    ans.wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        [
            "aa",
            "aaa",
            "aaaa",
            "aaaaa",
            "aaaaaa",
            "aaaaaaa",
            "aaaaaaaa",
            "aaaaaaaaa",
            "aaaaaaaaaa",
            "ba",
        ],
    )
)
