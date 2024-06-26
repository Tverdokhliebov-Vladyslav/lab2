import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial

# Задаємо символьну змінну x та функцію f(x)
x = sp.symbols('x')
f = sp.sin(2*x) + x

# Знаходимо перші три похідні
f1 = sp.diff(f, x)
f2 = sp.diff(f1, x)
f3 = sp.diff(f2, x)

# Виводимо похідні
print("f'(x) =", f1)
print("f''(x) =", f2)
print("f'''(x) =", f3)


# Значення функції та похідних у точці x = 0
x0 = 0
f_x0 = f.subs(x, x0).evalf()
f1_x0 = f1.subs(x, x0).evalf()
f2_x0 = f2.subs(x, x0).evalf()
f3_x0 = f3.subs(x, x0).evalf()

# Многочлен Тейлора
T = f_x0 + f1_x0 * (x - x0) + (f2_x0 / 2) * (x - x0)**2 + (f3_x0 / 6) * (x - x0)**3

print("f(0) =", f_x0)
print("T(x) =", T.evalf())


# Графік функції та наближення
x_vals = np.linspace(-2, 2, 1000)
f_vals = np.array([f.subs(x, xi).evalf() for xi in x_vals])
T_vals = np.array([T.subs(x, xi).evalf() for xi in x_vals])

fig, ax = plt.subplots()
ax.plot(x_vals, f_vals, label="f(x)")
ax.plot(x_vals, T_vals, label="T(x)")
ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Графік функції та наближення многочленом Тейлора")
plt.grid(True)
plt.show()


# Побудова багаточлена Тейлора за допомогою approximate_taylor_polynomial
def f_numeric(x):
    return np.sin(2*x) + x

x_vals = np.linspace(-2.0, 2.0, 400)
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_numeric(x_vals), label="f(x)", color='blue')
degree = 3
taylor = approximate_taylor_polynomial(f_numeric, 0, degree, 1)

plt.plot(x_vals, taylor(x_vals), label=f"degree={degree}", color='red', linestyle='--')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.0, shadow=True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графік функції та наближення багаточленами Тейлора")
plt.tight_layout()
plt.grid()
plt.show()

