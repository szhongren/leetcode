from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        """
        recursive, if n == 1, return all non mirrored, else, return 2 with mirroring
        """

        def findStrobogrammaticRecur(n: int) -> List[str]:
            if n == 1:
                return ["0", "1", "8"]
            if n == 2:
                return ["00", "11", "69", "88", "96"]
            else:
                inner_numbers = findStrobogrammaticRecur(n - 2)
                result = []
                for number in inner_numbers:
                    result.append(f"0{number}0")
                    result.append(f"1{number}1")
                    result.append(f"8{number}8")
                    result.append(f"6{number}9")
                    result.append(f"9{number}6")
            return result

        def all_zero(s: str) -> bool:
            if len(s) == 1:
                return False
            return s[0] == "0"

        result = findStrobogrammaticRecur(n)

        return [res for res in result if not all_zero(res)]
