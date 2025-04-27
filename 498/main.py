from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        approach
        0, 0
        0, 1: 1, 0
        2, 0: 1, 1: 0, 2
        0, 3: 1, 2: 2, 1: 3, 0
        """

        def elegant_solution():
            values = []
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    values.append((i + j, i, j, mat[i][j]))
            sorted_values = sorted(
                values, key=lambda x: (x[0], x[2] if x[0] % 2 == 0 else x[1])
            )
            print(sorted_values)
            return [value[3] for value in sorted_values]

        return elegant_solution()

        rows = len(mat)
        cols = len(mat[0])

        def get_next_coord(x: int, y: int):
            if x == rows - 1 and y == cols - 1:
                return None
            elif x == rows - 1:
                if (x + y) % 2 == 0:
                    return (x - 1, y + 1)
                else:
                    return (x, y + 1)
            elif y == cols - 1:
                if (x + y) % 2 == 0:
                    return (x + 1, y)
                else:
                    return (x + 1, y - 1)
            elif x == 0:
                if (x + y) % 2 == 0:
                    return (x, y + 1)
                else:
                    return (x + 1, y - 1)
            elif y == 0:
                if (x + y) % 2 == 0:
                    return (x - 1, y + 1)
                else:
                    return (x + 1, y)

            if (x + y) % 2 == 0:
                return (x - 1, y + 1)
            else:
                return (x + 1, y - 1)

        coord = (0, 0)
        result = []
        while coord is not None:
            x, y = coord
            coord = get_next_coord(x, y)
            if x < 0 or y < 0 or x > rows - 1 or y > cols - 1:
                continue
            result.append(mat[x][y])
        return result


sol = Solution()
print(sol.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
