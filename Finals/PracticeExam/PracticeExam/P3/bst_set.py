class BSTSetNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BSTSet:
    def __init__(self):
        self.root = None
        self.size = 0

    def _add(self, value, node):
        if node is None:
            self.size += 1
            return BSTSetNode(value)
        elif value < node.value:
            node.left = self._add(value, node.left)
        elif node.value < value:
            node.right = self._add(value, node.right)
        return node

    def add(self, value):
        self.root = self._add(value, self.root)

    def contains(self, value):
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def find_left_most(self, node):
        if node.left is None:
            return node
        else:
            return self.find_left_most(node.left)

    @staticmethod
    def is_leaf(node):
        if node.left is None and node.right is None:
            return True
        else:
            return False

    # IMPLEMENT THIS
    def _remove_node(self, node):
        if node.left is None and node.right is None:
            return None
        if node.left and node.right is None:
            return node.left
        if node.left is None and node.right:
            return node.right
        if node.left and node.right:
            if self.is_leaf(node.left) or not self.is_leaf(node.right):
                node_to_switch = self.find_left_most(node)
                target = node.value
                switch = node_to_switch.value
                node_to_switch.value = target
                node.value = switch
                node_to_switch = self._remove_node(node_to_switch)
                print(node.left)
                return node
            else:
                return self.find_left_most(node.right)

    def _remove(self, value, node):
        if node is not None:
            if value < node.value:
                node.left = self._remove(value, node.left)
            elif node.value < value:
                node.right = self._remove(value, node.right)
            else:
                self.size -= 1
                return self._remove_node(node)
        return node

    def remove(self, value):
        self.root = self._remove(value, self.root)

    def _inorder(self, node):
        my_str = ""
        if node:
            my_str += self._inorder(node.left)
            my_str += str(node) + " "
            my_str += self._inorder(node.right)
        return my_str

    def __str__(self):
        return self._inorder(self.root)

    def __len__(self):
        return self.size


if __name__ == "__main__":
    print("\n\nTESTING REMOVE\n")

    bst_set = BSTSet()
    bst_set.add(5)
    bst_set.add(2)
    bst_set.add(4)
    bst_set.add(3)
    bst_set.add(1)
    bst_set.add(7)
    bst_set.add(6)
    bst_set.add(8)
    bst_set.add(10)
    bst_set.add(9)
    bst_set.add(11)
    bst_set.add(12)
    print(bst_set)

    # bst_set.remove(11)
    # print(bst_set)

    bst_set.remove(10)
    print(bst_set)
    # bst_set.remove(8)
    # print(bst_set)
    # bst_set.remove(2)
    # print(bst_set)
    # bst_set.remove(7)
    # print(bst_set)
    # bst_set.remove(5)
    # print(bst_set)
    # bst_set.remove(9)
    # print(bst_set)
    # bst_set.remove(3)
    # print(bst_set)

