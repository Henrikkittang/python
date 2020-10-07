from math import sqrt


class Node(object):
    def __init__(self, position=None, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # distance from the starting node
        self.h = 0  # distance from end node
        self.f = 0  # h_cost + g_cost


def find_path(grid, start_pos, end_pos, diagonal=True):
    def calc_children(node):
        cur_pos = node.position
        children_pos = []
        for t in range(-1, 2):
            for q in range(-1, 2):
                if diagonal == False:
                    if abs(t) == abs(q):
                        continue

                if not (t == 0 and q == 0):
                    if grid[cur_pos[1] + t][cur_pos[0] + q] != 1:
                        pos = (cur_pos[0] + q, cur_pos[1] + t)
                        children_pos.append(pos)
        return children_pos

    open_nodes = []
    closed_nodes = []
    cur_node = Node(start_pos)
    end_node = Node(end_pos)
    open_nodes.append(cur_node)

    while cur_node.position != end_node.position:

        # Finds the open node with the lowest f-cost
        lowest_f = 1000
        for n in open_nodes:
            if n.f < lowest_f:
                cur_node = n
                lowest_f = n.f

        # if there aren't any paths, then exit and return none
        if len(open_nodes) == 0:
            return None

        # Finds the children of the current_node. Removes current_node from open and adds it to the closed
        children = calc_children(cur_node)
        open_nodes.remove(cur_node)
        closed_nodes.append(cur_node)

        # Loops over the current node`s children
        for pos in children:

            # if the child is in the closed list, then continue to the next child
            break_loop = False
            for closed_node in closed_nodes:
                if pos == closed_node.position:
                    break_loop = True
                    break
            if break_loop == True:
                continue

            child = Node(pos)

            # Sets the costs and the parent for the child
            child.g = cur_node.g + 1
            child.h = sqrt((end_node.position[0] - child.position[0])**2 + (end_node.position[1] - child.position[1])**2)
            child.f = child.g + child.h
            child.parent = cur_node

            # if the child is already in the open list, then continue to the next child
            break_loop = False
            for open_node in open_nodes:
                if child.position == open_node.position:
                    break_loop = True
                    break
            if break_loop == True:
                continue

            open_nodes.append(child)

    positions = []
    while cur_node != None:
        positions.append(cur_node.position)
        cur_node = cur_node.parent

    positions.reverse()
    return positions
