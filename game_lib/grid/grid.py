


class GridWrapper(object):
    def __init__(self, width: int=0, height: int=0):
        self._grid: list = []
        self.makeGrid(width, height)

    def __repr__(self):
        return '\n'.join(str(x) for x in self._grid)

    def __iter__(self):
        for column in range(self.height):
            for row in range(self.width):
                yield (row, column)

    @property
    def width(self): return len(self.grid[0])
    @property
    def height(self): return len(self.grid)
    @property
    def grid(self): return self._grid

    @staticmethod
    def generateGrid(width: int, height: int, defualtValue: any=0) -> list:
        return [[defualtValue for i in range(height)] for j in range(width)] 

    def makeGrid(self, width: int, height: int, defualtValue: any=0) -> None:
        self._grid = [[defualtValue for i in range(height)] for j in range(width)] 

    def getValue(self, row, column) -> any:
        try: return self._grid[column][row]
        except IndexError: return None
    def setValue(self, row: int, column: int, value: any) -> None:
        try: self._grid[column][row] = value
        except IndexError: pass

    def setValues(self, positions:list, value: any) -> None:
        [self.setValue(*pos, value) for pos in positions]
    
    def isOpen(self, row: int, column:int, value=0) -> bool:
        return bool( self.getValue(row, column) == value )
    def isClosed(self, row: int, column:int, value=1) -> bool:
        return self.isOpen(row, column, value)

    def outOfBounds(self, row: int, column: int) -> bool:
        if row >= 0 and row < self.width:
            if column >= 0 and column < self.height:
                return False
        return True

    def findNeighboursPos(self, row, column):
        neighbours = []
        for c in range(column-1, column+2):
            for r in range(row-1, row+2):
                if (c == column and r == row):
                    continue
                
                if not self.outOfBounds(r, c):
                    neighbours.append((r, c))
        return neighbours





