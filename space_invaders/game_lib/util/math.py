import math

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    ''' 
        Uses Pytagoras theorom to compute the distance between two points
    '''
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def lerp(a: float, b: float, t: float) -> float:
    ''' 
        Linear interpolation between the values of a and b  
        given the percentage t
    '''
    return a + (b-a)*t

def derivation(func: callable, x: float, dx: float=0.01):
    ''' 
        Compute the difference formula for f'(x) with step size dx.
        Using central derivation method f(x+dx) - f(x-dx))/2dx
    '''
    return (func(x + dx) - func(x - dx) ) / (2*dx)


def intergrate(func: callable, a: float, b: float, dx: float=0.001):
    ''' 
        Compute the area under f with step size dx
        in range of a to b
    '''
    xn = a
    sum_ = 0
    while xn <= b:
        sum_ += func(xn)*dx
        xn += dx
    return sum_

def intergrate3D(func: callable, a: float, b: float, n: float=0.001) -> float:
    ''' 
        Intergration in 3D space
    '''
    return math.pi * (intergrate(func, a, b, n))**2


def float_range(start: float, stop: float=None, step: float=1.0) -> iter:
    '''  
        Similar to the built-in range function, but step can be a float
        and the results are always floats
    '''
    if stop is None:
        stop = start 
        start = 0
    for x in range(int((stop-start)/step)):
        yield start + round(x / step**(-1), 15)


def gridToPixel(x: int, y: int, scaleX: int, scaleY: int=None) -> tuple:
    if scaleY is None: scaleY = scaleX
    return (x*scaleX, y*scaleY)

def pixelToGrid(x: float, y: float, scaleX: int, scaleY: int=None) -> tuple:
    if scaleY is None: scaleY = scaleX
    return (int(x/scaleX), int(y/scaleY))

def createUniqe(a: int, b: int) -> int:
    ''' 
        Uses Cantors pairing algorithm to generate a unique interger
        from two intergers. Works only for intergers
    '''
    return  (a + b)*(a + b + 1)/2 + b;


def rotationR(x: float, y: float) -> float:
    return math.atan2(y, x) 
def rotationD(x: float, y: float) -> float:
    return math.degrees( rotationR(x, y) )

