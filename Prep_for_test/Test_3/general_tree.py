class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


class GeneralTree:
    def __init__(self):
        self.root = None

    def populate(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._populate(data, self.root)

    def _populate(self, data, node):
        if len(node.children) < 4:
            new_node = TreeNode(data)
            node.children.append(new_node)
        else:
            pass