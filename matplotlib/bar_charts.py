import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [5, 6, 7, 3, 8]

x2 = [1,3,5,7,9]
y2 = [7,8,4,2,1]

plt.bar(x, y, label="Bar_1", color="red")
plt.bar(x2, y2, label="Bar_2", color="cyan")

plt.xlabel("x")
plt.ylabel("y")

plt.title("Interesting Graph\nCheck it out")
plt.legend()
plt.show()
