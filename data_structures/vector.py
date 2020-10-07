import math
import time


# Missing: point to line dist, line to line dist, 

class Point3():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        string = '({}, {}, {})'
        return string.format(self.x, self.y, self.z)

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        string = '[{}, {}, {}]'
        return string.format(self.x, self.y, self.z)
 
    def __add__(self, vect):
        return Vector3(self.x + vect.x, self.y + vect.y, self.z + vect.z)
    
    def __sub__(self, vect):
        return Vector3(self.x - vect.x, self.y - vect.y, self.z - vect.z)

    def __mul__(self, vect):
        # dot product
        return self.x*vect.x + self.y*vect.y + self.z*vect.z # vect * vect

    def __mod__(self, vect):
        # cross product
        return Vector3(
            self.y*vect.z - self.z*vect.y,
            self.z*vect.x - self.x*vect.z,
            self.x*vect.y - self.y*vect.x
        )

    def __abs__(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def lenght(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def factor(scalar):
        return Vector3(self.x*scalar, self.y*scalar, self.z*scalar)

    def angleR(self, vect):
        dotProd = self * vect
        lenProd = self.lenght() * vect.lenght()

        return math.acos(dotProd/lenProd)
    
    def angleD(self, vect):
        return math.degrees(self.angleR(vect))

def makeVector3(p1, p2):
    return Vector3(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)


class Line3():
    def __init__(self, point, vector):
        self.point = point
        self.rVect = vector

    def distToPoint(self, Q):
        PQvect = makeVector3(self.point, Q)
        h = abs(PQvect % self.rVect) / abs(self.rVect)

    def getPoint(self, t):
        x = self.point.x + self.rVect.x*t
        y = self.point.y + self.rVect.y*t
        z = self.point.z + self.rVect.z*t
        return Point3(x, y, z)


class Triangle3():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        self.ab = makeVector3(a, b)
        self.ac = makeVector3(a, c)
        self.bc = makeVector3(b, c)

        print(self.ab, self.ac, self.bc)

        nVect = self.ab % self.ac

    def areal(self):
        return self.nVect.lenght() / 2

class Matrix3():
    def __init__(self, x, y, z):
        # matrix[x][y][x] -> matriz[z][y][x]

        self.matrix = []
        for i in range(z):
            self.matrix.append([])
            for j in range(y):  
                self.matrix[i].append([])
                for q in range(x):
                    self.matrix[i][j].append(0)


m = Matrix3(3, 3, 3)

t = Triangle3(Point3(1, 2, 3), Point3(4, 2, 7), Point3(-4, 2, 9))



