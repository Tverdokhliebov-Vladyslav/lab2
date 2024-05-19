import numpy as np
import matplotlib.pyplot as plt

# Задані точки
x = np.array([0.01, 0.06, 0.11, 0.16, 0.21, 0.26, 0.31, 0.36, 0.41, 0.46, 0.51])
y = np.array([0.9918, 0.9519, 0.9136, 0.8769, 0.8416, 0.8077, 0.7753, 0.7441, 0.7141, 0.6854, 0.6579])

# Функція для обчислення інтерполяційного багаточлена Ньютона
def newton_interpolation(x, y, x0):
    n = len(x)
    f = np.zeros((n, n))
    f[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            f[i, j] = (f[i + 1, j - 1] - f[i, j - 1]) / (x[i + j] - x[i])
    
    ans = f[0, 0]
    for j in range(1, n):
        term = f[0, j]
        for i in range(j):
            term *= (x0 - x[i])
        ans += term
    
    return ans

# Обчислення значень функції в заданих точках
x1 = 0.027
x2 = 0.416
y1 = newton_interpolation(x, y, x1)
y2 = newton_interpolation(x, y, x2)

print(f"f({x1}) = {y1}")
print(f"f({x2}) = {y2}")

# Побудова графіку інтерполяційної функції
xx = np.linspace(np.min(x), np.max(x), 100)
yy = np.array([newton_interpolation(x, y, xi) for xi in xx])

plt.plot(x, y, 'o', label='Дані точки')
plt.plot(xx, yy, label='Інтерполяційна функція Ньютона')
plt.plot(x1, y1, 'o', label=f'({x1}, {y1})')
plt.plot(x2, y2, 'o', label=f'({x2}, {y2})')
plt.title("Графік інтерполяційної функції Ньютона")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
