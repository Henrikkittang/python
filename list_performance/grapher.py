import matplotlib.pyplot as plt
import numpy as np
import json

with open("test.json") as f:
    data = json.load(f)
    f.close()

ops = []
single = []
double = []
built_in = []
lists = {"single": single, "double": double, "built_in": built_in}
for key, value in data.items():
    ops.append(key)
    for i, q in value.items():
        if i != "elems":
            lists[i].append(q)


xpos = np.arange(len(ops))

plt.bar(xpos - 0.2, single, width=0.2, label="Single")
plt.bar(xpos + 0.2, double, width=0.2, label="Double")
plt.bar(xpos, built_in, width=0.2, label="Built-in")


plt.xticks(xpos, ops)
plt.ylabel("Time")
plt.title("List performance")
plt.legend()
plt.show()
