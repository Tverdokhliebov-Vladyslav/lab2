import math

x0 = 0.15
y0 = -2.1
epsilon = 0.001

def f1(y):
    return 2*x0 - math.cos(y + 1) # ваше перше рівняння
def f2(x):
    return -0.4 - math.sin(x0) # ваше друге рівняння

def проста_ітерація(x, y, e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while abs(xn1 - xn) >= e or abs(yn1 - yn) >= e:
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print('Проста ітерація:')
    print('x =', xn, '\ny =', yn, '\nКількість ітерацій =', n)

проста_ітерація(x0, y0, epsilon)
