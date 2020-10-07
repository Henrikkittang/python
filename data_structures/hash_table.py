
class node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list(object):
    def __init__(self, vals=None):
        self.head = node()
        self.tail = self.head
        self.list_length = 0
        self.iter_index = -1
        self.iter_node = self.head

        if vals != None:
            self.create(vals)

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, data):
        self.set(data, index)

    def __iter__(self):
        return self

    def __next__(self):
        self.iter_index += 1
        if self.iter_index == self.list_length:
            self.iter_index = -1
            self.iter_node = self.head
            raise StopIteration
        self.iter_node = self.iter_node.next
        return self.iter_node.data

    def create(self, vals):
        for i in vals:
            self.append(i)

    def append(self, data):
        new_node = node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.list_length += 1

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index, mode=None):
        if index >= self.list_length or index < self.list_length * -1:
            raise IndexError
        if index == self.list_length - 1 or index == -1:
            if mode == "n":
                return self.tail
            return self.tail.data
        cur_idx = 0
        if index < -1:
            cur_idx = self.list_length * -1
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                if mode == "n":
                    return cur_node
                return cur_node.data
            cur_idx += 1

    def set(self, data, index):
        if index >= self.list_length or index < self.list_length * -1:
            raise IndexError
        if index == -1 or index == self.list_length:
            self.tail.data = data
            return
        cur_idx = 0
        if index < -1:
            cur_idx = self.list_length * -1
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                cur_node.data = data
                return
            cur_idx += 1

    def remove(self, data):
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_node.data == data:
                last_node.next = cur_node.next
                if last_node.next == None:
                    self.tail = last_node
                self.list_length -= 1
                return


class hash_tabel(object):
    def __init__(self, size):
        self.size = size
        self.arr = [None] * self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __repr__(self):
        content = ""
        for i in self.arr:
            if i != None:
                for q in i:
                    content += str(q[1]) + ", "
        return content

    def _hash_function(self, key):
        chars = list(key)
        index = 0
        for i in chars:
            index += ord(i)
        return index % self.size

    def add(self, key, value):
        index = self._hash_function(key)
        pair = [key, value]
        if self.arr[index] == None:
            ll = linked_list([pair])
            self.arr[index] = ll
        else:
            self.arr[index].append(pair)

    def remove(self, key):
        index = self._hash_function(key)
        if self.arr[index] != None:
            if self.arr[index].list_length == 1:
                self.arr[index] = None
            else:
                for i in self.arr[index]:
                    if i[0] == key:
                        val = i
                self.arr[index].remove(val)

    def get(self, key):
        index = self._hash_function(key)
        val = None
        if self.arr[index] != None:
            for i in self.arr[index]:
                if i[0] == key:
                    val = i[1]
        return val

    def set(self, key, new_value):
        index = self._hash_function(key)
        if self.arr[index] != None:
            for i in self.arr[index]:
                if i[0] == key:
                    i[1] = new_value
