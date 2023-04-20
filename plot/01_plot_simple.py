import matplotlib.pyplot as plt

X = [ x for x in range(1, 100)]
Y = [ 1/x for x in range(1, 100)]

plt.plot(X,Y)
plt.grid()
plt.show()