import random


class NotFoundException(Exception):
    pass


class ItemExistsException(Exception):
    pass


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
        if not self.contains(key):
            self.head = Node(key, data, self.head)
            if self.tail is None:
                self.tail = self.head
            self.size += 1
        else:
            raise ItemExistsException()

    def update(self, key, data):
        try:
            self[key] = data
        except IndexError:
            return IndexError

    def find(self, key):
        if self.contains(key):
            return self[key]
        # raise NotFoundException()

    def contains(self, key):
        return key in self

    def __contains__(self, key):
        node = self.head
        while node is not None:
            if str(node.key) == str(key):
                return True
            node = node.next
        return False

    def remove(self, key):
        if self.contains(key):
            node_1 = self.head
            node_2 = self.head.next
            while node_2 is not None:
                if str(node_1.key) == str(key):
                    self.head = node_1.next
                    self.size -= 1
                    break
                if str(node_2.key) == str(key):
                    node_1.next = node_2.next
                    self.size -= 1
                    break
                node_1 = node_1.next
                node_2 = node_2.next
        else:
            pass
            # raise NotFoundError()

    def __setitem__(self, key, data):
        node = self.head
        if self.contains(key):
            while node is not None:
                if str(node.key) == str(key):
                    node.data = data
                node = node.next
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        node = self.head
        while node is not None:
            if str(node.key) == str(key):
                return node.data
            node = node.next
        # raise NotFound error

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


class HashMap:
    def __init__(self):
        self.map = [Bucket() for _ in range(10)]
        self.size = 10

    def insert(self, key, data):
        selected_bucket = self.map[key]
        if selected_bucket.contains(key):
            raise ItemExistsException
            pass
        else:
            selected_bucket.insert(key, data)

    def update(self, key, data):
        pass

    def find(self, key):
        pass

    def contains(self, key):
        pass

    def remove(self, key):
        pass

    def __setitem__(self, key, data):
        try:
            chose_bucket = self.map[key]
            chose_bucket[key] = data
        except IndexError:
            pass

    def __getitem__(self, key):
        try:
            chose_bucket = self.map[key]
            return chose_bucket[key]
        except IndexError:
            pass

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        for ix, bucket in enumerate(self.map):
            ret_str += "Bucket :{}, [{}]\n".format(ix, bucket)
        return ret_str


class MyHashableKey:
    def __init__(self, int_value=0, string_value=""):
        self.int = int_value
        self.str = string_value

    def __eq__(self, other):
        return self.int == other.int and self.str == other.str


    def __hash__(self):
        pass

'''
if __name__ == "__main__":
    my_map = HashMap()
    my_map.insert(1, "A")
    my_map.insert(2, "B")
    my_map.insert(3, "C")
    my_map.insert(4, "D")
    my_map.insert(5, "E")
    my_map.insert(6, "F")
    my_map.insert(7, "G")
    my_map.insert(8, "H")
    print(my_map)
'''

'''
if __name__ == "__main__":
    print("Testing bucket")
    my_b = Bucket()
    my_b.insert(1, "A")
    my_b.insert(2, "B")
    my_b.insert(3, "C")
    my_b[4] = 'Bucket'
    print(my_b)
'''

