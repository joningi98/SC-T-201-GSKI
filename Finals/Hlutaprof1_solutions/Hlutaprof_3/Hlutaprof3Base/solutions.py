class TreeNode:
    def __init__(self, key, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class TreeClass:
    def __init__(self, preset=0):
        node_list = []
        self.root = None
        self.size = 0
        if preset == 1:
            node_list = [5, 2, 1, 4, 8, 7, 9]
        if preset == 2:
            node_list = ["c", "a", "b", "e", "d", "f"]
        if preset == 3:
            node_list = [20, 13, 15, 8, 27, 21]
        if len(node_list) != 0:
            self.make_tree(node_list)

    def make_tree(self, my_list):
        for x in my_list:
            self.add(x)

    def _add(self, node, key):
        if key < node.key:
            if node.left:
                self._add(node.left, key)
            else:
                node.left = TreeNode(key)
        if key > node.key:
            if node.right:
                self._add(node.right, key)
            else:
                node.right = TreeNode(key)

    def add(self, value):
        self.size += 1
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._add(self.root, value)

    def preorder(self, node):
        my_str = ""
        if node:
            my_str += str(node.key) + " "
            my_str += self.preorder(node.left)
            my_str += self.preorder(node.right)
        return my_str

    def inorder(self, node):
        my_str = ""
        if node:
            my_str += self.inorder(node.left)
            my_str += str(node.key) + " "
            my_str += self.inorder(node.right)
        return my_str

    def postorder(self, node):
        my_str = ""
        if node:
            my_str += self.postorder(node.left)
            my_str += self.postorder(node.right)
            my_str += str(node.key) + " "
        return my_str

    def __str__(self):
        ret_str = ""
        if self.size != 0:
            ret_str += self.preorder(self.root) + "\n" + self.inorder(self.root) + "\n" + self.postorder(self.root)
        return ret_str


class HashItem:
    def __init__(self, key, data):
        self.key = key
        self.data = data


class HashClass:
    def __init__(self):
        self.map = [[] for _ in range(16)]

    def __setitem__(self, key, value):
        bucket_index = hash(key) % 16
        for item in self.map[bucket_index]:
            if item.key == key:
                item.data = value
            return
        self.map[bucket_index].append(HashItem(key, value))

    def __getitem__(self, key):
        bucket_index = hash(key) % 16
        if self.map[bucket_index]:
            return self.map[bucket_index]
        else:
            return None


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":
    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!
    """
    h = HashClass()
    h = HashClass(1)

    t = TreeClass()
    t = TreeClass(1)
    """
    print("\nTesting TreeClass __init__ & __str__")
    t = TreeClass()
    print("The tree: \n" + str(t))
    t = TreeClass(3)
    print("The tree: \n" + str(t))
    t = TreeClass(0)
    print("The tree: \n" + str(t))

