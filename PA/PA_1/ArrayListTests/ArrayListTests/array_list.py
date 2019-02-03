class IndexOutOfBounds(Exception):
    pass


class NotFound(Exception):
    pass


class Empty(Exception):
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
        print()

    # Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        if self.size == self.capacity:
            self.resize()
        temp = [None] * self.capacity
        self.size += 1
        for ix in range(self.size - 1):
            temp[ix + 1] = self.data[ix]
        temp[0] = value
        self.data = temp

    # Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if index <= self.size:
            if self.size == self.capacity:
                self.resize()
            self.size += 1
            temp = self.data
            for ix in range(self.size - 1, index, -1):
                temp[ix] = self.data[ix - 1]
            temp[index] = value
            self.data = temp

    # Time complexity: O(1) - constant time
    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1

    # Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index <= self.size - 1:
            self.data[index] = value

    # Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty()
        return self.data[0]

    # Time complexity: O(1) - constant time
    def get_at(self, index):
        if index <= self.size - 1:
            return self.data[index]
        raise IndexOutOfBounds

    # Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty()
        else:
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
        if index <= self.size - 1:
            temp = [x for x in self.data]
            for ix in range(self.size, index - 1, -1):
                self.data[ix] = temp[ix + 1]
            self.size -= 1

    # Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0
        self.capacity = 4
        self.data = [0] * self.capacity

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


arr_list = ArrayList()

# 31, 99, 38, 25, 27, 41, 61

arr_list.append(31)
arr_list.append(99)
arr_list.append(38)
arr_list.append(25)
arr_list.append(27)
arr_list.append(41)
arr_list.append(61)
arr_list.remove_at(1)

arr_list.print()