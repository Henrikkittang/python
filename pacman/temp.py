
class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None 

class LinkedList(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def append(self, value):
        newNode = Node(value)
        if self._head == None:
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.nextNode = newNode
            self._tail = newNode
        self._length += 1

    def _checkIndex(self, idx: int) -> int:
        if idx >= self.__len__():
            raise IndexError('Index ({}) out of range ({})'.format(idx, len(self)))
        elif idx < 0:
            return self._checkIndex(self.__len__()+idx)
        else:
            return idx

    def _getNodeByIdx(self, idx: int) -> Node:
        idx = self._checkIndex(idx)
        curNode = self._head
        curIdx = 0
        while curIdx < idx:
            curIdx += 1
            curNode = curNode.nextNode
        return curNode
        
    def __iter__(self):
        curNode = self._head
        while curNode:
            yield curNode.data
            curNode = curNode.nextNode

    def __contains__(self, key):
        return key in list(self)
       
    def __len__(self) -> int:
        return self._length

    def __getitem__(self, idx: int):
        return self._getNodeByIdx(idx).data

    def __setitem__(self, idx: int, value) -> None:
        self._getNodeByIdx(idx).data = value

    def __repr__(self) -> str:
        return '[' + ', '.join(str(x) for x in self) + ']'

           

ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

for data in ll:
    print(data)

iterator = iter(ll)
while iterator:
    try:
        print(next(iterator))
    except StopIteration:
        break

print('length: ', len(ll))
print(3 in ll, 18 in ll)
print(ll[0], ll[1], ll[2], ll[3], ll[4])
ll[-1] = 10
print(ll)
print(tuple(ll), list(ll), set(ll))
