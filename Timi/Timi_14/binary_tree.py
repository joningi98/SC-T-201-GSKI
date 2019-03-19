class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def _populate_tree_recur(self):
        data_str = input()
        if data_str == "":
            return None
        left = self._populate_tree_recur()
        right = self._populate_tree_recur()
        return BinaryTreeNode(data_str, left, right)

    def populate_tree(self):
        self.root = self._populate_tree_recur()

    def count_values(self, target):
        return self._count_values_recur(self.root, target)

    def _count_values_recur(self, node, target):
        if not node:
            return 0
        return (node.data == target) + self._count_values_recur(node.left, target) + \
                                       self._count_values_recur(node.right, target)

    def change_value(self, old_value, new_value):
        return self.__change_value_recur(self.root, old_value, new_value)

    def __change_value_recur(self, node, old_value, new_value):
        if not node:
            return None
        if node.data == old_value:
            node.data = new_value
        return self.__change_value_recur(node.left, old_value, new_value), \
               self.__change_value_recur(node.right, old_value, new_value)

    def print_postorder(self, node):
        if node is None:
            return
        self.print_postorder(node.left)
        self.print_postorder(node.right)
        print(str(node.data), end=" ")

    def print_preorder(self, node):
        if node is None:
            return
        print(str(node.data), end=" ")
        self.print_preorder(node.left)
        self.print_preorder(node.right)

    def print_inorder(self, node):
        string = ""
        if node:
            string += self.print_inorder(node.left)
            string += str(node.data) + " "
            string += self.print_inorder(node.right)
        return string

    def print_tree(self):
        print("Post-order")
        self.print_postorder(self.root)
        print("")
        print("Pre-order")
        self.print_preorder(self.root)
        print("")
        print("In-order")
        self.print_inorder(self.root)
        print("")

    def __str__(self):
        return self.print_inorder(self.root)


if __name__ == "__main__":
    print("\nTesting Binary-Tree\n")
    bt = BinaryTree()
    bt.root = BinaryTreeNode('A',
                             BinaryTreeNode('B',
                                            BinaryTreeNode('C'),
                                            BinaryTreeNode('D')),
                             BinaryTreeNode('E',
                                            BinaryTreeNode('F'),
                                            BinaryTreeNode('G',
                                                           BinaryTreeNode('A'))))
    bt.print_tree()

    print(bt)
