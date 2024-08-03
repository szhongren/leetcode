from pprint import pprint

def removeIslands(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    connected = []
    for i in range(rows):
        if matrix[i][0] == 1:
            connected.append((i, 0))
        if matrix[i][cols - 1] == 1:
            connected.append((i, cols - 1))
    for i in range(cols):
        if matrix[0][i] == 1:
            connected.append((0, i))
        if matrix[rows - 1][i] == 1:
            connected.append((rows - 1, i))
    seen = set()
    while len(connected) > 0:
        # for every point
        new_connected = []
        for y, x in connected:
            # add it to seen
            seen.add((y, x))
            # generate 4 directions
            neighbors = generate_neighbor_coords(y, x)
            # check 4 directions
            for y2, x2 in neighbors:
                # out of bounds
                if y2 < 0 or y2 >= rows or x2 < 0 or x2 >= cols:
                    continue
                # not out of bounds
                if (y2, x2) not in seen and matrix[y2][x2] == 1:
                    new_connected.append((y2, x2))
        connected = new_connected
    pprint(matrix)
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in seen:
                matrix[i][j] = 0
    pprint(matrix)




def generate_neighbor_coords(y, x):
    return [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]

# approachh
# find all connection parts
# iterate through the matrix and find all the spots that are not connected
testCase = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

0, 0
1, 3
1, 4
1, 5
2, 4
3, 0
3, 1
3, 4
4, 0
5, 0
5, 5

removeIslands(testCase)
