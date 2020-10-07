from math import ceil, log

# Needs an efficient build_heap function
# the index, change_key and delete functions are kind of pointless
# could use change_key and delete with indexes instead of keys also, but that too is kind of pointless
# needs to be rewritten or added and extra class for string keys
# could be a node with a integer priority and data slot for other values
# min_heap?


class max_heap(object):
    def __init__(self, values=[]):
        #   super().__init__()
        self.heap = []
        self.build_heap(values)

    def __repr__(self):
        return str(self.heap[0:len(self.heap)])

    def _swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def _bubbleUp(self, index):
        parent = (index - 1) // 2
        if index == 0:
            return
        if self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            self._bubbleUp(parent)

    def _maxHeapify(self, index):
        left = (2 * index) + 1
        right = (2 * index) + 2

        if left <= len(self.heap) - 1 and self.heap[left] > self.heap[index]:
            largest = left
        else:
            largest = index

        if right <= len(self.heap) - 1 and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self._swap(index, largest)
            self._maxHeapify(largest)

    def push(self, data):
        self.heap.append(data)
        self._bubbleUp(len(self.heap) - 1)

    def getMax(self):
        return self.heap[0]

    def popRoot(self):
        self._swap(0, len(self.heap) - 1)
        max_val = self.heap.pop()
        self._maxHeapify(0) 
        return max_val

    def get_height(self):
        temp_size = len(self.heap) - 1
        height = ceil(log(temp_size, 2))
        return height + 1

    def sort(self):
        sorted_list = []
        while len(self.heap) > 0:
            max_val = self.getMax()
            sorted_list.append(max_val)
            self.popRoot()
        self.heap = sorted_list 

    def clear(self):
        self.heap.clear()

    def index(self, data):
        return self.heap.index(data)

    def change_key(self, key, new_key):
        idx = self.index(key)
        self.heap[idx] = new_key

        if new_key > key:
            self._bubbleUp(idx)
        elif new_key < key:
            self._maxHeapify(idx)

    def delete(self, key):
        """Not tested"""
        idx = self.index(key)
        val = self.heap[-1]
        self._swap(idx, len(self.heap) - 1)
        self.heap.pop()

        if val > key:
            self._bubbleUp(idx)
            
        elif val < key:
            self._maxHeapify(idx)

    def build_heap(self, vals):
        self.heap = vals
        for i in range(len(self.heap) - 1, 0, -1):
            if (2 * i) + 1 < len(self.heap):
                self._maxHeapify(i)
        self._maxHeapify(0)



mh = max_heap()

mh.push(34)
mh.push(1)
mh.push(23)
mh.push(245)
mh.push(23)
mh.push(12)

mh.sort()

print(mh)

        
