from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        approach

        for string in strings, generate signature
        signature is difference between successive letters, make this a tuple, and use as key to a map of lists

        edge cases:
        things that go over from z -> a
        convert all negative diffs to positive -> -1 = +25
        len 1 strings
        """

        def generate_signature(s: str):
            diffs = []
            for i in range(len(s) - 1):
                diff = ord(s[i + 1]) - ord(s[i])
                if diff < 0:
                    diff = 26 + diff
                diffs.append(diff)
            if len(diffs) == 0:
                return ()
            return tuple(diffs)

        results = {}
        for s in strings:
            signature = generate_signature(s)
            if signature not in results:
                results[signature] = []
            results[signature].append(s)
        return [ls for ls in results.values()]
