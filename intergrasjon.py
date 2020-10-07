import math

def float_range(start, stop, steg):
    total = []
    while start < stop:
        total.append(start)
        start += steg
    return total

def intergral(func, a, b, n):
    areal = 0
    delta_x = (b-a)/n
    steg = (abs(a) + abs(b)) / n
    for x in float_range(a, b, steg):
        areal += func(x) * delta_x
    return areal

def volum(func, a, b, n):
    return math.pi * pow(intergral(func, a, b, n), 2)


def f(x):
    return x**2 - 2

print(4 << 2)
print(intergral(f, 2, 5, 1000000))




