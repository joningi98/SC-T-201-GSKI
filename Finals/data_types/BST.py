class BinaryNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def _insert(self, node, value):
        if value < node.data:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = BinaryNode(value)
        if value > node.data:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = BinaryNode(value)
        return

    def insert(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.size += 1
            self._insert(self.root, value)

    def _find(self, node, value, ret_node=False):
        if node is None:
            return False
        elif node.data == value:
            if ret_node:
                return node
            else:
                return True
        else:
            if value < node.data:
                return self._find(node.left, value)
            elif value > node.data:
                return self._find(node.right, value)

    def find(self, value, ret_node=False):
        return self._find(self.root, value, ret_node)

    def _swap_and_remove_node(self, original_node, node):
        if node.left is None:
            original_node.data = node.data
            return self._remove_node(node)
        else:
            node.left = self._swap_and_remove_node(original_node, node.left)
            return node

    def _remove_node(self, node):
        if node.left is None and node.right is None:
            return None
        elif node.left and node.right is None:
            return node.left
        elif node.left is None and node.right:
            return node.right
        else:
            node.right = self._swap_and_remove_node(node, node.right)
            return node

    def _remove(self, node, value):
        if node is not None:
            if value < node.data:
                node.left = self._remove(node.left, value)
            elif value > node.data:
                node.right = self._remove(node.right, value)
            else:
                self.size -= 1
                return self._remove_node(node)
        return node

    def remove(self, value):
        if self.find(value):
            self.root = self._remove(self.root, value)
        else:
            pass

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



