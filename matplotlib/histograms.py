import matplotlib.pyplot as plt

ages = [22, 55, 54, 34, 23, 79, 32, 89, 65, 76, 81, 32, 99, 102, 54, 32, 78, 57, 65, 43, 90, 103]

# ids = [x for x in range(len(ages))]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(ages, bins, histtype="line", rwidth=0.8)

plt.xlabel("x")
plt.ylabel("y")

plt.title("Interesting Graph\nCheck it out")
plt.legend()
plt.show()
