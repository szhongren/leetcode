class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        approach
        2 pointers
        if both at end, return True
        if one is empty and not the other, return False
        else:
        if not digit:
        check if word[i] == abbr[j]
        if not, return False
        else, recurse with i + 1, j + 1
        if digit, if leading 0, return False
        else, take until not digit
        i += int(value)
        j += len(number)
        """
        m = len(word)
        n = len(abbr)

        def validWordAbbreviationRecur(i: int, j: int):
            if i == m and j == n:
                return True
            if i > m:
                return False
            if i == m or j == n:
                return False

            if abbr[j].isdigit():
                if abbr[j] == "0":
                    return False
                b = j
                while j < n and abbr[j].isdigit():
                    j += 1
                value = int(abbr[b:j])
                return validWordAbbreviationRecur(i + value, j)
            else:
                if word[i] == abbr[j]:
                    return validWordAbbreviationRecur(i + 1, j + 1)
                else:
                    return False

        return validWordAbbreviationRecur(0, 0)
