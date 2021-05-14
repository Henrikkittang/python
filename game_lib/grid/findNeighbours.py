
def findNeighbours(position:tuple, grid: list, diagonal: bool=False):
    neighbours = []
    for t in range(-1, 2):
        for q in range(-1, 2):
            if (diagonal == False) and (abs(t) == abs(q)):
                continue

            if t != 0 or q != 0:
                if position[1] + t >= 0 and position[1] + t < len(grid) and position[0] + q >= 0 and position[0] + q < len(grid[0]):
                    if grid[position[1] + t][position[0] + q] == 0:
                        pos = (position[0] + q, position[1] + t)
                        neighbours.append(pos)

    return neighbours
 