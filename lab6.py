import numpy as np
import matplotlib.pyplot as plt

def lagrange_polynomial(xi, i, x):
    result = 1
    for j in range(len(xi)):
        if j != i:
            result *= (x - xi[j]) / (xi[i] - xi[j])
    return result

def lagrange_interpolation(xi, yi, x):
    result = 0
    for i in range(len(xi)):
        result += yi[i] * lagrange_polynomial(xi, i, x)
    return result

xi = [-3, -1, 1, 2]
yi = [3, 3, -13, -12]

x_values = np.linspace(min(xi), max(xi), 400)
y_values = [lagrange_interpolation(xi, yi, x) for x in x_values]

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="Interpolation")
plt.scatter(xi, yi, color='red', label="Given points")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolation Polynomial')
plt.legend()
plt.grid(True)
plt.show()



def lagrange_polynomial(xi, i, x):
    result = 1
    for j in range(len(xi)):
        if j != i:
            result *= (x - xi[j]) / (xi[i] - xi[j])
    return result

def lagrange_interpolation(xi, yi, x):
    result = 0
    for i in range(len(xi)):
        result += yi[i] * lagrange_polynomial(xi, i, x)
    return result

xi = [-3, -1, 1, 2]
yi = [3, 3, -13, -12]

x_values = [-4, -2, -1.5, 0.5]

# Обчислимо значення функції в заданих точках
interpolated_values = [lagrange_interpolation(xi, yi, x) for x in x_values]

for x, y in zip(x_values, interpolated_values):
    print(f"f({x}) ≈ {y}")

