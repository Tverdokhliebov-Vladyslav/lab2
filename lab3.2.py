import numpy as np
import numdifftools as nd

f = lambda x: 2*x**4 - 8*x**3 - 16*x**2 - 1

def nuton(a, b, eps, f):
    df2 = nd.Derivative(f, n=2)(b)  # Отримуємо значення похідної другого порядку в точці b
    if f(b) * df2 > 0:
        xi = b
    else:
        xi = a
    df = nd.Derivative(f, n=1)(xi)  # Отримуємо значення похідної першого порядку в точці xi
    xi_1 = xi - f(xi) / df
    while abs(xi_1 - xi) > eps:  # перевіряємо точність
        xi = xi_1
        xi_1 = xi - f(xi) / df
    print('Метод Ньютона, x = ', xi_1.round(4))

def komb(a, b, eps, f):
    if nd.Derivative(f, n=1)(a) * nd.Derivative(f, n=2)(a) > 0:
        a0 = a
        b0 = b
    else:
        a0 = b
        b0 = a
    ai = a0
    bi = b0
    while abs(ai - bi) > eps:
        ai_1 = ai - f(ai) * (bi - ai) / (f(bi) - f(ai))
        bi_1 = bi - f(bi) / nd.Derivative(f, n=1)(bi)
        ai = ai_1
        bi = bi_1
    x = (ai_1 + bi_1) / 2

    print('Комбінований метод, x = ', x.round(4))

if __name__ == "__main__":
    a1, b1 = -3, -2
    a2, b2 = 0, 1
    eps = 0.001
   
    print("Розв'язки на відрізку [-3, -2]")
    nuton(a1, b1, eps, f)
    komb(a1, b1, eps, f)
    print("\n Розв'язки на відрізку [0, 1]")
    nuton(a2, b2, eps, f)
    komb(a2, b2, eps, f)
