class Array:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.data = [0] * self.capacity

    def print_arr(self):
        for ix in range(self.size):
            if ix == self.size -1:
                print("{}".format(self.data[ix]), end="")
            else:
                print("{},".format(self.data[ix]), end="")
        print()

    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1

    def get_first(self):
        return self.data[0]

    def get_at(self, index):
        return self.data[index]

    def get_last(self):
        return self.data[self.size - 1]

    def resize(self):
        self.capacity *= 2
        temp = [0] * self.capacity
        for ix in range(self.size):
            temp[ix] = self.data[ix]
        self.data = temp

    def prepend(self, value):
        temp = self.data
        for ix in range(self.size, 0, -1):
            temp[ix] = self.data[ix - 1]
        temp[0] = value
        self.data = temp
        self.size += 1

    def insert(self, index, value):
        if index <= self.size:
            temp = self.data
            for ix in range(self.size, index, -1):
                temp[ix] = self.data[ix - 1]
            if self.size == self.capacity:
                self.resize()
            temp[index] = value
            self.data = temp
        print("Index out of range!")

    def remove(self, index):
        temp = self.data
        for ix in range(index, self.size, 1):
            temp[ix] = self.data[ix + 1]
        self.data = temp


my_arr = Array()

my_arr.insert(6, 5)

print(my_arr.data)