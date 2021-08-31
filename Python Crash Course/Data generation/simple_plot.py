import matplotlib.pyplot as plot

fib = [0,1,1,2,3,5,8,13,21,34,55,89]
plot.plot(fib, linewidth = 5)
plot.title("Fibonacci Sequence", fontsize=24)
plot.xlabel("Value", fontsize = 14)
plot.tick_params(axis='both', labelsize=14)
plot.show()
