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
        if self.contains(key):
            self[key] = data
        else:
            raise NotFoundException()

    def find(self, key):
        try:
            return self[key]
        except Exception:
            raise NotFoundException()

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
            if self.size != 1:
                node_1 = self.head
                node_2 = self.head.next
                while node_2 is not None:
                    if str(node_1.key) == str(key):
                        self.head = self.head.next
                        self.size -= 1
                        break
                    if str(node_2.key) == str(key):
                        node_1.next = node_2.next
                        self.size -= 1
                        break
                    node_1 = node_1.next
                    node_2 = node_2.next
            else:
                self.head = None
                self.tail = None
                self.size -= 1
        else:
            raise NotFoundException()

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
        raise NotFoundException()

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
        self.capacity = 8
        self.map = [Bucket() for _ in range(self.capacity)]
        self.size = 0

    def insert(self, key, data):
        if self.check_size_of_map():
            self.__resize()
        selected_bucket = self.map[hash(key) % self.capacity]
        if selected_bucket.contains(key):
            raise ItemExistsException()
        else:
            selected_bucket.insert(key, data)
            self.size += 1

    def update(self, key, data):
        selected_bucket = self.map[hash(key) % self.capacity]
        if selected_bucket.contains(key):
            selected_bucket.update(key, data)
        else:
            raise NotFoundException()

    def find(self, key):
        try:
            selected_bucket = self.map[hash(key) % self.capacity]
            return selected_bucket.find(key)
        except Exception:
            raise NotFoundException()

    def contains(self, key):
        return key in self

    def remove(self, key):
        selected_bucket = self.map[hash(key) % self.capacity]
        if selected_bucket.find(key):
            selected_bucket.remove(key)
            self.size -= 1
        else:
            raise NotFoundException()

    def __resize(self):
        self.capacity *= 2
        temp = [Bucket() for _ in range(self.capacity)]
        for bucket in self.map:
            node = bucket.head
            while node is not None:
                temp[hash(node.key) % self.capacity].insert(node.key, node.data)
                node = node.next
        self.map = temp

    def check_size_of_map(self):
        if self.size / self.capacity >= 1.20:
            return True
        else:
            return False

    def __contains__(self, key):
        selected_bucket = self.map[hash(key) % self.capacity]
        if selected_bucket.contains(key):
            return True
        else:
            return False

    def __setitem__(self, key, data):
        if self.contains(key):
            self.update(key, data)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        if self.contains(key):
            selected_bucket = self.map[hash(key) % self.capacity]
            return selected_bucket[key]
        else:
            raise NotFoundException()

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        for ix, bucket in enumerate(self.map):
            ret_str += "Bucket :{}, [{}]\n".format(ix, bucket)
        return ret_str


class MyHashableKey:
    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value

    def __eq__(self, other):
        return self.int_value == other.int_value and self.string_value == other.string_value

    def __hash__(self):
        str_value = sum([ord(x) for x in self.string_value])
        my_hash = str_value * self.int_value
        return (((my_hash * 33) // 37) * 39) * 41
