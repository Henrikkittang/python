import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

file_selector = input("1: last, 2: average  ")

if file_selector == "1":
    file = "cells_data.txt"
    delay = 100
else:
    file = "average_cells_data.txt"
    delay = 15000

def animate(i):
    graph_data = open(file, 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(int(x))
            ys.append(int(y))
    ax1.clear()
    ax1.plot(xs, ys)
    print(xs)


ani = animation.FuncAnimation(fig, animate, interval=delay)
plt.show()
