"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            seen = {}
            for ch in row:
                if ch == '.':
                    continue
                elif ch in seen:
                    return False
                else:
                    seen[ch] = True

        for i in range(9):
            seen = {}
            for j in range(9):
                curr = board[j][i]
                if curr == '.':
                    continue
                elif curr in seen:
                    return False
                else:
                    seen[curr] = True

        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                seen = {}
                for x in range(3):
                    for y in range(3):
                        curr = board[i + x][j + y]
                        if curr == '.':
                            continue
                        elif curr in seen:
                            return False
                        else:
                            seen[curr] = True
                print(seen)
        return True


ans = Solution()
print(ans.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]))