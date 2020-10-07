import time
from a_star import find_path
import numpy as np

def makeEmptyGrid(x_len, y_len):
    grid = np.ones((x_len, y_len))
    grid[1:-1,1:-1] = 0
    return grid


def aStarTime():
    times = []

    for num in range(550, 800, 10):
        grid = makeEmptyGrid(num, num)
        start_pos = (1, 1)
        end_pos = (num-2, num-2)

        time_start = time.time()
        path = find_path(grid, start_pos, end_pos, False)
        time_end = time.time()

        times.append( time_end - time_start )

    return times


def benhmarker():
    times = aStarTime()

    # with open('temp/time_data.txt', 'w') as file:
    #    file.write('')

    with open('temp/time_data.txt', 'a') as file:
        for time in times:
            file.write(str(time) + '\n')
        file.close()


benhmarker()





