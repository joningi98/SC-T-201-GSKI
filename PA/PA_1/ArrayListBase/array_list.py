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
        print()

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
        if index <= self.size:
            new_list = [x for x in self.data]
            for ix in range(self.size, index, -1):
                self.data[ix] = new_list[ix - 1]
            self.data[index] = value
            self.size += 1

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
        return self.data[0]

    # Time complexity: O(1) - constant time
    def get_at(self, index):
        if index <= self.size - 1:
            return self.data[index]
        raise IndexOutOfBounds

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
        def real_sort(my_list):

            result = []
            if len(my_list) < 2:
                return my_list
            mid = int(len(my_list) / 2)
            y = real_sort(my_list[:mid])
            z = real_sort(my_list[mid:])
            while (len(y) > 0) or (len(z) > 0):
                if len(y) > 0 and len(z) > 0:
                    if ord(y[0]) > ord(z[0]):
                        result.append(z[0])
                        z.pop(0)
                    else:
                        result.append(y[0])
                        y.pop(0)
                elif len(z) > 0:
                    for i in z:
                        result.append(i)
                        z.pop(0)
                else:
                    for i in y:
                        result.append(i)
                        y.pop(0)
            return result
        self.data = real_sort(self.data)

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

    @staticmethod
    def length(my_list):
        count = 0
        for _ in enumerate(my_list):
            count += 1
        return count





print("SOME STRING TESTS:")
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