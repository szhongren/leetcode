class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        approach: dp with recursion
        root case: empty s3, return true
        else, check all valid paths, so use last char of s1 or last char of s2 for last char of s3
        """
        cache = {}

        def isInterleaveRecur(s1: str, s2: str, s3: str) -> bool:
            print(s1, s2, s3)
            if (s1, s2, s3) in cache:
                return cache[(s1, s2, s3)]
            if len(s3) == 0:
                result = len(s1) == 0 and len(s2) == 0
                cache[(s1, s2, s3)] = result
                return result
            if len(s1) == 0 and len(s2) == 0:
                result = False
                cache[(s1, s2, s3)] = result
                return result
            s1_last, s2_last, s3_last = "", "", s3[-1]
            if len(s1) > 0:
                s1_last = s1[-1]
            if len(s2) > 0:
                s2_last = s2[-1]

            if s1_last != s3_last and s2_last != s3_last:
                result = False
                cache[(s1, s2, s3)] = result
                return result
            # 1 or both
            results = []
            if s1_last == s3_last:
                results.append(isInterleaveRecur(s1[:-1], s2, s3[:-1]))
            if s2_last == s3_last:
                results.append(isInterleaveRecur(s1, s2[:-1], s3[:-1]))
            result = any(results)
            cache[(s1, s2, s3)] = result
            return result

        return isInterleaveRecur(s1, s2, s3)


sol = Solution()
print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
