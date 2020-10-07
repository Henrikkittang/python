
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







            
