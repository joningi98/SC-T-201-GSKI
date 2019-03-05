class HeapNode:
    def __init__(self, priority, data=None, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right


class PriorityQueue:
    def __init__(self):
        self.root = None
        self.last_node = None

    def add(self, priority, value):
        if self.root is None:
            self.root = self.last_node = HeapNode(priority, value)
        elif:
