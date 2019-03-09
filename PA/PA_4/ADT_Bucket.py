class Node:
    def __init__(self, key=None, data=None, next=None):
        self.key = key
        self.data = data
        self.next = next

    def __str__(self):
        return "{}: {}".format(self.key, self.data)


class Bucket:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, key, data):
        node = self.head
        change = False
        while node is not None:
            if str(node.key) == str(key):
                node.data = data
                change = True
                break
            node = node.next
        if not change:
            self.head = Node(key, data, self.head)
            if self.tail is None:
                self.tail = self.head
            self.size += 1

    def update(self, key, data):
        try:
            self[key] = data
        except IndexError:
            return IndexError

    def find(self, key):
        if self.contains(key):
            _, node = self.contains(key)
            return node.data
        else:
            print("not found")

    def contains(self, key):
        return key in self

    def __contains__(self, key):
        node = self.head
        while node is not None:
            if str(node.key) == str(key):
                return True, node
            node = node.next
        return False

    def remove(self, key):
        pass

    def __setitem__(self, key, data):
        try:
            node = self.head
            while node is not None:
                if str(node.key) == str(key):
                    node.data = data
                node = node.next
        except IndexError:
            self.insert(key, data)

    def __getitem__(self, key):
        node = self.head
        while node is not None:
            if str(node.key) == str(key):
                return node.data
            node = node.next
        return IndexError

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        node = self.head
        while node is not None:
            if node.next is None:
                ret_str += "{}".format(node)
            else:
                ret_str += "{}, ".format(node)
            node = node.next
        return ret_str


class Map:
    def __init__(self):
        self.map = [Bucket() for _ in range(10)]
        self.size = 0

    def insert(self, key, data):
        pass

    def update(self, key, data):
        pass

    def find(self, key):
        pass

    def contains(self, key):
        pass

    def remove(self, key):
        pass

    def __setitem__(self, key, data):
        pass

    def __getitem__(self, key):
        pass

    def __len__(self):
        pass


if __name__ == "__main__":
    my_b = Bucket()
    my_b.insert(1, "A")
    my_b.insert(2, "B")
    my_b.insert(3, "C")
    print(my_b)
    my_b[1] = "Hello"
    print(my_b)
    print(my_b[2])
    my_b[2] = "Valli"
    print(my_b)
    my_b.update(4, "Jón")
    print(my_b)
    print(1 in my_b)
    print(my_b.find(3))
