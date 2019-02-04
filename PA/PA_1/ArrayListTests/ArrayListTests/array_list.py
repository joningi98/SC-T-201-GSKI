class IndexOutOfBounds(Exception):
    pass


class NotFound(Exception):
    pass


class Empty(Exception):
    pass


class ArrayList:
    def __init__(self):
        self._size = 0
        self._capacity = 4
        self._data = [0] * self._capacity
        self._sorted = True

    # Time complexity: O(n) - linear time in size of list
    def print(self):
        for ix in range(self._size):
            if ix == self._size - 1:
                print("{}".format(self._data[ix]), end="")
            else:
                print("{}, ".format(self._data[ix]), end="")
        print()

    # Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self._sorted = False
        if self._size == self._capacity:
            self.resize()
        temp = [0] * self._capacity
        self._size += 1
        for ix in range(self._size - 1):
            temp[ix + 1] = self._data[ix]
        temp[0] = value
        self._data = temp

    # Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        self._sorted = False
        if self._size >= index >= 0:
            if self._size == self._capacity:
                self.resize()
            self._size += 1
            for ix in range(self._size - 1, index, -1):
                self._data[ix] = self._data[ix - 1]
            self._data[index] = value

    # Time complexity: O(1) - constant time
    def append(self, value):
        self._sorted = False
        if self._size == self._capacity:
            self.resize()
        self._data[self._size] = value
        self._size += 1

    # Time complexity: O(1) - constant time
    def set_at(self, value, index):
        self._sorted = False
        if index <= self._size - 1:
            self._data[index] = value

    # Time complexity: O(1) - constant time
    def get_first(self):
        if self._size == 0:
            raise Empty()
        return self._data[0]

    # Time complexity: O(1) - constant time
    def get_at(self, index):
        if self._size - 1 >= index >= 0:
            return self._data[index]
        raise IndexOutOfBounds

    # Time complexity: O(1) - constant time
    def get_last(self):
        if self._size == 0:
            raise Empty()
        else:
            return self._data[self._size - 1]

    # Time complexity: O(n) - linear time in size of list
    def resize(self):
        self._capacity *= 2
        new_list = ([0] * self._capacity)
        for ix in range(self._size):
            new_list[ix] = self._data[ix]
        self._data = new_list

    # Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if self._size - 1 >= index >= 0:
            for ix in range(index, self._size - 1):
                self._data[ix] = self._data[ix+1]
            self._size -= 1

    # Time complexity: O(1) - constant time
    def clear(self):
        self._sorted = True
        self._size = 0
        self._capacity = 4
        self._data = [0] * self._capacity

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarythmic time in size of list
    def insert_ordered(self, value):
        if self._size == 0:
            self.append(value)
        elif not self._sorted:
            self.append(value)
            self.sort()
        else:
            ix = self.binary_search(0, self._size, value, failure=False)
            self.insert(value, ix)

    # Time complexity: O(n^2) - quadratic time in size of list
    # Time complexity: O(n log n) - linear times logarythmic time in size of list
    def sort(self):
        tmp = self._data[:self._size]
        tmp.sort()
        self._data = tmp + (len(self._data) - len(tmp)) * [0]
        self._sorted = True
        # TODO: remove 'pass' and implement functionality

    def binary_search(self, low, high, target, failure=True):
        size = high - low
        mid = size // 2
        if low >= high:
            if failure:
                raise NotFound
            else:
                return mid + low
        if target > self._data[low + mid]:
            return self.binary_search(low + (size + 1) // 2, high, target, failure=failure)
        elif target < self._data[low + mid]:
            return self.binary_search(low, high - (size+1) // 2, target, failure=failure)
        return low + mid

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarythmic time in size of list
    def find(self, value):
        if self._sorted:
            index = self.binary_search(0, self._size, value)
            return index
        else:
            for ix in range(self._size):
                print(self._data[ix], value)
                if self._data[ix] == value:
                    return ix
            raise NotFound

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarythmic time in size of list
    def remove_value(self, value):
        ix = self.find(value)
        self.remove_at(ix)

