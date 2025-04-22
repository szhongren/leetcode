class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        approach:
        count number of open parens without matching close parens
        count number of close parens without matching open parens
        return sum
        """
        opened = 0
        opens_needed = 0
        for c in s:
            if c == "(":
                opened += 1
            else:
                if opened == 0:
                    opens_needed += 1
                else:
                    opened -= 1

        return opened + opens_needed
