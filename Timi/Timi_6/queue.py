class Queue:
    def __init__(self):
        self.start = 0
        self.stop = 0
        self.capacity = 4
        self.data = [0] * self.capacity

    def add(self, value):
        if self.start - 1 == self.stop:
            self.resize()
        self.data[self.stop] = value
        self.stop += 1

    def remove(self):
        self.data[self.start] = 0
        self.start += 1

    def resize(self):
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for ix in range(self.stop, -1, -1):
            new_arr[ix] = self.data[ix]
        self.data = new_arr


my_queue = Queue()

my_queue.add(4)
my_queue.add(5)
my_queue.add(6)
my_queue.add(9)

print(my_queue.start)
print(my_queue.data)

my_queue.remove()
print(my_queue.data)
my_queue.remove()
print(my_queue.data)





