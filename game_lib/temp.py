from grid.grid import GridWrapper
from algorithms.pathfinding import Pathfinding
from util.profiler import meanTime


size = 10

g = GridWrapper.generateGrid(size, size)


p = Pathfinding(g, (0, 0), (size-1, size-1))

path = meanTime(1)(p.AStar)()
print(path)