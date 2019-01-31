

class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    def remove_first(self):
        temp = [None] * self.capacity
        for ix in range(1, self.size):
            temp[ix - 1] = self.arr[ix]
        self.arr = temp
        self.size -= 1

    def get_size(self):
        return self.size

    def print(self):
        for ix in range(self.size):
            print("{}".format(self.arr[ix]), end=" ")
        print()

    def resize(self):
        self.capacity *= 2
        temp = [None] * self.capacity
        for ix in range(self.size):
            temp[ix] = self.arr[ix]
        self.arr = temp





arr = ArrayList()

arr.append("str1")
arr.append("str2")

arr.print()

arr.remove_first()

arr.print()