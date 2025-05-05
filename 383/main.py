class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for ch in magazine:
            if ch not in count:
                count[ch] = 0
            count[ch] += 1
        for ch in ransomNote:
            if ch not in count:
                return False
            if count[ch] == 0:
                return False
            count[ch] -= 1
        return True
