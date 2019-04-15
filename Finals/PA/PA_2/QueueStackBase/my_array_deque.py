class ArrayDeque:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    def push_front(self, value):
        if self.size + 1 == self.capacity:
            self.resize()
        for ix in range(self.size + 1, 0, -1):
            self.arr[ix - 1] = self.arr[ix - 2]
        self.arr[0] = value
        self.size += 1

    def push_back(self, value):
        if self.size + 1 == self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    def pop_back(self):
        if self.size != 0:
            ret_value = self.arr[self.size]
            self.arr[self.size] = None
            self.size -= 1
            return ret_value
        else:
            return None

    def pop_front(self):
        if self.size != 0:
            ret_val = self.arr[0]
            for ix in range(self.size - 1):
                self.arr[ix] = self.arr[ix + 1]
            self.size -= 1
            return ret_val
        else:
            return None

    def resize(self):
        self.capacity *= 2
        temp = [None] * self.capacity
        for ix in range(self.size):
            temp[ix] = self.arr[ix]
        self.arr = temp

    def get_size(self):
        return self.size

    def __str__(self):
        ret_str = ""
        for ix in range(self.size):
            ret_str += str(self.arr[ix]) + " "
        return ret_str
