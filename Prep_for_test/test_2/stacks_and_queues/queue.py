class Queue:
    def __init__(self):
        self.capacity = 4
        self.front = 0
        self.size = 0
        self.data = [None] * self.capacity

    def remove(self):
        ret_value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.size
        self.size -= 1
        return ret_value

    def add(self, value):
        if self.size == self.capacity:
            self.resize()
        avail = (self.front + self.size) % self.capacity
        self.data[avail] = value
        self.size += 1

    def resize(self):
        self.capacity *= 2
        temp = self.data
        self.data = [None] * self.capacity
        walk = self.front
        for ix in range(self.size):
            self.data[ix] = temp[walk]
            walk = (walk + 1) % len(temp)
        self.front = 0

my_q = Queue()

my_q.add(1)
my_q.add(2)
my_q.add(3)
print(my_q.data)
my_q.remove()
print(my_q.data)
my_q.add(5)
my_q.add(6)
my_q.add(7)
print(my_q.data)