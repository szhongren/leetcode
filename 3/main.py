class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        approach
        keep 2 pointers, start and end
        end is in loop
        keep a running count of chars
        if has repeats, move left
        get max length
        abcabcbb
        i | ch | slow | max_len | chars
        0 | a  | 0    | 0       | {a: 1}
        1 | b  | 0    | 2       | {a: 1, b: 1}
        2 | c  | 0    | 3       | {a: 1, b: 1, c: 1}
        3 | a  | 0    | 3       | {a: 2, b: 1, c: 1}
        3 | a  | 1    | 3       | {a: 1, b: 1, c: 1}
        """
        chars = {}
        slow = 0
        max_len = 0
        n = len(s)
        for i in range(n):
            ch = s[i]
            if ch not in chars:
                chars[ch] = 0
            chars[ch] += 1
            while chars[ch] > 1:
                chars[s[slow]] -= 1
                slow += 1
            max_len = max(max_len, i - slow + 1)
        return max_len
