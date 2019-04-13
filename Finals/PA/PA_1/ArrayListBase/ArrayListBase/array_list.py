class IndexOutOfBounds(Exception):
    pass


class NotFound(Exception):
    pass


class Empty(Exception):
    pass


class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [0] * self.capacity
        self.size = 0

    # Time complexity: O(n) - linear time in size of list
    def print(self):
        for ix in range(self.size):
            if ix + 1 == self.size:
                print("{}\n".format(self.arr[ix]), end="")
            else:
                print("{},".format(self.arr[ix]), end="")

    # Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        for ix in range(self.size, -1, -1):
            print(self.arr[ix])

    # Time complexity: O(1) - constant time
    def append(self, value):
        if self.size == self.capacity:
            pass
        self.arr[self.size] = value
        self.size += 1

    # Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(n) - linear time in size of list
    def resize(self):
        pass

    # Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        pass

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


my_arr = ArrayList()

my_arr.append(1)
my_arr.append(2)
my_arr.append(3)

my_arr.insert(5, 1)

my_arr.print()
print(my_arr.arr)

