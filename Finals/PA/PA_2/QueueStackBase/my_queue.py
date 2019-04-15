from Finals.PA.PA_2.QueueStackBase.my_array_deque import *
from Finals.PA.PA_2.QueueStackBase.my_linked_list import *


class Queue:
    def __init__(self, type=""):
        self.type = type
        if self.type == "array":
            self.container = ArrayDeque()
        if self.type == "linked":
            self.container = LinkedList()

    def add(self, value):
        self.container.push_back(value)

    def remove(self):
        return self.container.pop_front()

    def get_size(self):
        return self.container.get_size()
