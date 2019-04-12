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

    def _inorder(self, node):
        my_str = ""
        if node:
            my_str += self._inorder(node.left)
            my_str += str(node) + " "
            my_str += self._inorder(node.right)
        return my_str

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

    def find_parent(self, parent, node):
        if parent.left.key == node:
            return parent
        else:
            self.find_parent(parent.left, node)

    def __getitem__(self, key):
        if self.contains(key):
            return self._get_item_helper(key, self.root)
        else:
            raise NotFoundException()

    def _remove_right(self, key, node):
        if node.right is None:
            new_value = node.key
            new_data = node.value
            self.remove(node.key)
            self.size -= 1
            return new_value, new_data
        elif node.right is not None:
            self._remove_right(key, node.right)

    def _remove(self, key, node):
        if node is None:
            return node
        elif node.key is key:
            if node.left is None and node.right is None:
                return None
            elif node.left is None or node.right is None:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
            new_value, new_data = self._remove_right(key, node.left)
            node.key = new_value
            node.value = new_data
            self.size -= 1
            return node
        elif node.key > key:
            node.left = self._remove(key, node.left)
            # self.size-=1
            return node
        elif node.key < key:
            node.right = self._remove(key, node.right)
            # self.size-=1
            return node

    def remove(self, key):
        self._remove(key, self.root)

    def __len__(self):
        return self.size

    def __str__(self):
        return self._inorder(self.root)


class MyComparableKey:
    def __init__(self, value, strval):
        self.int = value
        self.string = strval

    def __lt__(self, other):
        if self.int < other.int:
            return True
        elif self.int == other.int:
            if self.string < other.string:
                return True
        return False

