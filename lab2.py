import numpy as np
import numdifftools as nd

def f(x):
    return 2*pow(x, 4) - 8*pow(x, 3) - 16*pow(x, 2) - 1

eps = 0.0001

def find_segments(): 
    search_range = np.arange(-10, 10, 1)
    
    a = None
    previous_x = None
    current_x = None
    segments = []

    for x in search_range:
        x = round(x, 4)
        current_x = f(x)
        if previous_x is not None and previous_x * current_x < 0:
            segments.append((a, x))
        a = x
        previous_x = current_x
    return segments

segments = find_segments()
for a, b in segments:
    print(f'Знайдений сегмент: [{a}, {b}]')

def rec(a, b, eps): 
    while abs(a - b) > eps:
        if f(a) * f((a + b) / 2) < 0:
            b = (a + b) / 2
        else:
            a = (a + b) / 2
    x = (a + b) / 2
    print('x= ', round(x, 5), ' - Метод ділення навпіл')

def hord(a, b, eps): 
    if f(a) * f(b) > 0:
        print("Не можливо застосувати метод хорд, однакові знаки на обох кінцях сегмента.")
        return
    derivative_f = nd.Derivative(f, n=1)
    if f(a) * derivative_f(a) > 0:
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a
    xi_1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0) + 1e-10)
    while abs(xi_1 - xi) > eps:
        xi = xi_1
        xi_1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0) + 1e-10)
    print('x= ', round(xi_1, 5), ' - Метод хорд')

a = -2 
b = -1
a1 = 1.
b1 = 2.

print (f'Розв\'язок нелінійного рівняння на сегменті [{a}, {b}]')
rec(a, b, eps) 
if f(a) * f(b) < 0:
    hord(a, b, eps) 
print (f'Розв\'язок нелінійного рівняння на сегменті [{a1}, {b1}]')
rec(a1, b1, eps) 
if f(a1) * f(b1) < 0:
    hord(a1, b1, eps)
