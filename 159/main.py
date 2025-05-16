class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        approach
        sliding window
        have frequencies map
        slow = 0
        max_len = 0
        for i in range(len(s)):
            map[s[i]] += 1
            if map[s[i]] == 1:
                unique_count += 1
            if unique_count > 2:
                slow += 1
                until unique_count == 2
            max_len = max(max_len, i - slow)

        eeeeeaaaaa
        0123456789

        state: i | slow | max | unique | map
               0   0      0     0        {}
               0   0      1     1        e:1
               4   0      5     1        e:5
        i=0
        e:1
        unique=1
        max = 1

        i=1
        e:2
        unique=1
        max = 2

        i=2
        e:3
        unique=1
        max = 3

        i=4
        e:5
        unique=1
        max = 5

        i=5
        e:5,a:1
        unique=2
        max = 6

        eeabbbb

        i=0
        e:1
        unique=1
        max = 1

        i=1
        e:2
        unique=1
        max = 2

        i=2
        e:2,a:1
        unique=2
        max = 3

        i=3
        e:2,a:1,b:1
        unique=3

        slow=0
        e:1,a:1,b:1

        slow=1
        e:0,a:1,b:1
        unique=2
        slow=2

        aaaaaaa
        """
        count_of_char = {}
        slow = 0
        max_len = 0
        unique_chars = 0
        for i in range(len(s)):
            if s[i] not in count_of_char:
                count_of_char[s[i]] = 0
            count_of_char[s[i]] += 1
            if count_of_char[s[i]] == 1:
                # new char
                unique_chars += 1
            while unique_chars > 2:
                count_of_char[s[slow]] -= 1
                if count_of_char[s[slow]] == 0:
                    unique_chars -= 1
                slow += 1
            max_len = max(max_len, i - slow + 1)
        return max_len
