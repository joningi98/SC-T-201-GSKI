class Stack:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.data = [None] * self.capacity

    def push(self, value):
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1

    def pop(self):
        ret_value = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return ret_value

    def resize(self):
        self.capacity *= 2
        temp = [None] * self.capacity
        for ix in range(self.size):
            temp[ix] = self.data[ix]
        self.data = temp


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack.data)
my_stack.pop()
print(my_stack.data)
my_stack.push(88)
print(my_stack.data)
