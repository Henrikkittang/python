
def calc_children(a_grid, a_parent_pos):
    """Finds the blank tiles around a open tile"""
    children_pos = []
    for t in range(-1, 2):
        for q in range(-1, 2):
            if abs(t) == abs(q):
                continue

            if not (t == 0 and q == 0):
                try:
                    if a_grid[a_parent_pos[1] + t][a_parent_pos[0] + q] == 0:
                        pos = (a_parent_pos[0] + q, a_parent_pos[1] + t)
                        children_pos.append(pos)
                except IndexError:
                    continue
    return children_pos

def find_open(a_grid, a_start_pos):
    open_pos = set()
    closed_pos = set()
    free_pos = []
    open_pos.add(a_start_pos)
    while len(open_pos) > 0:
        cur_pos = open_pos.pop() # poping
        closed_pos.add(cur_pos) # adding
        children = calc_children(a_grid, cur_pos) # Find the surrounding nodes

        for child in children:
            # checks if the position is already discovered
            if (child in closed_pos) or (child in open_pos):
                continue

            open_pos.add(child) # adding new pos
            free_pos.append(child) # appending new pos

    return free_pos
