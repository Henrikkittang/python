# distutils: language = c++
# distutils: sources = adder.cpp

from libcpp.vector cimport vector

cdef extern from 'src/vector.cpp':
    double average(vector[double])


cpdef double avg(list a):
    return average(a)

