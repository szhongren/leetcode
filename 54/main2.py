from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def generate_starting_seen(matrix):
            seen = set()
            number_of_rows = len(matrix)
            number_of_cols = len(matrix[0])
            seen.add((-1, 0))
            seen.add((0, number_of_cols))
            seen.add((number_of_rows, number_of_cols - 1))
            seen.add((number_of_rows - 1, -1))
            return seen

        def is_end(current_element, seen):
            curr_x, curr_y = current_element
            return (
                (curr_x - 1, curr_y) in seen
                and (curr_x + 1, curr_y) in seen
                and (curr_x, curr_y - 1) in seen
                and (curr_x, curr_y + 1) in seen
            )

        def add_element(current_element, seen, direction, elements):
            curr_x, curr_y = current_element
            dir_x, dir_y = direction
            seen.add(current_element)
            elements.append(matrix[curr_x][curr_y])

            if is_end(current_element, seen):
                return elements

            if (curr_x + dir_x, curr_y + dir_y) in seen:
                new_dir_x, new_dir_y = {
                    (0, 1): (1, 0),
                    (1, 0): (0, -1),
                    (0, -1): (-1, 0),
                    (-1, 0): (0, 1),
                }[direction]
                return add_element(
                    (curr_x + new_dir_x, curr_y + new_dir_y),
                    seen,
                    (new_dir_x, new_dir_y),
                    elements,
                )
            else:
                return add_element(
                    (curr_x + dir_x, curr_y + dir_y), seen, direction, elements
                )

        return add_element((0, 0), generate_starting_seen(matrix), (0, 1), [])


print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
