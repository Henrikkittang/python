
class hash_table(object):
    def __init__(self, size):
        self.size = size
        self.arr = [None] * self.size
        self.iter_index = -1

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __iter__(self):
        return self

    def __next__(self):
        self.iter_index += 1
        if self.iter_index == self.size:
            self.iter_index = -1
            raise StopIteration
        return self.arr[self.iter_index][1]

    def __repr__(self):
        content = ""
        for i in self.arr:
            if i != None:
                content += str(i[1]) + ", "
        return content

    def _hash_function(self, key):
        chars = list(key)
        ascii_val = 0
        for i in chars:
            ascii_val += ord(i)
        index = ascii_val % self.size
        return index

    def add(self, key, value):
        index = self._hash_function(key)
        pair = [key, value]
        for i in range(index, self.size):
            if self.arr[i] == None:
                self.arr[i] = pair
                return
        print("Not enough space in list, items not added")

    def remove(self, key):
        index = self._hash_function(key)
        for i in range(index, self.size):
            if self.arr[i] != None:
                if self.arr[i][0] == key:
                    self.arr[i] = None
                    return
        print("Key not in list")

    def get(self, key):
        index = self._hash_function(key)
        for i in range(index, self.size):
            if self.arr[i] != None:
                if self.arr[i][0] == key:
                    return self.arr[i][1]
        print("Key not in list")

    def set(self, key, new_val):
        index = self._hash_function(key)
        for i in range(index, self.size):
            if self.arr[i] != None:
                if self.arr[i][0] == key:
                    self.arr[i][1] = new_val
                    return
        print("Key not in list")

