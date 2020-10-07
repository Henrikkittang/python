import time
import json


with open("test.json") as f:
    data = json.load(f)


class Node_ll(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list(object):
    def __init__(self, vals=None):
        self.head = Node_ll()
        self.tail = self.head
        self.list_length = 0
        self.iter_index = -1
        self.Node_ll = self.head

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

    def __repr__(self):
        cur_node = self.head
        if cur_node.next == None:
            return "Empty"
        list_content = ""
        while cur_node.next != None:
            cur_node = cur_node.next
            list_content += str(cur_node.data) + ", "
        return list_content

    def create(self, vals):
        for i in vals:
            self.append(i)

    def append(self, data):
        new_node = Node_ll(data)
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

    def pop(self, index):
        if index >= self.list_length:
            raise IndexError
        elif index < 0:
            index = self.list_length + index
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                if last_node.next == None:
                    self.tail = last_node
                self.list_length -= 1
                return
            cur_idx += 1

    def insert(self, data, index):
        if index >= self.list_length or index < 0:
            raise IndexError
        if index == self.list_length - 1:
            self.append(data)
            return
        cur_idx = 0
        cur_node = self.head
        new_node = Node_ll(data)
        last_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = new_node
                new_node.next = cur_node
                self.list_length += 1
                return
            last_node = cur_node
            cur_idx += 1

    def merge(self, new_list):
        self.tail.next = new_list.get(0, "n")
        self.tail = new_list.tail
        self.list_length += new_list.list_length

    def clear(self):
        cur_node = self.head
        cur_node.next = None
        self.tail = self.head
        self.list_length = 0

    def index(self, data):
        cur_idx = 0
        cur_node = self.head
        while cur_idx < self.list_length:
            cur_node = cur_node.next
            if cur_node.data == data:
                return cur_idx
            cur_idx += 1

    def count(self, data):
        apperans = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_node.data == data:
                apperans += 1
            if cur_node.next == None:
                return apperans

    def copy(self):
        cur_node = self.head
        new_list = linked_list()
        while True:
            cur_node = cur_node.next
            new_list.append(cur_node.data)
            if cur_node.next == None:
                break
        return new_list


class node():
    def __init__(self, data=None):
        self.next = None
        self.prev = None
        self.data = data

class doubly_linked_list():
    def __init__(self, content=None):
        self.head = node()
        self.tail = self.head
        self.list_length = 0
        self.iter_index = -1
        self.iter_node = self.head

        if content != None:
            for i in content:
                self.append(i)

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, index, data):
        return self.set(data, index)

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

    def __repr__(self):
        cur_node = self.head
        if cur_node.next == None:
            return "Empty"
        list_content = ""
        while cur_node.next != None:
            cur_node = cur_node.next
            list_content += str(cur_node.data) + ", "
        return list_content

    def append(self, data):
        new_node = node(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.list_length += 1

    def pop(self, index=None):
        if index == None:
            self.tail = self.tail.prev
            self.tail.next = None
        elif index < 0:
            index = self.list_length + index
            if index == self.list_length + 1:
                self.tail = self.tail.prev
                self.tail.next = None
        elif index >= self.list_length or index < 0:
            raise IndexError
        elif index == 0 or self.list_length // index >= 2:
            self._front_pop(index)
        else:
            self._back_pop(index)
        self.list_length -= 1

    def _front_pop(self, index):
        if self.list_length == 1:
            self.head.next = None
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                prev_node = cur_node.prev
                next_node = cur_node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                if cur_node.next == None:
                    self.tail = prev_node
                return
            cur_idx += 1

    def _back_pop(self, index):
        cur_idx = self.list_length - 1
        cur_node = self.tail
        while True:
            if cur_idx == index:
                prev_node = cur_node.prev
                next_node = cur_node.next
                prev_node.next = next_node
                if cur_node != self.tail:
                    next_node.prev = prev_node
                else:
                    self.tail = prev_node
                return
            cur_idx -= 1
            cur_node = cur_node.prev

    def remove(self, data):
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_node.data == data:
                prev_node = cur_node.prev
                next_node = cur_node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                if cur_node.next == None:
                    self.tail = prev_node
                return

    def get(self, index):
        if index < 0:
            index = self.list_length + index
        if index >= self.list_length or index < 0:
            raise IndexError
        elif index == 0 or (self.list_length // index) >= 2:
            data = self._front(index)
        else:
            data = self._back(index)
        return data

    def set(self, data, index):
        if index < 0:
            index = self.list_length + index
        if index >= self.list_length or index < 0:
            raise IndexError
        elif index == 0 or self.list_length // index >= 2:
            self._front(index, data)
        else:
            self._back(index, data)

    def _front(self, index, data=None):
        cur_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                if data != None:
                    cur_node.data = data
                    return
                return cur_node.data
            cur_idx += 1

    def _back(self, index, data=None):
        cur_node = self.tail
        cur_idx = self.list_length - 1
        while True:
            if cur_idx == index:
                if data != None:
                    cur_node.data = data
                    return
                return cur_node.data
            cur_node = cur_node.prev
            cur_idx -= 1

    def insert(self, data, index):
        if index < 0:
            index = self.list_length + (index + 1)
        if index >= self.list_length + 1 or index < 0:
            raise IndexError
        elif index == 0 or self.list_length // index >= 2:
            self._front_insert(data, index)
        else:
            print("dsf")
            self._back_insert(data, index)
        self.list_length += 1

    def _front_insert(self, data, index):
        cur_node = self.head
        new_node = node(data)
        cur_idx = 0
        while True:
            if cur_idx == index:
                new_node.next = cur_node.next
                cur_node.next.prev = new_node
                cur_node.next = new_node
                new_node.prev = cur_node
                return
            cur_node = cur_node.next
            cur_idx += 1

    def _back_insert(self, data, index):
        cur_node = self.tail
        new_node = node(data)
        cur_idx = self.list_length - 1
        if index == self.list_length:
            self.append(data)
            return
        while True:
            if cur_idx == index:
                new_node.prev = cur_node.prev
                cur_node.prev.next = new_node
                cur_node.prev = new_node
                new_node.next = cur_node
                return
            cur_node = cur_node.prev
            cur_idx -= 1

    def sort(self):
        cur_node = self.head
        interval = self.list_length
        for q in range(0, self.list_length):
            for i in range(0, interval):
                cur_node = cur_node.next
                if i + 1 == self.list_length:
                    pass
                elif cur_node.data > cur_node.next.data:
                    val = cur_node.data
                    cur_node.data = cur_node.next.data
                    cur_node.next.data = val
            cur_node = self.head
            interval -= 1

    def clear(self):
        self.head.next = None
        self.tail = self.head
        self.list_length = 0

    def copy(self):
        """Returns a copy of the list"""
        new_list = doubly_linked_list()
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_node == None:
                return new_list
            new_list.append(cur_node.data)

    def count(self, data):
        """Counts the number of times a value appears in the list"""
        app = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_node == None:
                return app
            if cur_node.data == data:
                app += 1

    def index(self, data):
        """Finds the index of a value"""
        cur_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_node == None:
                raise ValueError
            if cur_node.data == data:
                return cur_idx
            cur_idx += 1

    def merge(self, doubley_ll):
        """Merges two lists, making list b empty"""
        first_node = doubley_ll._first_node()
        self.tail.next = first_node
        first_node.prev = self.tail
        doubley_ll.head.next = None
        self.tail = doubley_ll.tail
        self.list_length += doubley_ll.list_length

    def _first_node(self):
        return self.head.next

    def extend(self, iterable):
        """Adding the content of a list to this one"""
        for i in iterable:
            self.append(i)


# append
# remove last
# push - add to the front
# search, get index
# remove first

ll = linked_list()
dl = doubly_linked_list()
bl = []


def write_file(opr, obj, num):
    data[opr][obj] = num
    with open("test.json", "w") as f:
        json.dump(data, f)


def append(num):
    list_elems = num  # 500 000
    write_file("append", "elems", num)

    t1 = time.time()
    for i in range(0, list_elems):
        ll.append(i)
    t2 = time.time()
    write_file("append", "single", t2-t1)
    print(t2-t1)

    t1 = time.time()
    for i in range(0, list_elems):
        dl.append(i)
    t2 = time.time()
    write_file("append", "double", t2-t1)
    print(t2-t1)


    t1 = time.time()
    for i in range(0, list_elems):
        bl.append(i)
    t2 = time.time()
    write_file("append", "built_in", t2-t1)
    print(t2-t1)

    print("---------------------------")


def pop(num):
    list_elems = num
    write_file("pop", "elems", num)


    t1 = time.time()
    for i in range(0, list_elems):
        dl.pop()
    t2 = time.time()
    write_file("pop", "double", t2-t1)
    print(t2-t1)


    t1 = time.time()
    for i in range(0, list_elems):
        bl.pop()
    t2 = time.time()
    write_file("pop", "built_in", t2-t1)
    print(t2-t1)

    print("--------------")


def push(num):
    list_elems = num
    write_file("push", "elems", num)

    ll.append(0)
    t1 = time.time()
    for i in range(0, list_elems):
        ll.insert(i, 0)
    t2 = time.time()
    write_file("push", "single", t2-t1)
    print(t2-t1)


    dl.append(0)
    t1 = time.time()
    for i in range(0, list_elems):
        dl.insert(i, 0)
    t2 = time.time()
    write_file("push", "double", t2-t1)
    print(t2-t1)

    t1 = time.time()
    for i in range(0, list_elems):
        bl.insert(0, i)
    t2 = time.time()
    write_file("push", "built_in", t2-t1)
    print(t2-t1)

    print("--------------")


def search(num):
    list_elems = num
    write_file("search", "elems", num)

    t1 = time.time()
    for i in range(0, list_elems):
        ll.index(i)
    t2 = time.time()
    write_file("search", "single", t2 - t1)
    print(t2 - t1)

    t1 = time.time()
    for i in range(0, list_elems):
        dl.index(i)
    t2 = time.time()
    write_file("search", "double", t2 - t1)
    print(t2 - t1)

    t1 = time.time()
    for i in range(0, list_elems):
        bl.index(i)
    t2 = time.time()
    write_file("search", "built_in", t2 - t1)
    print(t2 - t1)

    print("--------------")


def remove_first(num):
    list_elems = num
    write_file("remove_first", "elems", num)

    ll.append(0)
    t1 = time.time()
    for i in range(0, list_elems):
        ll.pop(0)
    t2 = time.time()
    write_file("remove_first", "single", t2-t1)
    print(t2 - t1)

    dl.append(0)
    t1 = time.time()
    for i in range(0, list_elems):
        dl.pop(0)
    t2 = time.time()
    write_file("remove_first", "double", t2-t1)
    print(t2 - t1)

    t1 = time.time()
    for i in range(0, list_elems):
        bl.pop(0)
    t2 = time.time()
    write_file("remove_first", "built_in", t2-t1)

    print(t2 - t1)


append(5000000)
pop(5000000)
push(1000000)
search(1000)
remove_first(1000000)
