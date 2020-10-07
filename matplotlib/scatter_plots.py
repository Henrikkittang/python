import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [4,5,6,3,8,3,6,2,1]

plt.scatter(x, y, label="skitscat", color="black", marker="*", s=100)

plt.xlabel("x")
plt.ylabel("y")

plt.title("Interesting Graph\nCheck it out")
plt.legend()
plt.show()
