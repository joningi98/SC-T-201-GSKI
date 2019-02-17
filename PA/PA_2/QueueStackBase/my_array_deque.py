
class ArrayDeque:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.data = [None] * self.capacity

    def push_front(self, value):
        self.size += 1
        if self.size == self.capacity:
            self.resize()
        for ix in range(self.size + 1, 0, -1):
            self.data[ix - 1] = self.data[ix - 2]
        self.data[0] = value

    def pop_front(self):
        if self.size != 0:
            temp = [None] * self.capacity
            ret_data = self.data[0]
            for ix in range(self.size):
                temp[ix] = self.data[ix + 1]
            self.data = temp
            self.size -= 1
            return ret_data

    def push_back(self, value):
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1

    def pop_back(self):
        if self.size != 0:
            ret_value = self.data[self.size - 1]
            self.data[self.size - 1] = None
            self.size -= 1
            return ret_value

    def resize(self):
        self.capacity *= 2
        temp = [None] * self.capacity
        for ix in range(self.size):
            temp[ix] = self.data[ix]
        self.data = temp

    def get_size(self):
        return self.size

    def __str__(self):
        ret_srt = ""
        for ix in range(self.size):
            ret_srt += str(self.data[ix]) + " "
        return ret_srt
