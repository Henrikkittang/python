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
        new_node = node(data)
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

    def idx(self, data):
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

