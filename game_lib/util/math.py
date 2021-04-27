import math

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def lerp(a: float, b: float, t: float) -> float:
    return a + (b-a)*t

# def derivation(func, x, dx=0.0001):
#     return round( ( func(x + dx) - f(x) ) / dx, abs(int(math.log10(dx))) )

def derivation(func: callable, x, dx=0.0001):
    return (func(x + dx) - func(x) ) / dx

def intergrate(f, a, b, dx=0.001):
    i = a
    s = 0
    while i <= b:
        s += f(i)*dx
        i += dx
    return s

def intergrate3D(func, a, b, n):
    return math.pi * (intergrate(func, a, b, n))**2


def float_range(start: float, stop: float, step: float) -> iter:
    for x in range(int((stop-start)/step)+1):
        yield x / pow(step, -1)

# def intergrate(func: callable, a: float, b: float, n: int=10) -> float:
#     s = 0
#     steps = (b-a)/n
#     for i in float_range(a, b, steps):
#         s += func(i) * steps
#     return s

def gridToPixel(x: int, y: int, scale: int) -> tuple:
    return (x*scale, y*scale)

def pixelToGrid(x: float, y: float, scale: int) -> tuple:
    return (int(x/scale), int(y/scale))

