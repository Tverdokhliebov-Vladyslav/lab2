import numpy as np
import matplotlib.pyplot as plt

def f1(x, y):
    return 2*x - np.cos(y + 1)

def f2(x, y):
    return y + np.sin(x) + 0.4

x_values = np.linspace(-2, 2, 400)
y_values = np.linspace(-2, 2, 400)

X, Y = np.meshgrid(x_values, y_values)
Z1 = f1(X, Y)
Z2 = f2(X, Y)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.contour(X, Y, Z1, levels=[0], colors='r')
plt.title('Contour plot of 2x - cos(y + 1) = 0')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(1, 2, 2)
plt.contour(X, Y, Z2, levels=[0], colors='b')
plt.title('Contour plot of y + sin(x) = -0.4')
plt.xlabel('x')
plt.ylabel('y')

plt.tight_layout()
plt.show()
