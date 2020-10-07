from numpy import zeros, int16

files = []

with open("average/files_name.txt", "r") as f:
    graph_data = f.read()
    lines = graph_data.split('\n')
    for line in lines:
        files.append(line)
 
if files[-1] == "":
    files.pop()

ys_av = zeros(1500, dtype=int16)
xs = []

for i in range(0, 1500):
    xs.append(i)

for file in files:
    with open(file, "r") as f:
        graph_data = f.read()
        lines = graph_data.split('\n')
        index = 0
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                ys_av[index] += int(y)
                index += 1
        index = 0

ys_av = ys_av // len(files)


with open("average_cells_data.txt", "w") as f:
            for i in range(0, len(xs)):
                if ys_av[i] == 0:
                    break
                f.write(str(xs[i]) + "," + str(ys_av[i]))
                f.write("\n")
