class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "{}:{}".format(self.key, self.value)


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class Dict:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, key, value):
        new_item = Item(key, value)
        new_node = Node(new_item)
        over_write = False
        if self.head is None:
            new_node.next = None
        else:
            node = self.head
            for _ in range(self.size):
                if str(node.data.key) == str(key):
                    node.data.value = value
                    over_write = True
                node = node.next
            if over_write is False:
                pivot = self.head
                while node is not None:
                    if str(pivot.data.key) < str(new_node.data.key):
                        new_node.next = pivot.next
                        pivot.next = new_node
                    node = node.next
                new_node.next = self.head
        if over_write is False:
            self.head = new_node
            self.size += 1

    def find(self, key):
        node = self.head
        while node is not None:
            if str(node.data.key) == str(key):
                return node.data.value
            node = node.next

    def update(self, key, value):
        node = self.head
        while node is not None:
            if str(node.data.key) == str(key):
                node.data.value = value
                break
            node = node.next

    def remove(self, key):
        node_1 = self.head
        node_2 = self.head.next
        while node_1 is not None:
            if str(node_2.data.key) == str(key):
                    node_1.next = node_2.next
                    break

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = "{ "
        node = self.head
        while node is not None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str + "}"


my_dict = Dict()

my_dict.insert("1", "A")
my_dict.insert("3", "C")
my_dict.insert("2", "B")

print(my_dict)
print(len(my_dict))

my_dict.insert("2", "Helllloooo")

print(my_dict)
print(len(my_dict))


my_dict.insert("4", "E")

print(my_dict)
print(len(my_dict))