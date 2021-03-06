import matplotlib.pyplot as plt

x_values = range(0,1001)
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 1100, 0, 1100000])
plt.show()
