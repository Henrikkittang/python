import matplotlib.pyplot as plt

plt.style.use('seaborn')

def read_csv(filename):
    dates = []
    infected = []

    with open(filename + '.csv', 'r') as csv_file:
        lines = csv_file.read().split('\n')
        if lines[-1] == '': lines.pop()
        lines.pop(0)

        for line in lines:
            line = line.split(';')
            dates.append(line[0])
            infected.append(int(line[1]))
 
    return dates, infected

# 4 * x = 6, x = 6 / 4

def getProsents(arr):
    prosents = [0]
    for idx, item in enumerate(arr):
        if idx == len(arr) - 1: break
        prosent = ((arr[idx+1] / item) - 1) * 100
        prosents.append(prosent)
    return prosents

dates, infected = read_csv('totalt-smittede')
prosents = getProsents(infected)

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

ax1.plot(dates, infected, color='green')
ax1.set_xlabel('Dato')
ax1.set_ylabel('Smittede')
ax1.set_title('Antall smittede i Norge')

ax2.plot(dates, prosents, color='blue')
ax2.set_xlabel('Dato')
ax2.set_ylabel('Smittede endring')
ax2.set_title('Antall smitted(endring) Norge')

plt.tight_layout()
plt.show()


