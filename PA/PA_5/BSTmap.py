class ItemExistsException(Exception):
    pass


class NotFoundException(Exception):
    pass


class BST_Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "{" + str("{}, {}".format(self.key, self.value) + "}")


class BSTMap:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, value):
        if self.contains(key):
            raise ItemExistsException()
        else:
            self.size += 1
            if self.root is None:
                self.root = BST_Node(key, value)
            else:
                self._insert(key, value, self.root)

    def _insert(self, key, value, node):
        if key < node.key:
            if node.left:
                self._insert(key, value, node.left)
            else:
                node.left = BST_Node(key, value)
        else:
            if node.right:
                self._insert(key, value, node.right)
            else:
                node.right = BST_Node(key, value)

    def update(self, key, value):
        self[key] = value

    def find(self, key):
        return self[key].value

    def contains(self, key):
        return self._contains(key, self.root)

    def _contains(self, key, node):
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._contains(key, node.left)
        else:
            return self._contains(key, node.right)

    def _print_inorder(self, node):
        if node is None:
            return None
        self._print_inorder(node.left)
        print("{}".format(node), end=' ')
        self._print_inorder(node.right)

    def _set_item(self, key, value, node):
        if key == node.key:
            node.value = value
            return
        if key < node.key:
            self._set_item(key, value, node.left)
        else:
            self._set_item(key, value, node.right)

    def __setitem__(self, key, value):
        try:
            if self.contains(key):
                self._set_item(key, value, self.root)
        except Exception:
            raise NotFoundException()

    def _get_item_helper(self, key, node):
        if key == node.key:
            return node
        if key < node.key:
            return self._get_item_helper(key, node.left)
        if key > node.key:
            return self._get_item_helper(key, node.right)

    def remove(self, key):
        if self.contains(key):
            node_before_target = self._find_target_to_remove(key, self.root)
            self._remove_node(key, node_before_target)
        else:
            raise NotFoundException()

    def _find_target_to_remove(self, key, node):
        if key == node.left.key:
            return node
        if key == node.right.key:
            return node
        else:
            if key < node.key:
                return self._find_target_to_remove(key, node.left)
            else:
                return self._find_target_to_remove(key, node.right)

    def _remove_node(self, key, node):
        node_before_target = node
        if key == node_before_target.left.key:
            target = node_before_target.left
            if target.left is None and target.right is None:
                node_before_target.left = None
            elif target.left and target.right is None:
                node_before_target.left = target.left
            elif target.left is None and target.right:
                node_before_target.left = target.right
            elif target.left and target.right:
                node_to_swap = self._find_leftmost(target.right)
                temp_key, temp_value = target.key, target.value
                target.key = node_to_swap.key
                target.value = node_to_swap.value
                node_to_swap.key, node_to_swap.value = temp_key, temp_value
                self.remove(node_to_swap.key)
        elif key == node_before_target.right.key:
            if node_before_target.right.right is None and node_before_target.right.left is None:
                node_before_target.right = None
            elif node_before_target.right.right and node_before_target.right.left is None:
                node_before_target.right = node_before_target.right.right
            elif node_before_target.right.right is None and node_before_target.right.left:
                node_before_target.right = node_before_target.right.left
            elif node_before_target.right.right and node_before_target.right.left:
                node_to_swap = self._find_leftmost(node_before_target.right.right)
                print(node_to_swap)
                node_to_swap.right = node_before_target.right.right
                node_before_target = node_to_swap

    def _find_leftmost(self, node):
        if node.left is None:
            return node
        else:
            return self._find_leftmost(node.left)

    def __getitem__(self, key):
        if self.contains(key):
            return self._get_item_helper(key, self.root)
        else:
            raise NotFoundException()

    def __len__(self):
        return self.size

    def __str__(self):
        self._print_inorder(self.root)
        return ""


bst = BSTMap()
bst.insert(8, "Eight")
bst.insert(10, "Ten")
bst.insert(3, "Three")
bst.insert(7, "Seven")
bst.insert(5, "Five")
bst.insert(6, "Six")
bst.insert(2, "Two")
print(bst)
bst.remove(3)
print(bst)