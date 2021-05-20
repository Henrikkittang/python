from heapq import heappush, heappop
from math import sqrt


class Node(object):
    def __init__(self, position: tuple=None, parent=None):
        self.position: tuple = position
        self.parent: Node = parent
        self.g: float = 0  # distance from the starting node
        self.h: float = 0  # distance from the end node
        self.f: float = 0  # h_cost + g_cost
    
    def __lt__(self, other):
        return self.f < other.f


class Pathfinding(object):
    def __init__(self, grid: list, start: tuple, end: tuple, diagonal:bool=True):
        self._grid    :list  = grid
        self._start   :tuple = start
        self._end     :tuple = end
        self._diagonal:bool  = diagonal


    def euclidean(self, pos1: int, pos2: int) -> float:
        return sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2)

    def manhatten(self, pos1: tuple, pos2: tuple) -> int:
        return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])

    def outOfBounds(self, row: int, column: int) -> bool:
        if row >= 0 and row < len(self._grid[0]):
            if column >= 0 and column < len(self._grid):
                return False
        return True
        
    def findNeighbours(self, cur_pos: tuple) -> iter:
        row, column = cur_pos
        for t in range(-1, 2):
            for q in range(-1, 2):
                if not self._diagonal and abs(t) == abs(q):
                    continue

                if (t != 0 or q != 0) and not self.outOfBounds(row+q, column+t):
                    if self._grid[column + t][row + q] == 0:
                        yield (row + q, column + t)

    def traversePath(self, node: Node) -> list:
        positions = [] 
        while node is not None:
            positions.append(node.position)
            node = node.parent
        return positions

    def bfs(self) -> list:
        cur_node = Node(self._start)

        open_queue = [cur_node]
        closed_set = set()

        while cur_node.position != self._end:
            if len(open_queue) == 0: return None

            cur_node = open_queue.pop(0)
            closed_set.add(cur_node.position)
            neighbours = self.findNeighbours(cur_node.position)

            if len(neighbours) == 0:
                open_queue.pop(0)

            for neighbour in neighbours:
                if neighbour not in closed_set:
                    open_queue.append(neighbour)
 
        return self.traversePath(cur_node)

    def dfs(self) -> list:
        
        cur_node = Node(self._start)

        open_stack = [cur_node]
        closed_set = set()

        while cur_node.position != self._end:
            if len(open_stack) == 0: return None
            cur_node = open_stack.pop()
            closed_set.add(cur_node.position)
            neighbours = self.findNeighbours(cur_node.position)

            if len(neighbours) == 0:
                open_stack.pop(0)

            for neighbour in neighbours:
                if neighbour not in closed_set:
                    open_stack.append(neighbour)
 
        return self.traversePath(cur_node)
        
    def AStar(self, heuristicWeight: float=1.0) -> list:
        ''' 
            Switches between euclidean and manhatten distance based on wether it can
            travel digagonally. A heuristicWeight of 0 effectivly makes the algorithm
            behave like Dijkstra and a heuristicWeight of infinity makes it a greedy best first
            search. Returns a empty list if no path is found
        '''


        heuristic = self.euclidean if self._diagonal else self.manhatten

        cur_node = Node(self._start)

        open_nodes = [cur_node]
        open_set = set([self._start])
        closed_set = set()

        while cur_node.position != self._end:
            if len(open_nodes) == 0:
                return []

            cur_node = heappop(open_nodes)
            open_set.remove(cur_node.position)

            # Finds the children of the current_node. Removes current_node from open and adds it to the closed
            neighbours = self.findNeighbours(cur_node.position)
            closed_set.add(cur_node.position)

            # Loops over the current node`s children
            for neighbour in neighbours:
                # Both are dictonaries and have fast lookup of nodes
                if (neighbour in closed_set) or (neighbour in open_set):
                    continue

                # Sets the costs and the parent for the child
                child = Node(neighbour, cur_node)
                child.g = cur_node.g + 1
                child.h = heuristic(neighbour, self._end) * heuristicWeight
                child.f = child.g + child.h

                heappush(open_nodes, child)
                open_set.add(child.position)
                
        return self.traversePath(cur_node)



