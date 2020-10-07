import math


class Node:
    def __init__(self, data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.count = 1


class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0

    def show(self):
        if self.root != None:
            self._show(self.root)

    def _show(self, node):
        if node != None:
            self._show(node.leftChild)
            print(node.data, " x ", node.count)
            self._show(node.rightChild)

    def add(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._add(self.root, data)
        self.numNodes += 1

    def _add(self, node, data):
        if data == node.data:
            node.count += 1

        elif data > node.data and node.rightChild != None:
            self._add(node.rightChild, data)

        elif data < node.data and node.leftChild != None:
            self._add(node.leftChild, data)

        else:
            if node.count > 1:
                node.count -= 1
            elif data > node.data:
                node.rightChild = Node(data)
                node.rightChild.parent = node
            else:
                node.leftChild = Node(data)
                node.leftChild.parent = node

    def height(self):
        return math.floor(math.log(self.numNodes, 2)) + 1

    def delete(self, data):
        self._delete(self.root, data)

    def _delete(self, node, data):
        if node == None:
            raise ValueError("Item not in tree")

        left = node.leftChild
        right = node.rightChild
        parent = node.parent

        if data != node.data:
            if data > node.data:
                self._delete(node.rightChild, data)
            else:
                self._delete(node.leftChild, data)
            return

        elif node.count > 1:
            node.count -= 1

        # zero children delete
        elif left == None and right == None:
            if parent == None:
                self.root = None
            else:
                if parent.rightChild == node:
                    parent.rightChild = None
                else:
                    parent.leftChild = None

        # one child delete, left child
        elif left != None and right == None:
            if parent == None:
                node.leftChild.parent = None
                self.root = node.leftChild
            else:
                if parent.rightChild == node:
                    parent.rightChild = node.leftChild
                else:
                    parent.leftChild = node.leftChild

        # one child delete, right child
        elif left == None and right != None:
            if parent == None:
                node.rightChild.parent = None
                self.root = node.rightChild
            else:
                if parent.rightChild == node:
                    parent.rightChild = node.rightChild
                else:
                    parent.leftChild = node.rightChild

        # two children
        elif left != None and right != None:
            lowest = self._pop_lowest(right)
            node.data = lowest.data

    def _pop_lowest(self, node):
        if node.leftChild != None:
            return self._pop_lowest(node.leftChild)
        else:
            if node.parent.rightChild == node:
                node.parent.rightChild = node.rightChild
            else:
                node.parent.leftChild = node.rightChild
            return node

    def find(self, data):
        return self._find(self.root, data)

    def _find(self, node, data):
        if node == None:
            return False
        elif data != node.data:
            if data > node.data:
                return self._find(node.rightChild, data)
            else:
                return self._find(node.leftChild, data)
        else:
            return True


