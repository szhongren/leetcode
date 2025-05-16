from typing import Set


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        approach
        brute force
        recurse down one letter at a time, use a set to return number of possibilities
        example

        recur(AAA) = recur(AA) + A at every position
        recur(AA) = recur(A) + A at every position
        recur(A) = [A]
        recur(AA) = [A, AA]

        recur(ABC) = recur(BC) + A at every position
        recur(BC) = recur(C) + B at every position
        recur(C) = [C]
        recur(BC) = [C, B, CB, BC]
        recur(ABC) = [A, C, B, CB, BC, AC, CA, AB, BA, ACB, CAB, CBA, ABC, BAC, BCA]

        """

        def numTilePossibilitiesRecur(tiles: str) -> Set[str]:
            if len(tiles) == 1:
                return set([tiles])
            first_char = tiles[0]
            recursive_solution = numTilePossibilitiesRecur(tiles[1:])
            new_set = set()
            for seq in recursive_solution:
                for i in range(len(seq) + 1):
                    new_set.add(seq[:i] + first_char + seq[i:])
            recursive_solution.add(first_char)
            return recursive_solution.union(new_set)

        return len(numTilePossibilitiesRecur(tiles))
