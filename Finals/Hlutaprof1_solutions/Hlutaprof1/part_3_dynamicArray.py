class dynamicArray:
    def __init__(self):
        self.capacity = 4
        self.array = [None] * self.capacity
        self.size = 0

    def prepend(self, value):
        new_array = self.array[:]
        for ix in range(self.size):
            new_array[ix + 1] = self.array[ix]
        new_array[0] = value
        self.array = new_array
        self.size += 1

    def insert_at(self, index, value):
        new_array = self.array[:]
        for ix in range(self.size):
            new_array[ix + 1] = self.array[ix]
        new_array[index] = value
        self.array = new_array
        self.size += 1

    def remove_last(self):
        if self.size != 0:
            ret_val = self.array[self.size]
            self.array[self.size - 1] = None
            self.size -= 1
            return ret_val
        else:
            return None

    def remove_first(self):
        self.array[0] = None
        for ix in range(self.size - 1):
            self.array[ix] = self.array[ix + 1]
        self.size -= 1

    def remove_at(self, index):
        for ix in range(index, self.size):
            self.array[ix - 1] = self.array[ix]
        self.array[self.size - 1] = None
        self.size -= 1

    def append(self, value):
        self.array[self.size] = value
        self.size += 1

    def set_at(self, index, value):
        self.array[index] = value

    def get_size(self):
        return self.size

    def print_list(self):
        for ix in range(self.size):
            print("{}".format(self.array[ix]), end=" ")
        print()


my_arr = dynamicArray()

my_arr.insert_at(0, "String 1")
my_arr.insert_at(0, "String 2")
my_arr.insert_at(0, "String 3")
my_arr.print_list()
my_arr.prepend("HELLOO")
my_arr.print_list()
my_arr.remove_first()
my_arr.print_list()
