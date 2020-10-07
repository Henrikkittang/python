class node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list(object):
    def __init__(self, list=None):
        self.head = node()
        self.tail = self.head
        self.list_length = 0
        self.index = -1
        self.iter_index = -1
        self.iter_node = self.head

        if list != None:
            self.create(list)

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
        list_content = ""
        while cur_node.next != None:
            cur_node = cur_node.next
            list_content += str(cur_node.data) + ", "
        return list_content

    def create(self, list):
        for i in list:
            self.append(i)

    def append(self, data):
        new_node = node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.list_length += 1

    def length(self):
        return self.list_length

    def display(self):
        list_content = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            list_content.append(cur_node.data)
        print(list_content)

    def get(self, index, mode=None):
        if index >= self.length() or index < self.list_length * -1:
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
        if index >= self.length() or index < self.list_length * -1:
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

    def pop(self, index=None):
        if index == None:
            self._remove_last()
            return
        elif index >= self.length() or index < 0:
            raise IndexError
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

    def _remove_last(self):
        cur_node = self.head
        while True:
            if cur_node.next == self.tail:
                cur_node.next = None
                self.tail = cur_node
                return
            cur_node = cur_node.next

    def remove(self, data):
        cur_node = self.head
        while True:
            if cur_node.next == None:
                raise ValueError
            cur_node = cur_node.next
            if cur_node.next.data == data:
                cur_node.next = cur_node.next.next
                cur_node.next.next = None
                return

    def insert(self, data, index):
        if index >= self.length() or index < 0:
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
        self.head.next = None
        self.tail = self.head
        self.list_length = 0
