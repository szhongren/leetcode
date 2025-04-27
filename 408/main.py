class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        approach
        recursion, base case:
        "", ""
        else
        if first chars are equal, drop first chars and recur
        else
        get chars until non-numeric, convert to int, and take out first x chars from word and continue
        """

        def validWordAbbreviationRecur(word: str, abbr: str) -> bool:
            if word == "" and abbr == "":
                return True
            if word == "" or abbr == "":
                return False
            if word[0] == abbr[0]:
                return validWordAbbreviationRecur(word[1:], abbr[1:])
            if not abbr[0].isdigit():
                return False
            if abbr[0] == "0":
                return False
            i = 0
            while i < len(abbr) and abbr[i].isdigit():
                i += 1
            count = int(abbr[:i])
            if count > len(word):
                return False
            return validWordAbbreviationRecur(word[count:], abbr[i:])

        return validWordAbbreviationRecur(word, abbr)


sol = Solution()
print(sol.validWordAbbreviation("internationalization", "i5a11o1"))
