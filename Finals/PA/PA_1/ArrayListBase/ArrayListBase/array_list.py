class IndexOutOfBounds(Exception):
    pass


class NotFound(Exception):
    pass


class Empty(Exception):
    pass


class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0
        self.sorted = True

    # Time complexity: O(n) - linear time in size of list
    def print(self):
        for ix in range(self.size):
            if ix + 1 == self.size:
                print("{}\n".format(self.arr[ix]), end="")
            else:
                print("{},".format(self.arr[ix]), end="")

    # Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        if self.size + 1 == self.capacity:
            self.resize()
        new_arr = self.arr[:]
        for ix in range(self.size + 1):
            new_arr[ix + 1] = self.arr[ix]
        new_arr[0] = value
        self.arr = new_arr
        self.size += 1
        self.sorted = False

    # Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if self.size + 1 == self.capacity:
            self.resize()
        new_arr = self.arr[:]
        for ix in range(index, self.size + 1):
            new_arr[ix] = self.arr[ix - 1]
        new_arr[index] = value
        self.arr = new_arr
        self.size += 1
        self.sorted = False

    # Time complexity: O(1) - constant time
    def append(self, value):
        if self.size + 1 == self.capacity:
            self.resize()
        if self.size == self.capacity:
            pass
        self.arr[self.size] = value
        self.size += 1
        self.sorted = False

    # Time complexity: O(1) - constant time
    def set_at(self, value, index):
        self.arr[index] = value
        self.sorted = False

    # Time complexity: O(1) - constant time
    def get_first(self):
        return self.arr[0]

    # Time complexity: O(1) - constant time
    def get_at(self, index):
        return self.arr[index]

    # Time complexity: O(1) - constant time
    def get_last(self):
        return self.arr[self.size - 1]

    # Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.capacity *= 2
        temp = [None] * self.capacity
        for ix in range(self.size):
            temp[ix] = self.arr[ix]
        self.arr = temp

    # Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        new_arr = self.arr[:]
        for ix in range(index, self.size):
            new_arr[ix - 1] = self.arr[ix]
        new_arr[self.size - 1] = None
        self.arr = new_arr

    # Time complexity: O(1) - constant time
    def clear(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarythmic time in size of list
    def insert_ordered(self, value):
        if self.size == 0:
            self.append(value)
        elif not self.sorted:
            self.append(value)
            self.sort()
        else:
            ix = self._binary_search(0, self.size, value, failure=False)
            self.insert(value, ix)

    # Time complexity: O(n^2) - quadratic time in size of list
    # Time complexity: O(n log n) - linear times logarythmic time in size of list
    def sort(self):
        for x in range(self.size):
            minimum = x

            for y in range(x + 1, self.size):
                if self.arr[y] < self.arr[minimum]:
                    minimum = y

            self.arr[minimum], self.arr[x] = self.arr[x], self.arr[minimum]
        self.sorted = True

    def _binary_search(self, low, high, target, failure=True):
        size = high - low
        mid = size // 2
        if size % 2 == 1:
            mid += 1
        if low >= high:
            if failure:
                raise NotFound
            else:
                return mid + low
        if target > self.arr[low + mid]:
            return self._binary_search(low + (size + 1) // 2, high, target, failure=failure)
        elif target < self.arr[low + mid]:
            return self._binary_search(low, high - (size + 1) // 2, target, failure=failure)
        return low + mid

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarythmic time in size of list
    def find(self, value):
        if self.sorted:
            index = self._binary_search(0, self.size, value)
            return index
        else:
            for ix in range(self.size):
                if self.arr[ix] == value:
                    return ix
        raise NotFound

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarythmic time in size of list
    def remove_value(self, value):
        try:
            ix = self.find(value)
            self.remove_at(ix)
        except NotFound:
            pass


my_arr = ArrayList()

my_arr.append(1)
my_arr.append(2)
my_arr.append(3)
my_arr.remove_at(1)
