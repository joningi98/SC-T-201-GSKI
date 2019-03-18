class BT_Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class BT:
    def __init__(self):
        self.root = None

    def populate_tree(self, data):
        if self.root is None:
            self.root = BT_Node(data)
        else:
            self._populate_tree(self.root, data)

    def _populate_tree(self, root, value):
        if value < root.data:
            if root.left:
                self._populate_tree(root.left, value)
            else:
                root.left = BT_Node(value)
        if value > root.data:
            if root.right:
                self._populate_tree(root.right, value)
            else:
                root.right = BT_Node(value)

    def print_inorder(self, node):
        if node is None:
            return None
        self.print_inorder(node.left)
        print("{}".format(node.data), end=" ")
        self.print_inorder(node.right)

    def print_preorder(self, node):
        if node is None:
            return None
        print(str(node.data), end=" ")
        self.print_preorder(node.left)
        self.print_preorder(node.right)

    def print_postorder(self, node):
        if node is None:
            return None
        self.print_postorder(node.left)
        self.print_postorder(node.right)
        print(str(node.data), end=" ")

    def __str__(self):
        print("Inorder")
        self.print_inorder(self.root)
        print("\nPreorder")
        self.print_preorder(self.root)
        print("\nPostorder")
        self.print_postorder(self.root)
        return ""


bt = BT()
bt.populate_tree(5)
bt.populate_tree(4)
bt.populate_tree(2)
bt.populate_tree(1)
bt.populate_tree(3)
print(bt)
