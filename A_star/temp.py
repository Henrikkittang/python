

def test():
    return [[0, 0], [2, 2], [3, 5]]


a = []
b = []
c = []
result = test()

(a, b, c) = result 
print(a)