class ArrayList:
    def __init__(self):
        self.size = 3
        self.capacity = 4
        self.arr = [0] * self.capacity

    def print_array_list(self):
        for ix in range(self.size - 1):
            if ix == self.size - 2:
                print("{}".format(self.arr[ix]), end="")
            else:
                print("{},".format(self.arr[ix]), end="")
        print("\n")

    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size - 1] = value
        self.size += 1

    def get_at(self, ix):
        return self.arr[ix]

    def get_last(self):
        return self.arr[self.size - 1]

    def resize(self):
        new_list = ([0] * self.capacity) * 2
        for ix in range(self.size):
            new_list[ix] = self.arr[ix]
        self.arr = new_list

    def prepend(self, value):
        for ix in range(self.capacity, 0, -1):
            self.arr[ix + 1] = self.arr[ix]
        self.arr[0] = value
        self.size += 1

    def insert(self, value, index):
        for ix in range(self.capacity, 0, -1):
            self.arr[ix + 1] = self.arr[ix]
        self.arr[index] = value
        self.size += 1

    def remove(self, index):
        self.arr.remove(self.arr[index])
        for ix in range(index, 0, self.capacity):
            self.arr[ix - 1] = self.arr[ix]
        self.size -= 1


my_arr = ArrayList()
my_arr.append(5)
my_arr.print_array_list()
my_arr.append(8)
my_arr.print_array_list()
my_arr.insert(12, 2)
my_arr.print_array_list()
my_arr.remove(0)
my_arr.print_array_list()
