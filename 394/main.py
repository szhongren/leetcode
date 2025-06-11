class Solution:
    def decodeString(self, s: str) -> str:
        """
        approach
        divide and conquer
        1. find repeat amount
        2. find value to repeat
        3. return amount * decode(repeated_value) + decode(part after "]")
        """
        n = len(s)
        if s == "":
            return ""

        paren_indexes = {}
        stack = []
        for i in range(n):
            if s[i] not in set(["[", "]"]):
                continue
            elif s[i] == "[":
                stack.append(i)
            elif s[i] == "]":
                paren_indexes[stack.pop()] = i

        if len(paren_indexes) == 0:
            return s

        prefix = ""
        for i in range(n):
            if i not in paren_indexes:
                if not s[i].isdigit():
                    prefix += s[i]
                continue
            repeat_amount = int(s[len(prefix) : i])
            return (
                prefix
                + repeat_amount * self.decodeString(s[i + 1 : paren_indexes[i]])
                + self.decodeString(s[paren_indexes[i] + 1 :])
            )
        return ""
