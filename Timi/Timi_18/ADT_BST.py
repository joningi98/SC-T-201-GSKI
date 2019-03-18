class Binary_Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class Binary_Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, value):
        self.size += 1
        if self.root is None:
            self.root = Binary_Node(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value < node.value:
            if node.left:
                self._add(node.left, value)
            else:
                node.left = Binary_Node(value)
        else:
            if node.right:
                self._add(node.right, value)
            else:
                node.right = Binary_Node(value)

    def contains(self, value):
        if self.root is None:
            return False
        else:
            return self._contains(self.root, value)

    def _contains(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._contains(node.left, value)
        if value > node.value:
            return self._contains(node.right, value)

    def remove(self, value):
        self.size -= 1
        if self.contains(value):
            node_before_target = self._find_1_before_node(self.root, value)
            print(node_before_target)
            self._remove(node_before_target, value)
        else:
            return "Node not in the tree"

    def _remove(self, node, value):
        if node.value > value:
            node_to_remove = node.left
            if node_to_remove.left is None and node_to_remove.right is None:
                node.left = None
            elif node_to_remove.left is not None and node_to_remove.right is not None:
                the_swaper = self._swap_rightmost(node_to_remove)
                node_to_remove.value = the_swaper.value
        if node.value < value:
            node_to_remove = node.right
            if node_to_remove.left is None and node_to_remove.right is None:
                node.right = None
            elif node_to_remove.left is not None and node_to_remove.right is not None:
                the_swaper = self._swap_rightmost(node_to_remove)
                node_to_remove.value = the_swaper.value

    def _swap_rightmost(self, node):
        if node.right.right is None:
            if node.right.left is None:
                ret_node = node.right
                node.right = None
                return ret_node
        else:
            self._swap_rightmost(node.right)

    def _find_1_before_node(self, node, value):
        if node is None:
            return False
        elif node.left is not None and value == node.left.value:
            return node
        elif node.right is not None and value == node.right.value:
            return node
        elif value < node.value:
            return self._find_1_before_node(node.left, value)
        elif value > node.value:
            return self._find_1_before_node(node.right, value)

    def print_inorder(self, node):
        if node is None:
            return None
        self.print_inorder(node.left)
        print(str(node.value), end=" ")
        self.print_inorder(node.right)

    def print_postorder(self, node):
        if node is None:
            return None
        self.print_postorder(node.left)
        self.print_postorder(node.right)
        print(str(node.value), end=" ")

    def __len__(self):
        return self.size

    def __str__(self):
        print("IN-ORDER")
        self.print_inorder(self.root)
        print("\nPOST-ORDER")
        self.print_postorder(self.root)
        return ""


bst = Binary_Tree()

bst.add('D')
bst.add('E')
bst.add('B')
bst.add('A')
bst.add('C')
print(bst)
print()
print(bst.remove('B'))
print()
print(bst)