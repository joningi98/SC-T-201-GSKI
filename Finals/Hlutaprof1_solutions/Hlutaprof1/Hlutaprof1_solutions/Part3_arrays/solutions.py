
class ArrayList:
    def __init__(self):
        self.capacity = 4 #do not change this initial capacity
        self.arr = [None] * self.capacity
        self.size = 0

    def get_size(self):
        return self.size

    def print_list(self):
        for i in range(self.size):
            print(self.arr[i], end = " ")
        print("")

    def resize(self):
        self.capacity *= 2
        tmp = [0] * self.capacity
        for i in range(self.size):
            tmp[i] = self.arr[i]
        self.arr = tmp

    def insert_at(self, index, value):
        if self.size == self.capacity:
            self.resize()
        if index >= 0 and index <= self.size:
            i = self.size
            while i > index:
                self.arr[i] = self.arr[i - 1]
                i -= 1
            self.arr[index] = value
            self.size += 1

    def remove_at(self, index):
        if index >= 0 and index < self.size:
            i = index + 1
            while i < self.size:
                self.arr[i - 1] = self.arr[i]
                i += 1
            self.size -= 1

    def prepend(self, value):
        if self.size == self.capacity:
            self.resize()
        i = self.size
        while i > 0:
            self.arr[i] = self.arr[i - 1]
            i -= 1
        self.arr[0] = value
        self.size += 1

    def remove_first(self):
        if self.size > 0:
            i = 1
            while i < self.size:
                self.arr[i - 1] = self.arr[i]
                i += 1
            self.size -= 1


    def set_at(self, index, value):
        if index >= 0 and index < self.size:
            self.arr[index] = value

    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    def remove_last(self):
        if self.size > 0:
            self.size -= 1
