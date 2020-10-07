import math


class Vector():
    def __init__(self, exp):
        self.exp = list(exp)
        self.len = self._length()

    def __repr__(self):
        string = str(self.exp)
        return string

    def __add__(self, vector):
        new_vect = [self.exp[0] + vector.exp[0], self.exp[1] + vector.exp[1]]
        return new_vect

    def __sub__(self, vector):

        rev_vect = self._reverse()
        new_vect = [rev_vect[0] + vector.exp[0], rev_vect[1] + vector.exp[1]]
        return new_vect

    def __mul__(self, vector):
        scalar = (self.exp[0] * vector.exp[0]) + (self.exp[1] * vector.exp[1])
        return scalar

    def _length(self):
        len = math.sqrt(math.pow(self.exp[0], 2) + math.pow(self.exp[1], 2))
        return len

    def _reverse(self):
        new_vect = [self.exp[0] * (-1), self.exp[1] * (-1)]
        return new_vect

    def reverse(self):
        self.exp[0] *= (-1)
        self.exp[1] *= (-1)
        return

    def angle(self, vector):
        scalar = self * vector
        len_prod = self.len * vector.len
        angle = math.degrees(math.acos((scalar/len_prod)))
        return angle


a = Vector([1, 5])
b = Vector([4, 3])

