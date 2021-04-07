from heapq import heappush, heappop
from math import sqrt

class Node(object):
    def __init__(self, position=None, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # distance from the starting node
        self.h = 0  # distance from end node
        self.f = 0  # h_cost + g_cost
    
    def __lt__(self, other):
        return self.f < other.f

def calc_children(node: Node, grid: list):
    cur_pos = node.position
    children_pos = []
    for t in range(-1, 2):
        for q in range(-1, 2):
            if abs(t) == abs(q):
                continue

            if t != 0 or q != 0:
                if cur_pos[1] + t >= 0 and cur_pos[1] + t < len(grid) and cur_pos[0] + q >= 0 and cur_pos[0] + q < len(grid[0]):
                    if grid[cur_pos[1] + t][cur_pos[0] + q] == 0:
                        pos = (cur_pos[0] + q, cur_pos[1] + t)
                        children_pos.append(pos)

    return children_pos
 

def find_path(grid: list, start_pos: tuple, end_pos: tuple) -> list:
    cur_node = Node(start_pos)

    open_nodes = [cur_node]
    open_set = set([start_pos])
    closed_set = set()


    while cur_node.position != end_pos:
        if len(open_nodes) == 0:
            return None

        cur_node = heappop(open_nodes)
        open_set.discard(cur_node.position)

        # Finds the children of the current_node. Removes current_node from open and adds it to the closed
        childrenPos = calc_children(cur_node, grid)
        closed_set.add(cur_node.position)

        # Loops over the current node`s children
        for childPos in childrenPos:
            # Both are dictonaries and have fast lookup of positions
            if (childPos in closed_set) or (childPos in open_set):
                continue

            # Sets the costs and the parent for the child
            child = Node(childPos, cur_node)
            child.g = cur_node.g + 1
            # child.h = sqrt((end_pos[0] - child.position[0])**2 + (end_pos[1] - child.position[1])**2)
            child.h = abs(end_pos[0] -  child.position[0]) + abs(end_pos[1] -  child.position[1])
            child.f = child.g + child.h

            heappush(open_nodes, child)
            open_set.add(child.position)
            
    positions = []
    while cur_node != None:
        positions.append(cur_node.position)
        cur_node = cur_node.parent

    return positions
