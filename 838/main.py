class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        go through list from left, for every R, start at 1 and increment, until we meet an L or R, then reset
        go through list from right, for every L, start at 1 and increment, until we meet an L or R, then reset
        ...LR..
        0000123 -> a
        4321000 -> b
        ...RL..
        0001000 -> a
        0000100 -> b
        .R..L..
        0123000 -> a
        0032100 -> b
        .RR.L..
        0112000 -> a
        0002100 -> b
        .RL.L..
        0000123 -> a
        4321000 -> b
        if equal:
        .
        if one is 0:
            if a > b -> R
            if b > a -> L
        else:
            if a < b -> R
            if b < a -> L
        """
        n = len(dominoes)
        l_counter = [0] * n
        r_counter = [0] * n
        l_counter[-1] = 1 if dominoes[-1] == "L" else 0
        r_counter[0] = 1 if dominoes[0] == "R" else 0
        for i in range(1, n):
            if dominoes[i] == ".":
                if r_counter[i - 1] == 0:
                    r_counter[i] = 0
                else:
                    r_counter[i] = r_counter[i - 1] + 1
            elif dominoes[i] == "R":
                r_counter[i] = 1
            elif dominoes[i] == "L":
                r_counter[i] = 0

        for i in range(n - 2, -1, -1):
            if dominoes[i] == ".":
                if l_counter[i + 1] == 0:
                    l_counter[i] = 0
                else:
                    l_counter[i] = l_counter[i + 1] + 1
            elif dominoes[i] == "R":
                l_counter[i] = 0
            elif dominoes[i] == "L":
                l_counter[i] = 1

        print(dominoes)
        print(l_counter)
        print(r_counter)
        result = ""
        for i in range(n):
            if l_counter[i] == r_counter[i]:
                result += "."
            elif l_counter[i] == 0 or r_counter[i] == 0:
                if l_counter[i] > r_counter[i]:
                    result += "L"
                if l_counter[i] < r_counter[i]:
                    result += "R"
            else:
                if l_counter[i] < r_counter[i]:
                    result += "L"
                if l_counter[i] > r_counter[i]:
                    result += "R"

        return result


sol = Solution()
print(sol.pushDominoes("RR.L"))
print(sol.pushDominoes(".L.R...LR..L.."))
