class BinaryNode:
    def __init__(self, key, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def _insert(self, node, key, value):
        if key < node.key:
            if node.left:
                self._insert(node.left, key, value)
            else:
                node.left = BinaryNode(key, value)
        if key > node.key:
            if node.right:
                self._insert(node.right, key, value)
            else:
                node.right = BinaryNode(key, value)
        return

    def insert(self, key, value):
        if self.root is None:
            self.root = BinaryNode(key, value)
        else:
            self.size += 1
            self._insert(self.root, key, value)

    def _find(self, node, key, ret_node=False):
        if node is None:
            return False
        elif node.key == key:
            if ret_node:
                return node
            else:
                return True
        else:
            if key < node.key:
                return self._find(node.left, key)
            elif key > node.key:
                return self._find(node.right, key)

    def find(self, key, ret_node=False):
        return self._find(self.root, key, ret_node)

    def swap_and_remove_leftmost(self, original_node, node):
        if node.left is None:


    def _remove_node(self, node):
        if node.left is None and node.right is None:
            return None
        if node.left and node.right is None:
            return node.left
        if node.left is None and node.right:
            return node.right
        else:
            node.right = self.swap_and_remove_leftmost(node, node.right)


    def _remove(self, node, key):
        if key < node.key:
            return self._remove(node.left, key)
        if key > node.key:
            return self._remove(node.right, key)
        else:
            return self._remove_node(node)


    def remove(self, key):
        if self[key]:
            self.root = self._remove(self.root, key)
        else:
            return None

    def __setitem__(self, key, value):
        if self.find(key, True):
            self[key].data = value
        else:
            self.insert(key, value)

    def __getitem__(self, value):
        if self.find(value, True):
            return self.find(value, True)
        else:
            return None

    def preorder(self, node):
        my_str = ""
        if node:
            my_str += str(node.data) + " "
            my_str += self.preorder(node.left)
            my_str += self.preorder(node.right)
        return my_str

    def inorder(self, node):
        my_str = ""
        if node:
            my_str += self.inorder(node.left)
            my_str += str(node.data) + " "
            my_str += self.inorder(node.right)
        return my_str

    def postorder(self, node):
        my_str = ""
        if node:
            my_str += self.postorder(node.left)
            my_str += self.postorder(node.right)
            my_str += str(node.data) + " "
        return my_str

    def __str__(self):
        return "Pre-order:\n{}\nIn-order:\n{}\nPost-order:\n{}".format(self.preorder(self.root), self.inorder(self.root), self.postorder(self.root))


bst = BST()

bst.insert(5, "Number 5")
bst.insert(4, "Number 4")
bst.insert(3, "Number 3")
bst.insert(8,  "Number 8")
bst.insert(1, "Number 1")
bst.insert(10, "Number 10")
