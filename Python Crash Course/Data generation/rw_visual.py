import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=3)
    plt.show()

    keep_running = input("Another one?(Y/n): ")
    if keep_running == 'n':
        break
