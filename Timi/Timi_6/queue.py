class Queue:
    def __init__(self):
        self.front = 0
        self.size = 0
        self.capacity = 4
        self.data = [None] * self.capacity

    def add(self, value):
        if self.capacity == self.size:
            self.resize()
        avail = (self.front + self.size) % self.capacity
        self.data[avail] = value
        self.size += 1

    def remove(self):
        self.data[self.front] = None
        self.front += 1
        self.size -= 1

    def resize(self):
        self.capacity *= 2
        temp = self.data
        self.data = [0] * self.capacity
        walk = self.front
        for ix in range(self.size):
            self.data[ix] = temp[walk]
            walk = (walk + 1) % len(temp)
        self.front = 0


my_queue = Queue()

my_queue.add(4)
my_queue.add(5)
my_queue.add(6)
my_queue.add(9)

print(my_queue.front)
print(my_queue.data)

my_queue.remove()
print(my_queue.data)

my_queue.add(10)
print(my_queue.data)

my_queue.add(11)
print(my_queue.data)

my_queue.remove()
print(my_queue.data)

