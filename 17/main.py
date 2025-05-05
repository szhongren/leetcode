from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        result = [""]
        for digit in digits:
            new_result = []
            for result in result:
                for ch in digit_map[digit]:
                    new_result.append(result + ch)
            result = new_result
        if len(result) == 1:
            return []
        return result
