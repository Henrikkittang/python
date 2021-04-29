import math

class Vector(object):
    ''' 
        Vector class for doing vector math in 2d space    
    '''

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y  

    def __repr__(self) -> str:
        return '[{}, {}]'.format(self.x, self.y)
 
    def __add__(self, vect: object) -> object:
        return Vector(self.x + vect.x, self.y + vect.y)
    
    def __sub__(self, vect: object) -> object:
        return Vector(self.x - vect.x, self.y - vect.y)

    def __mul__(self, vect: object) -> float:
        return self.x*vect.x + self.y*vect.y # dot product

    def __abs__(self):
        return self.length

    def __iter__(self):
        yield self.x; yield self.y

    @property
    def length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def extend(self, scalar: float) -> None:
        self.x *= scalar
        self.y *= scalar

    def unit(self) -> object:
        return Vector(self.x / self.lenght, self.y/self.lenght)    

    def angleR(self, vect):
        dotProd = self * vect
        lenProd = self.length * vect.length

        return math.acos(dotProd/lenProd)
    
    def angleD(self, vect):
        return math.degrees(self.angleR(vect))

    def rotationR(self):
        return math.atan2(self.y, self.x)  
    def rotationD(self):
        return math.degrees(self.rotationR())

