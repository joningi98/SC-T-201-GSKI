class IndexOutOfBounds(Exception):
    pass


class NotFound(Exception):
    pass


class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.data = [0] * self.capacity

    # Time complexity: O(n) - linear time in size of list
    def print(self):
        for ix in range(self.size):
            if ix == self.size - 1:
                print("{}".format(self.data[ix]), end="")
            else:
                print("{}, ".format(self.data[ix]), end="")
        print("\n")

    # Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.size += 1
        if self.data == self.capacity:
            self.resize()
        for ix in range(self.size + 1, 0, -1):
            self.data[ix - 1] = self.data[ix - 2]
        self.data[0] = value

    # Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        new_list = self.data
        new_list[index] = value
        for ix in range(index - 1, self.size):
            new_list[ix] = self.data[ix]
        new_list[index] = value
        print(self.data)
        # TODO: remove 'pass' and implement functionality

    # Time complexity: O(1) - constant time
    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1

    # Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(1) - constant time
    def get_first(self):
        return self.data[0]

    # Time complexity: O(1) - constant time
    def get_at(self, index):
        return self.data[index]
        # TODO: Fix raise IndexOutOfBounds

    # Time complexity: O(1) - constant time
    def get_last(self):
        return self.data[self.size - 1]

    # Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.capacity *= 2
        new_list = ([0] * self.capacity)
        for ix in range(self.size):
            new_list[ix] = self.data[ix]
        self.data = new_list

    # Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(1) - constant time
    def clear(self):
        self.data = [0] * self.size

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarythmic time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(n^2) - quadratic time in size of list
    # Time complexity: O(n log n) - linear times logarythmic time in size of list
    def sort(self):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarythmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarythmic time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


arr_lis = ArrayList()

arr_lis.append("c")
arr_lis.append("e")
arr_lis.append("d")
arr_lis.print()
arr_lis.append("i")
arr_lis.append("h")
arr_lis.append("g")
arr_lis.print()
arr_lis.append("m")
arr_lis.append("o")
arr_lis.append("n")
arr_lis.print()

arr_lis.insert(4,4)
arr_lis.print()

