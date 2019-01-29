class Stack:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.data = [0] * self.capacity

    def pop(self):
        self.size -= 1
        the_pop = self.data[self.size - 1]
        self.data[self.size] = 0
        return the_pop

    def push(self, value):
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1

    def resize(self):
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for ix in range(self.size - 1, -1, -1):
            new_arr[ix] = self.data[ix]
        self.data = new_arr


my_arr = Stack()

my_arr.push(4)

print(my_arr.data)

my_arr.push(5)
my_arr.push(6)
my_arr.push(7)
my_arr.push(8)

print(my_arr.data)

my_arr.pop()

print(my_arr.data)


